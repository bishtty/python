

guest_list = ['daadi', 'daada', 'naani', 'naana']
print("you are invited to special dinner: ", guest_list[0])
print("you are invited to special dinner: ", guest_list[1])
print("you are invited to special dinner: ", guest_list[2])
print("you are invited to special dinner: ", guest_list[3])
print('number of guest coming are: ', len(guest_list))
not_coming = 'daada'
guest_list.remove('daada')
print('\n', not_coming, " will not be able to make it")

guest_list.append('indira gandhi')
print("new guest list: ", guest_list)
print("\nI hope you guys will be able to make it: ", guest_list[0])
print("I hope you guys will be able to make it: ", guest_list[1])
print("I hope you guys will be able to make it: ", guest_list[2])
print("I hope you guys will be able to make it: ", guest_list[3])

# again adding more folks in the guest_list
guest_list.insert(0, 'savitri bai phule')
guest_list.insert(2, 'sardar patel')
guest_list.append('annie besant')
print("\nI hope you guys will be able to make it: ", guest_list[0])
print("I hope you guys will be able to make it: ", guest_list[1])
print("I hope you guys will be able to make it: ", guest_list[2])
print("I hope you guys will be able to make it: ", guest_list[3])
print("I hope you guys will be able to make it: ", guest_list[4])
print("I hope you guys will be able to make it: ", guest_list[5])
print("I hope you guys will be able to make it: ", guest_list[6])

print('sorry, I can invite only two people')

# removing guest using pop command
popped_guest = guest_list.pop() #1
print('\ni am sory i cant invited you to dinner', popped_guest.title())
popped_guest = guest_list.pop()#2
print('i am sory i cant invited you to dinner', popped_guest.title()) 
popped_guest = guest_list.pop()#3
print('i am sory i cant invited you to dinner', popped_guest.title()) 
popped_guest = guest_list.pop()#4
print('i am sory i cant invited you to dinner', popped_guest.title()) 
popped_guest = guest_list.pop() #5
print('i am sory i cant invited you to dinner', popped_guest.title()) 

print('\nyou guys are still invited for dinner', guest_list[0])
print('you guys are still invited for dinner', guest_list[1])

del guest_list[0]
del guest_list[0]
print(guest_list, ' guest list is now empty')
