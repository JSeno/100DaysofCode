import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("O que você escolhe? 0-pedra, 1-papel, 2-tesoura:\n "))

if user_choice >= 3 or user_choice < 0:
    print("Você digitou um número inválido")
else:
    print(game_images[user_choice])

    cpu_choice = random.randint(0,2)
    print("CPU escolheu:")
    print(game_images[cpu_choice])


    if user_choice == 0 and cpu_choice ==2:
        print("P1 Venceu!!!")
    elif cpu_choice == 0 and user_choice == 2:
        print("CPU Venceu!!!")
    elif cpu_choice > user_choice:
        print("CPU Venceu!!!")
    elif user_choice > cpu_choice:
        print("P1 Venceu!!!")
    elif cpu_choice == user_choice:
        print("Empatou!!!")
