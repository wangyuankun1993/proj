def greet_users(names):
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)