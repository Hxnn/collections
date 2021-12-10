def main():
import random

colors = ('Orange', 'Blauw', 'Groen', 'Bruin')


def dataZak(amount: int):
    bag = {}
    for i in range(int(amount)):
        color = random.choice(colors)
        if color in bag:
            bag[color] += 1
        else:
            bag.update({color: 1})
    return bag


question = int(input('Hoeveel M&Ms wil je in de zak? : '))
if question <= 0:
    print('Sorry, dat kan niet.')

print(sorted(dataZak(question).items(), key=lambda kv: kv[1], reverse=True))
