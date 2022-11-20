class Car:
    """ Проста спроба моделювати автівку """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskriptive_name(self):
        """ Поварнути відформатоване змітовне ім'я """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Вивести повідомлення з пробігом машини """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milage):
        """
        Встановити значення одометра.
        Відкинути зміни яущо йдеться про відмотування значеннь одометра.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Додати задане значення до показника одометра. """
        self.odometer_reading += miles


