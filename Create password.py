import string
import random

passnum =int(input('How many passwords\n'))


def do():
    carnum =int(input('How many charaters\n'))
    chara = string.ascii_letters
    ran = random.choices(chara, k= carnum)
    x = ''.join(ran)
    print(x)

for _ in range(passnum):
    do()