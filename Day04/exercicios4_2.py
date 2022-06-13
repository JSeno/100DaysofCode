from random import random


import random

# Split string method

names_string = input("Me de alguns nomes separados por uma virgula: ")
names = names_string.split(",")


# num_item = len(names)
# random_choice = random.randint(0, num_item -1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " vai pagar o almoço hoje!")

#print(random_choice)
# print(len(names))
# print(names)