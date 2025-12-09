import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.conf import settings
from jwt import decode as jwt_decode
from openai import AsyncOpenAI

from .models import ChatSession, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--- DEBUG: WebSocket Auth via Tor/Local ---")
        try:
            query_string = self.scope['query_string'].decode()
            if 'token=' not in query_string:
                await self.close()
                return
            
            token = query_string.split('token=')[-1]
            user = await self.get_user_from_token(token)
            
            if user is None:
                await self.close()
                return
            
            self.scope['user'] = user
            await self.accept()
            print(f"User {user.id} Connected")

        except Exception as e:
            print(f"Connection Error: {e}")
            await self.close()

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            user_message = data.get('message', '')
            session_id = data.get('session_id')
            user = self.scope['user']

            session = await self.get_or_create_session(user, session_id)
            
            await self.save_message(session, Message.Role.USER, user_message)

           
            ai_response = await self.call_llm_with_fallback(user_message)

            await self.save_message(session, Message.Role.ASSISTANT, ai_response)

            await self.send(text_data=json.dumps({
                'message': ai_response,
                'session_id': session.id
            }))

        except Exception as e:
            await self.send(text_data=json.dumps({'error': str(e)}))

    async def call_llm_with_fallback(self, prompt):
        """
        Essaie de contacter Ollama (Local). Si échoue, utilise Mock.
        """
        try:
            client = AsyncOpenAI(
                base_url="http://localhost:11434/v1", 
                api_key="ollama",
                timeout=5.0 
            )
            response = await client.chat.completions.create(
                model="llama3.2", 
                messages=[
                    {"role": "system", "content": "You are an empathetic nutrition coach."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception:
            await asyncio.sleep(1)
            return f"🤖 [Mock AI]: Je suis le coach IA (Simulation). Serveur LLM indisponible. J'ai bien reçu: '{prompt}'"

    @database_sync_to_async
    def get_user_from_token(self, token):
        try:
            payload = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return User.objects.get(id=payload.get('user_id'))
        except:
            return None

    @database_sync_to_async
    def get_or_create_session(self, user, session_id=None):
        if session_id:
            try:
                return ChatSession.objects.get(id=session_id, user=user)
            except ChatSession.DoesNotExist:
                pass
        return ChatSession.objects.create(user=user, session_name=f"Chat {user.username}")

    @database_sync_to_async
    def save_message(self, session, role, content):
        session.save() 
        return Message.objects.create(session=session, role=role, content=content)