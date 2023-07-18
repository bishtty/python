# storing different kind of info. about one object

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': 'green'}
print("the alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("the alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("the alien's original position: " + str(alien_0['x_position']))
# move alien to right 
# determine how far to move alien according to its speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# this must be a fast alien.
	x_increment = 3
	
# the new positiion is old position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))

# del to remove key-value pair from dictionary 
# deleted key-value is removed permanently

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

