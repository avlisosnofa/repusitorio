numero1 = int(input("Digite um número\n"))
numero2 = int(input("Insira outro número\n"))
numero3 = int(input("Quantos numeros avançam\n"))

print(f'Os números entre {numero1} e {numero2} que aumentam de {numero3} em {numero3} são:')
for i in range(numero1, numero2 + 1, numero3):
    print(i, end=' ')