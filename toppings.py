# use if statement- to check for more than one condition to be true
# use if-elif-else statement- when you just need to pass one test

requested_toppings = ["mushrooms", "green pepper", "extra cheese"]

# if "mushrooms" in requested_toppings:
#     print("adding mushrooms")
# if "capsicum" in requested_toppings:
#     print("adding capsicum")
# if "extra cheese" in requested_toppings:
#     print("adding extra cheese")

# page 123/562
for requested_topping in requested_toppings:
    if requested_topping == "green pepper":
        print("sorry, we are out of green pepper atm")
    else:
        print("adding "+ requested_topping + ".")

print("\nfinished making your pizza")

