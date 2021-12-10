import random

spelList = ('Monopoly', 'Yahtzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo')


def spelProgramma(spelList,minimum = 3, maximum = 10):
    x = random.choice(range(minimum,maximum))
    return random.choices(spelList, k=x)


print(spelProgramma(spelList))
print(spelProgramma(spelList, 1))
print(spelProgramma(spelList, 3))
