from time import sleep

num = int(input("Qual o número inicial?\n"))
while num > 0:
    print(num)
    num -= 1
    sleep(1)
print("Lançar!")