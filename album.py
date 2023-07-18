# exercise 8-7 pg 146/179


def make_album(artist_name, album_title, tracks=""):
	
	if tracks:
		album = {'album': album_title, 'artist': artist_name, 
				'no_of_tracks': tracks}
	else:
		album = {'album': album_title, 'artist': artist_name}
	return album

# exercise 8-8 pg 146/179
while True:
	print("\nEnter your choice of album and its artist")
	print("enter 'q' at anytime to quit")
	al_name = input("Enter album name: ")
	if al_name == 'q':
		break
	ar_name = input("Enter album artist name: ")
	if ar_name == 'q':
		break
	
	musician = make_album(al_name, ar_name)	
	print(musician)
 

# below is part of 8-7
'''
musician = make_album('aayush', 'country road', 5)
print(musician)
musician = make_album('aurora', 'a 1000 times')
print(musician)
musician = make_album('rafaella', 'bailando', 9)
print(musician)
'''





