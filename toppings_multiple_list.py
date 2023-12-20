# page 125/562

available_toppings = ["mushrooms", "olives", "green peppers",
                       "pepparoni", "extra cheese"]
requested_toppings = ["mushroons", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding " + requested_topping + '.')
    else:
        print("sorry, we are out of " + requested_topping + " atm.")

print("\nfinished making your pizza!")