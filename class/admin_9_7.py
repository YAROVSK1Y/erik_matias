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
        print(great)


class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privileg in self.privileges:
            print(privileg.title())

#
#user_1 = User('Andrii', 'Yarovski', 'Man', '42')
# user_2 = Admin('Olja', 'Peck', 'Woman', '44')
#user_1.great_user()
# print(f"\n{user_2.great_user()}\nYou can:\n")
# user_2.show_privileges()
