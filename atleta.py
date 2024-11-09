from datetime import date

n = int(input("Qual foi o ano de nascimento do atleta?\n"))
hoje = date.today().year

i = hoje - n

if i <= 9:
    print("Mirim")
elif i > 9 and i <= 14:
    print("Infantil")
elif i > 14 and i <= 19:
    print("Junior")
elif i > 19 and i <= 25:
    print("Senior")
else:
    print("Master")