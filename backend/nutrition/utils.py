import time
import random

def analyze_meal_photo_mock(image_path_or_name):
    """
    Simule l'analyse visuelle d'un plat (Local LLM Vision).
    Retourne une liste d'aliments reconnus et le total calorique.
    """
    time.sleep(2)
    
    name_lower = image_path_or_name.lower()
    
    if "pizza" in name_lower:
        foods = [{"name": "Pizza Margharita", "calories": 250, "protein": 10, "carbs": 30, "fat": 10}]
        total = 250
    elif "salad" in name_lower or "salade" in name_lower:
        foods = [{"name": "Salade Verte", "calories": 50, "protein": 2, "carbs": 5, "fat": 3}]
        total = 50
    elif "burger" in name_lower:
        foods = [{"name": "Cheeseburger", "calories": 450, "protein": 25, "carbs": 40, "fat": 20}]
        total = 450
    else:
        # Default (Poulet Grillé etc)
        foods = [
            {"name": "Poulet Grille", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
            {"name": "Riz Basmati", "calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
            {"name": "Brocoli Vapeur", "calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.6}
        ]
        total = 350
        
    return {
        "foods": foods,
        "total_calories": total
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