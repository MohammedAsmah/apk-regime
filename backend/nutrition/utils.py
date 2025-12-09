import time
import random

def analyze_meal_photo_mock(image_path):
    """
    Simule l'analyse visuelle d'un plat (Local LLM Vision).
    Retourne une liste d'aliments reconnus et le total calorique.
    """
    time.sleep(2)
    
    return {
        "foods": [
            {"name": "Poulet Grillé", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
            {"name": "Riz Basmati", "calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
            {"name": "Brocoli Vapeur", "calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.6}
        ],
        "total_calories": 350
    }

def generate_meal_plan_mock(user_profile, constraints):
    """
    Simule la génération de plan par Llama 3.
    """
    time.sleep(1.5)
    
    target_cal = constraints.get('target_calories', 2000)
    meals_count = constraints.get('meals_per_day', 3)
    
    generated_meals_data = []
    
    for i in range(meals_count):
        cal_share = int(target_cal / meals_count)
        generated_meals_data.append({
            "name": f"Repas IA {i+1}",
            "foods": ["Oeufs", "Avocat", "Pain Complet"] if i == 0 else ["Saumon", "Quinoa"],
            "calories": cal_share
        })
        
    return generated_meals_data