from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        dei = randint(1, self.sides)
        return dei

    def throw_times(self, times=10):
        self.times_x = [randint(1, times) for i in range(times)]
        print(self.times_x)


dei = Die()
dei.roll_die()
dei.throw_times(10)


class Die10(Die):
    def __init__(self, sides=10):
        super().__init__(sides=10)
        self.sides = sides


dei10 = Die10()
dei10.roll_die()
dei10.throw_times(10)


class Dei20(Die):
    def __init__(self, sides=20):
        super().__init__(sides=20)
        self.sides = sides


dei20 = Dei20()
dei20.roll_die()
dei20.throw_times(20)
