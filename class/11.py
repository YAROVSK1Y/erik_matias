# # # # class Dog:
# # # #
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #
# # # #     def sit(self):
# # # #         print(f"{self.name} is now siting.")
# # # #
# # # #     def roll_over(self):
# # # #         print(f"{self.name} roll over.")
# # # #
# # # #
# # # # my_dog = Dog('Willie', '6')
# # # # print(f"My dog's name is {my_dog.name}")
# # # # print(f"My dog's age is {my_dog.age}")
# # # # your_dog = Dog('Lucie', '3')
# # # # print(f"Your dog's name is {your_dog.name}")
# # # # print(f"Your dog's age is {your_dog.age}")
# # # # my_dog.roll_over()
# # # # your_dog.sit()
# # #
# # # class Restaurant:
# # #     def __init__(self, restaurant_name, cuisine_type):
# # #         self.restaurant_name = restaurant_name
# # #         self.cuisine_type = cuisine_type
# # #
# # #     def describle_restaurant(self):
# # #         print(f"Restaurant name is {self.restaurant_name}\n"
# # #               f"Here is {self.cuisine_type} cuisine.")
# # #
# # # restaurant_1 = Restaurant("McDonald's", "fast food")
# # # print(f"{restaurant_1.restaurant_name}{restaurant_1.cuisine_type}")
# # # restaurant_1.describle_restaurant()
# # #
# #
# #
# # class Restaurant:
# #     def __init__(self, name_restaurant, cuisine_restaurant):
# #         self.restaurant = name_restaurant
# #         self.cuisine = cuisine_restaurant
# #
# #     def deskrible_restaurant(self):
# #         print(f"This restaurant name is {self.restaurant}\nHere is {self.cuisine} cuisine.")
# #
# #     def open_restaurant(self):
# #         print(f"Restaurant {self.restaurant} is open.")
# #
# #
# # rest_1 = Restaurant("Restoooorant", 'Taufel')
# #
# # rest_1.open_restaurant()
# # rest_1.deskrible_restaurant()
# #
#
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_deskriptive_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print(f"You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# my_car = Car('audi', 'a4', '2019')
# print(my_car.get_deskriptive_name())
# my_car.read_odometer()
# my_car.odometer_reading = 23
# my_car.read_odometer()
# my_car.update_odometer(22)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()



#
#
# class Restaurant:
#     def __init__(self, name_restaurant, cuisine_restaurant):
#         self.restaurant = name_restaurant
#         self.cuisine = cuisine_restaurant
#         self.number_served = 0
#
#     def deskrible_restaurant(self):
#         print(f"This restaurant name is {self.restaurant}\nHere is {self.cuisine} cuisine.")
#
#     def open_restaurant(self):
#         print(f"Restaurant {self.restaurant} is open.")
#
#     def served_reading(self):
#         print(f"Klientov - {self.number_served}")
#
#     def change_quantity(self, quantity):
#         self.number_served = quantity
#
#     def inkrement_quantity(self, increment):
#         self.number_served += increment
#
# rest_1 = Restaurant("Restoooorant", 'Taufel')
#
# rest_1.open_restaurant()
# rest_1.deskrible_restaurant()
# print(rest_1.number_served)
# rest_1.served_reading()
# rest_1.change_quantity(100)
# rest_1.served_reading()
# rest_1.inkrement_quantity(120)
# rest_1.served_reading()
# rest_1.inkrement_quantity(-220)
# rest_1.served_reading()

class User:
    def __init__(self, name, age):
        self.user_name = name
        self.user_age = age
        self.login_atempts = 0

    def describle_user(self):
        user_info = f"It's {self.user_name}\nAge {self.user_age} year old. "
        return user_info.title()

    def great_user(self):
        great_user_now = f"Viva {self.user_name}"
        return great_user_now.title()


user_1 = User('andrii', 42)
user_1.describle_user()

print(user_1.describle_user())
print(user_1.great_user())






