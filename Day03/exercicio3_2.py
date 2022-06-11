# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("Coloque sua altura em m: "))
weight = float(input("Coloque seu peso em kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
print(bmi)
if bmi < 18.5:
    print("Você está abaixo do peso")
elif bmi >= 18.5 and bmi < 25:
    print("Você está com o peso normal")
elif bmi >= 25 and bmi < 30:
    print("Você está com sobrepeso")
elif bmi >= 30 and bmi < 35:
    print("Você está com obesidade")
else:
    print("Você está com obesidade morbida!!!")





