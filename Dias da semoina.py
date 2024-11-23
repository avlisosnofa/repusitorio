dia = input("Qual dia da semana é? ")
match dia:
    case "Segunda-feira":
        atividade = "Ir correr ao parque"
    case "Terça-feira":
        atividade = "Tomar banho"
    case "Quarta-feira":
        atividade = "Anseia-se para o final desta semana"
    case "Quinta-feira":
        atividade = "Passear com o cão"
    case "Sexta_feira":
        atividade = "Ir ao cinema"
    case "Sábado":
        atividade = "Progamar"
    case "Domingo":
        atividade = "Dormir"
    case _:
        atividade = "Dia invalido"
print(atividade)