
seeing_the_world = ['italy', 'germany', 'sardania', 'turkey', 'france']
print(seeing_the_world)

print('\nhere is temporarily sorted list: \n', sorted(seeing_the_world))
print('here is the original list: \n', seeing_the_world)
print('here is temporarily sorted list in reverse order: \n', sorted(seeing_the_world, reverse=True))

seeing_the_world.reverse()
print(seeing_the_world)
seeing_the_world.reverse()
print(seeing_the_world)
seeing_the_world.sort()
print("here is the sorted list: \n", seeing_the_world)
seeing_the_world.sort(reverse=True)
print('here is the reverse sort list: \n', seeing_the_world)
