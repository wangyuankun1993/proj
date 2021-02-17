import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename, 'w') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'user.json'
    with open(filename, 'w') as f_ojb:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        result = input(username + " is right?")
        if result:
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()