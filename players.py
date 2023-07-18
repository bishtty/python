# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print(players[0:3]) # this will print from 0-2
#print(players[1:4]) # this will print from 1-3
#print(players[:4]) # print from starting till 3rd position
#print(players[2:])
#print(players[-3:]) # will print from last value in same order

print(' here is the list of first 3 players')
for player in players[:3]:
	print(' ', player.title())

