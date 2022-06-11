print("Seja bem-vindo a Montanha-Russa!")
height = int(input("Qual é sua altura em cm? "))


if height >= 120:
    print("Você tem altura permitida")
    idade = int(input("Qual é sua idade? "))
    if idade < 12:
        print("O ticket custa R$5,00")
        foto = str(input("Você deseja foto? "))
        if foto == "sim":
            print("Vai custar R$3,00 a mais")
            print(f"Ficou R$8,00")
        else:
            print("O ticket custa R$5,00")

    elif idade >= 12 and idade < 18:
        print("O ticket custa R$7,00")
        foto = str(input("Você deseja foto? "))
        if foto == "sim":
            print("Vai custar R$3,00 a mais")
            print(f"Ficou R$10,00")
        else:
            print("O ticket custa R$7,00")

    else:
        print("O ticket custa R$10,00")
        foto = str(input("Você deseja foto? "))
        if foto == "sim":
            print("Vai custar R$3,00 a mais")
            print(f"Ficou R$13,00")
        else:
            print("O ticket custa R$10,00")
else:
    print("Você não tem altura mínima permitida!")