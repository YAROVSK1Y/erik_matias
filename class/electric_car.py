from car import Car
class Battery:
    def __init__(self, battery_size=70):
        """ Проста спроба змоделювати аккумулятор електрокара. """
        self.battery_size = battery_size
    def describle_battery(self):
        """ Вивести повідомлення про розмір аккумулятора. """
        print(f"This car has a {self.battery_size} kWt battery.")

    def get_range(self):
        """ Вивести повідомлення про відстань,
         яку може подолати авто відповідно до ємності аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectroCar(Car):
    """ Змоделювати властивості притаманні електрокарам. """
    def __init__(self, make, model, year):
        """  Ініціаліщувати атрибути батьківського класу.
         Тоді ініціалізувати атрибути електрокара."""
        super().__init__(make, model, year)
        self.battery = Battery()