nota1 = float(input("Diga o valor da primeira nota\n"))
nota2 = float(input("Diga o valor da segunda nota\n"))

med = (nota1 + nota2)/2

if med < 10:
    print("Nota negativa! És péssimo! >:(")
elif med >= 10 and med <= 17:
    print("Nota fixe mas podias fazer melhor -_-")
else:
    print("Parabéns Zé! :D")
