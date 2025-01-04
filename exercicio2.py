from random import randint

num = randint(1,100)

resp = int(input("Advinhe o número entre 1 a 100\n"))
erro = 0

while resp != num:
    print("Errado!")
    if num > resp:
        print(f"É maior do que {resp}")
    elif num < resp:
        print(f"É menor do que {resp}")
    resp = int(input("Tente novamente\n"))
    erro +=1

print(f"Acertou o número {num}!\nErrou {erro} vezes")
