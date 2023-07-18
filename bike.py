
bikes = ['honda', 'cafe racer', 'yezdi', 'r15']
print("one day I would like to own a " + bikes[1].title() + " bike")
print(bikes)

bikes[1] = "RE-650X"
print(bikes)

# adding new item in list through append()
bikes.append('continental-GT')
print(bikes)

# creating dynamic list using append()
fav_bikes = []
fav_bikes.append('splendor')
fav_bikes.append('R1')
fav_bikes.append('cafe racer')
print('\n created dynamic list using append(): ',fav_bikes)

# adding new item at any position using insert()
fav_bikes.insert(0, 'ducati')
print('\n Inserted using list(): ', fav_bikes)

# removing item from list using del statement
del fav_bikes[1]
print(fav_bikes)

# using pop() to remove last item from list and still we can access the removed item
popped_bike = fav_bikes.pop()
print(fav_bikes)
print(popped_bike)

#using remove() to remove the item if you dont know the position
print('\n', bikes)
bikes.remove('r15')
print('\n', bikes)

bikes.append('ducati')
print(bikes)

too_expensive = 'ducati'
bikes.remove('ducati')
print(bikes)
print('\nA ' + too_expensive.title() + " is too expensive for me.")
