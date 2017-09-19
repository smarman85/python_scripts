import json
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

print(type(best_food_chains))

best_food_chains_string = json.dumps(best_food_chains)

print(type(best_food_chains_string))

print(type(json.loads(best_food_chains_string)))

fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
