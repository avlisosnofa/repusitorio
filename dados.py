from random import randint
from time import sleep

print('Quantas jogadas serão necessárias até aparecer 2 dados com o mesmo número?')
sleep(2)
num = 0
dado1 = 0
dado2 = 0
r = True
while (r == True):
    num += 1
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(dado1)
    print(dado2)
    sleep(0.2)
    print()
    if (dado1 == dado2):
        print(f'Os dois dados têm o mesmo valor depois de {num} tentativas')
        r = False
