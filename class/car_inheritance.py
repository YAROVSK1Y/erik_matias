class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage

        else:
            print("You can't roll back an odometer!")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


    def describe_battery(self):
        print(f"This car has a {self.battery_size} -- kWh battery.")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")


class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a\t" + str(self.battery_size) + "\tkWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about\t"+ str(range) + "\tmiles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print(f"-------------------------------------\n"
            "It's car has upgrade.\nHe has: 100 kWt battery.\n"
                  "--------------------------------------")
        else:
            print("It's car NOT upgraded! ")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def change_battery(self, battery_size):
        self.battery = battery_size


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def change_battery(self, battery_size):
        self.battery = battery_size


my_logan = Car('renault', 'logan', 2007)
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_deskriptive_name())

my_tesla.battery.describe_battery()
my_tesla.change_battery(100)
my_tesla.battery.describe_battery()

