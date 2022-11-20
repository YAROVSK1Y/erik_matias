from user_privileges_admin import User
from  user_privileges_admin import Admin
from user_privileges_admin import Privileges

user_1 = User('Andrii', 'Yarovskiy', 'male', 42)
print(user_1.great_user())
user_2 = Admin('Olja', 'Peck', 'female', 44)
user_2.describe_user()
print(user_2.great_user())


privileges = Privileges
user_2.show_privileges()