class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_reise(self, sum_up=5000):
        self.sum_up = sum_up
        self.salary += sum_up

    def slow_me_person(self):
        person = f"{self.name} {self.surname} {self.salary}"
        print(person)

#
# man = Employee("Jan", "Peck", 2000)
# man.give_reise(300)
# man.slow_me_person()



