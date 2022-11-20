
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskriptive_name(self):

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometr(self, mileage):
        """ Відкинути змінну у разі спроби відмотати заначення """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer ")

    def increment_odometer(self, miles):
        """ Додати задане значення до показника одометра """
        self.odometer_reading += miles
        print(miles)

my_new_car = Car('audi', 'a4', '2019')
#print(my_new_car.get_deskriptive_name())

my_used_car = Car('subaru', 'outback', '2015')

my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increment_odometer(1001)
my_used_car.read_odometr()
my_used_car.update_odometr(900)



