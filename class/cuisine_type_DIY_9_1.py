class Restautant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def desctible_restaurant(self):
        print(f"This restaurant called -= {self.name} =- end here serves -="
              f" {self.cuisine} =- cuisine.")

    def open_restaurant(self):
        print(f"This restaurant now is open.")

restaurant = Restautant('YA', 'Ukrainian')
print(f"My restaurant colled {restaurant.name}")
restaurant.open_restaurant()



restaurant1 = Restautant('Pershii', 'ohne_küche')
print(f"'{restaurant1.name}' ось такий ресторан "
      f"\nі тут не готують, тому що {restaurant1.cuisine}")


restaurant2 = Restautant('Essen', 'etwas')


restaurant3 =Restautant('Їжа для людей', 'щось їстівне')







