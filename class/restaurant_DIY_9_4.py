class Restautant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.numbers_served = 0

    def desctible_restaurant(self):
        print(f"_____________________________________\n"
              f"This restaurant called -='{self.name}'=-.\n"
              f"Here serves -={self.cuisine}=- cuisine.\n"
              f"_____________________________________")

    def open_restaurant(self):
        print(f"This restaurant now is open.")

    def set_number_served(self):
        print(f"Now restorant have - {self.numbers_served} users.")

    def inkrement_number_served(self, visitors):
        self.numbers_served += visitors



# restaurant = Restautant('YA', 'Ukrainian')
# print(f"My restaurant colled {restaurant.name}")
# restaurant.inkrement_number_served = 188
# print(restaurant.inkrement_number_served)
#
# restaurant.numbers_served = 122
# restaurant.set_number_served()




