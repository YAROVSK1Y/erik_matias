class User:
    def __init__(self, first_name, last_name, gender, age ):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.login_attempts = 0
        self.gender = gender

    def describe_user(self):
        print(f"\nThis is {self.gender},  {self.first} {self.last}.\n"
              f"She/He {self.age} years old.")

    def great_user(self):
        great = f"I congratulate you , {self.first} {self.last}! "
        return great

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

user_1 = User('Anfrii', 'Yarovskiy', 'Man', '42')
user_1.describe_user()

print(f" Attempt to login in |{user_1.login_attempts}| ")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f" Attempt to login in |{user_1.login_attempts}| ")



