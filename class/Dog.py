class Dog:
    """проста спроба стваорити собаку"""

    def __init__(self, name, age):
        """ініціювати атрибути ім'я та вік"""

        self.name = name
        self.age = age

    def sit(self):
        """Симулювати визначення команди 'сидіти' """
        print(f"{self.name} is now sitting .")

    def roll_over(self):
        """Симулювання команди 'лежати' """
        print(f"{self.name} rolled over! ")


my_dog = Dog('Willie', 6)

print(f"My dog`s name is {my_dog.name}.")
print(f"My dog's age {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

yor_dog = Dog('Lucy', '3')

yor_dog.sit()
yor_dog.roll_over()
