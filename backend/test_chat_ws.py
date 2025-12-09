import asyncio
import websockets
import json

async def main():
    async with websockets.connect("ws://127.0.0.1:8000/ws/chat/") as ws:
        print(await ws.recv())
        await ws.send(json.dumps({"message": "Bonjour AI"}))
        print(await ws.recv())

asyncio.run(main())

