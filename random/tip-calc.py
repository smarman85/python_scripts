def meal_price(meal):
    meal = meal + meal * .08
    return meal

def tip_ammount(meal, percent):
    tip = meal * percent / 100
    return tip

def final_ammount(meal, percent_tip):
    meal_only = meal_price(meal)
    tip_only  = tip_ammount(meal, percent_tip)
    total = meal_only + tip_only
    return "%.2f" % total

print final_ammount(50.78, 17)
