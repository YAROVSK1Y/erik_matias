from random import randint
from random import choice

class Die:
    def __init__(self, sides=6):
      randint(1, sides)
    def roll_die(self):
        choise = randint(1, 6)
        print(choise)

    def roll_die_choise(self):
        players = ['Хорватія', 'Італія', 'Іспанія',
                   'Греція', 'Німеччина']
        first_up = choice(players)
        print(f"{first_up}?")
play = Die()
#play.roll_die()
print(f"В яку країну поїдемо пожити")

play.roll_die_choise()
