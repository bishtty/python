# using slice operator and looping through slice operator
friends = ["auri", "maff-ox", "bsihty", "nomi", "akher", "cindy", "jenny", "alli"]
for friend in friends[:3]:
    print(friend + " is my friends from powerful student server")

# to copy a list 
my_food = ["pav bhaji", "khichdi", "tofu", "idli"]
friends_food = my_food[:]

print("my favourite food is ")
print(my_food)
print("my friends favourite food is ")
print(friends_food)

# to add extra item in list we use append()
my_food.append("jalebi")
friends_food.append("kalakand")

print(my_food)
print(friends_food)