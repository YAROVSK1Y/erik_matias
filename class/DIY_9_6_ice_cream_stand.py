class Restautant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def desctible_restaurant(self):
        print(f"This restaurant called -={self.name}=- "
              f"end here serves -={self.cuisine}=- cuisine.")

    def open_restaurant(self):
        print(f"This restaurant now is open.")

restaurant = Restautant('YA', 'Ukrainian')


class IceCreamStand(Restautant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['bananas', 'ananas', 'peer']

    def show_flavors(self):
        for flavor in self.flavors:

            print(f"{flavor.title()}")

ice_cream = IceCreamStand('Malukam', 'Icecream')
ice_cream.show_flavors()
ice_cream.desctible_restaurant()

