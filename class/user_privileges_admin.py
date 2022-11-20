class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"\nThis is {self.gender},  {self.first} {self.last}.\n"
              f"She/He {self.age} years old.")

    def great_user(self):
        great = f"I congratulate you, {self.first} {self.last}! "
        return great


class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privileg in self.privileges:
            print(privileg.title())

class Privileges:
    def __init__(self):
        self.user_privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privileg in self.user_privileges:
            print(privileg.title())

user1 = User('andrey', 'yarovskiy', 'male', '42')
print(user1.describe_user())
