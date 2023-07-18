# exercis 5-8 pg93

usernames = ['admin', 'auri', 'bishty', 'maff_ox', 'franci', 'mari']

for user in usernames:
    if user == 'admin':
        print('hello ' + user + 
              ', would you like to see a status report?')
    else:
        print('hello ' + user + ', thankyou for logging in again.')
        
