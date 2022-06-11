# 🚨 Don't change the code below 👇
print("Bem vindo a Disk Python Pizzas!")
size = input("Qual o tamanho da PIZZA? P, M, ou G? ")
add_pepperoni = input("Você que calabresa? S ou N ")
extra_cheese = input("Queijo extra? S ou N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

small_pizza = 0
medium_pizza = 0
large_pizza = 0
perp_small = 2
perp_medium = 3
cheese = 1

if size == "P":
    small_pizza = 15
    print(f"Pizza pequena custa R${small_pizza},00 e se quiser acrescentar calabresa são R${perp_small},00 e o queijo extra é R${cheese},00")
    if add_pepperoni == "S":
        small_pizza += perp_small
        print(f"Pizza pequena só com calabreza custa R${small_pizza},00")
    if extra_cheese == "S":
        small_pizza += cheese
        print(f"Pizza pequena com calabreza e queijo custa R${small_pizza},00")

elif size == "M":
    medium_pizza = 20
    print(f"Pizza média custa R${medium_pizza},00 e se quiser acrescentar calabresa são R${perp_medium},00 e o queijo extra é R${cheese},00")
    if add_pepperoni == "S":
        medium_pizza += perp_medium
        print(f"Pizza média só com calabreza custa R${medium_pizza},00")
    if extra_cheese == "S":
        medium_pizza += cheese
        print(f"Pizza média com calabreza e queijo custa R${medium_pizza},00")

else:
    large_pizza = 25
    print(f"Pizza grande custa R${large_pizza},00 e se quiser acrescentar calabresa são R${perp_medium},00 e o queijo extra é R${cheese},00")
    if add_pepperoni == "S":
        large_pizza += perp_medium
        print(f"Pizza grande só com calabreza custa R${large_pizza},00")
    if extra_cheese == "S":
        large_pizza += cheese
        print(f"Pizza grande com calabreza e queijo custa R${large_pizza},00")

    
            


