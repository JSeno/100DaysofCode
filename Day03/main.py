print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Você está em uma trilha na ilha e próximo de uma grande rocha você olha e vê dois caminhos um em indo para o Leste o o outro indo para o Oeste.")
direction1 = input("Qual caminho você deseja seguir? \n")
if direction1 == "Leste":
    print("Você segue adentrando a uma densa mata e começa escutar um som de um rio e segue adiante.")
    print("Após caminhar por algumas horas você olha e ve um uma cachoeira alta e um pequeno rio e começa olha em volta.")
    print("De repente você começa escutar soms cada vez mais altos vindo em sua direção.\nVocê não sabe de onde vem fica assustado o que você faz?")
    direction2 = input("Você aguarda para ver o que acontece ou resolve nadar para na tentativa de fugir do som?\n ")
    if direction2 == "aguardar":
        print("O que sai da mata nada mais é que um cervo mais assustado que você e olha em sua direção e sai correndo adentrando a mata novamente.")
        print("Você olha aliviado e resolve continuar sua jornada e resolve subir a cachoeira.\nE ve uma antiga fortaleza dos tempos de guerra e caminha em direção a ela.")
        print("Entrando na fortaleza e vasculando você acaba em um corredor onde há três portas que leva em diferentes direções.")
        directtion3 = input("Tem a porta que fica a sua esquerda, uma que está bem a sua frente e outra bem a direita.\nQual porta você deseja seguir?\n ")
        if directtion3 == "esquerda":
            print("Você força a entrada da porta consegue arromba-la escuta um som de algo estourando antes mesmo de saber o que aconteceu,")
            print("você cai morto. Havia sido acertado com uma flecha de uma besta. Era uma armadilha que havia sido deixada há muito tempo.")
        elif directtion3 == "direita":
            print("Você toca na maçaneta e ela se desfaz em sua mão, consegue abrir a porta sem dificuldade alguma.")
            print("Você olha para a sala e vê que ali era um quarto que deveria ter pertencido alguma pessoa muito importante na época.")
            print("Havia muitas antiguidades que resistiram ao tempo assim como tesouros você pega tudo e foge da fortaleza buscando caminho para casa.")
        else:
            print("Você não tem dificuldade em abrir a porta conforme vai andando o chão se desfaz você cai em um buraco que parecia ser uma armadilha.")
            print("Havia muitas lanças e espadas dentro do buraco enficandas no chão você foi perfurado por várias e acaba morto naquele buraco.")
            print("Game Over!!!")

    else:
        print("De repente você sente uma caimbra não consegue nadar sente a correnteza mais forte")
        print("e acaba sendo puxado para outra cachoeira bate a cabeça e morre.")
        print("Game Over!!!")

else:
    print("Você segue por um por uma planicie com mato na altura de seu joelho acaba pisando em falso\n e caindo em um buraco batendo sua cabeça no chão.")
    print("Game Over!!!")

