# exercise 5-10

current_users = ["mari", "auri", "bishty", "maff-ox", "francesca"]
new_users = ["aayush", "aurora", "mari", "rafaella", "francesca"]

for username in new_users:
    if username in current_users:
        print("'" + username + "' username is already in use.")
    else:
        print("'" + username + "' username is available.")
