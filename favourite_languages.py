# page134/562
favourite_languages = {"jen": "python", "sarah": 'c', "edward": "ruby"}
print(favourite_languages)

for name, language in favourite_languages.items():
    print(name + "'s favourite language is " + language)

# to print just keys we use keys()    
for name in favourite_languages.keys():
    print(name)

# to print values we use values()
for language in favourite_languages.values():
    print(language)

friends = ["phill", "sarah"]
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" hi " + name.title() + 
              ", your favourite language is " + 
              favourite_languages[name].title())
        