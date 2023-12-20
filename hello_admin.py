# page 125/562

usernames = ["mari", "auri", "admin", "maff-ox", "francesca"]
if usernames:
    for username in usernames:
        if username == "admin":
            print("hello admin, would you like to see a status report")
        else:
            print("hello " + username + ", thanyou for logging in again")

else:
    print("we need to find some users!")

