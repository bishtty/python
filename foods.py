# copying list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(' my fav. food are:', my_foods)
print(' friends fav. food are:', friend_foods)

my_foods.append('canoli')
friend_foods.append('ice cream')

print(' \nmy fav. food are(updated):', my_foods)
print(' friends fav. food are(updated):', friend_foods)

# this will not work, it will concatinate both list
my_foods = friend_foods
print(' my fav. food are:', my_foods)
print(' friends fav. food are:', friend_foods)
