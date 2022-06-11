year = int(input("Insira o ano que você que checar se é bissexto: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("O ano é bissexto")
        else:
            print("O ano não é bissexto")
    else:
        print("O ano é bissexto")
else:
    print("O ano não é bissexto")



    


