# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number2 = int(input("Which the second number do you want to check? "))
res = number / number2
if res % 2 == 0:
    print(f"The result is even and the result is {res}")
else:
    print(f"The result is odd and the result is {res}")
