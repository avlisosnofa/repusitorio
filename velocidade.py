velocidade_ult = float(input("Qual é a velocidade que o veículo passou por um radar?"))
match velocidade_ult:
    case 80:
        print("O condutor encontrasse dentro do limite de velocidade")
    case _:
        y = velocidade_ult - 80
        x = 2 *y

        print(f"A multa é de {x} euros")