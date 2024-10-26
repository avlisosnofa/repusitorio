print("Idioma/Language\n")
idioma= int(input("1- Português, 2-English\n"))

if idioma == 1:
    print("Bem-vindo à loja do Manel!\nCriação de novo produto\n")
    item1 = input("Qual o nome do primeiro produto? ")
    preco1 = float(input("Qual o preço do produto? "))
    quant1 = int(input("Quantos do produto existe no stock? "))

    vtotal1 = preco1 * quant1
    print()
    item2 = input("Qual o nome do segundo produto? ")
    preco2 = float(input("Qual o preço do produto? "))
    quant2 = int(input("Quantos do produto existe no stock? "))

    vtotal2 = preco2 * quant2
    print()
    item3 = input("Qual o nome do terceiro produto? ")
    preco3 = float(input("Qual o preço do produto? "))
    quant3 = int(input("Quantos do produto existe no stock? "))

    vtotal3 = preco3 * quant3

    print()
    print("Produto(1):",item1,"\nPreço(1):",preco1,"€\nQuantidade(1):",quant1,"\nValor total do stock(1):",vtotal1,"€\n")
    print("Produto(2):",item2,"\nPreço(2):",preco2,"€\nQuantidade(2):",quant2,"\nValor total do stock(2):",vtotal2,"€\n")
    print("Produto(3):",item3,"\nPreço(3):",preco3,"€\nQuantidade(3):",quant3,"\nValor total do stock(3):",vtotal3,"€\n")

elif idioma == 2:
    print("Welcome to Manel's shop!\nNew item creation\n")

    item1 = input("What's the name of the first product? ")
    preco1 = float(input("What's the price? "))
    quant1 = int(input("How many items are in stock? "))

    vtotal1 = preco1 * quant1

    print()
    item2 = input("What's the name of the second product? ")
    preco2 = float(input("What's the price? "))
    quant2 = int(input("How many items are in stock? "))

    vtotal2 = preco2 * quant2

    print()
    item3 = input("What's the name of the third product? ")
    preco3 = float(input("What's the price? "))
    quant3 = int(input("How many items are in stock? "))

    vtotal3 = preco3 * quant3

    print()
    print("Item(1):", item1, "\nPrice(1):",preco1,"€\nQuantity(1):",quant1,"\nTotal value of stock(1)",vtotal1,"€\n")
    print("Item(2):", item2, "\nPrice(2):",preco2,"€\nQuantity(2):",quant2,"\nTotal value of stock(2)",vtotal2,"€\n")
    print("Item(3):", item3, "\nPrice(3):",preco3,"€\nQuantity(3):",quant3,"\nTotal value of stock(3)",vtotal3,"€\n")

else:
    print("Resposta inválida / Invalid response")