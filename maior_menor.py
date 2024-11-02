num1 = int(input("Insira o primeiro numero\n"))
num2 = int(input("Insira o segundo numero\n"))
num3 = int(input("Insira o terceiro numero\n"))

if num1 > num2 and num1 > num3:
    print("O número", num1,"é o maior")
elif num1 < num2 and num2 > num3:
    print("O número", num2,"é o maior")
elif num3 > num2 and num1 < num3:
    print("O número", num3,"é o maior")