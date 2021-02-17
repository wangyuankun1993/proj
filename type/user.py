class User():
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("The user name is " + self.fn.title() + self.ln.title())

    def greet_user(self):
        print("Welcome, " + self.fn.title() + self.ln.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_attempts(self):
        print(self.login_attempts)