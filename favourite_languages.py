# one kind of info about many object

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python'
    }

    
print("Sarah's favorite language is " +
	favourite_languages['sarah'].title() +
	".")

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite languege is " +
		language.title() + ".") 

'''	
friends = ['phill', 'sarah']
for name in favourite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" hi " + name.title() + 
			", I see your favorite language is " + 
			favourite_languages[name].title() + "!")
'''	
'''
# wrapping sorted() around dictionary,keys()
		
for name in sorted(favourite_languages.keys()):
	print(name.title() + ", thankyou for taking the poll.")
'''
print("\nthe choosen languages for the program are mentioned:")
for language in favourite_languages.values():
	print(language.title()) 
# this method might lead to repetitive printing of same language
# set() is used to avoid repetition	
