class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskriptive_name(self):
        deskriptive = f"{self.make} {self.model} {self.year}"
        return deskriptive

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} on it.")

    def update_odometer(self, milage):

        if milage >= self.odometer_reading:
            self.odometer_reading = milage
            print(f"The value {milage} is updated")
        else:
            print("Error")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def deskrible_battery(self):
        print(f"This car has a {self.battery_size} - kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full change.")

class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(100)




my_avto = Car('renault', 'logan', '2007')
my_tesla = ElectriCar('tesla', 'model s', '2019')
print(my_tesla.get_deskriptive_name())
my_tesla.battery.deskrible_battery()
my_tesla.battery.get_range()
