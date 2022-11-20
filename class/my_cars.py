from car import Car
from electric_car import ElectroCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_deskriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_deskriptive_name())


