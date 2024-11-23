nota = int(input("Qual é a sua nota:"))

match nota:
    case 0:
        print("És um burro")
    case 9:
        print("Quase lá!")
    case 10:
        print("Ótimo, podes melhorar")
    case 15:
        print("Bom,estude mais!")
    case 18:
        print("Muito, podes melhorar!")
    case 19:
        print("Muito bom, vais receber uma prenda de natal!")
    case 20:
        print("Excelente!!! És o melhor")
    case _:
        print("Nota não reconhecida!!! HAHHA")