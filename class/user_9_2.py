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
        great = f"I congratulate you , {self.first} {self.last}! "
        return great



user_1 = User('Anfrii', 'Swarovski', 'Man', '42')

print(user_1.great_user())
