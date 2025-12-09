from datetime import date

def calculate_daily_calories(user):
    """
    Calcule le BMR et TDEE basé sur l'équation Mifflin-St Jeor.
    """
    if not all([user.date_of_birth, user.height_cm, user.current_weight_kg, user.gender]):
      
        return 2000 

  
    today = date.today()
    age = today.year - user.date_of_birth.year - (
        (today.month, today.day) < (user.date_of_birth.month, user.date_of_birth.day)
    )

   
    weight = user.current_weight_kg
    height = user.height_cm
    
    bmr = (10 * weight) + (6.25 * height) - (5 * age)

    if user.gender == 'M':
        bmr += 5
    else:
        bmr -= 161

  
    multipliers = {
        'SED': 1.2,   
        'LIG': 1.375, 
        'MOD': 1.55,  
        'ACT': 1.725, 
        'VER': 1.9    
    }
    
    
    activity_multiplier = multipliers.get(user.activity_level, 1.2)
    tdee = bmr * activity_multiplier

    
    if user.target_weight_kg and user.target_weight_kg < user.current_weight_kg:
       
        target_calories = int(tdee - 500)
        
        
        return max(target_calories, 1200)
    
   
    return int(tdee)