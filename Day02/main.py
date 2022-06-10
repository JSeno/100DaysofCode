# Dia 02 Calculadora que calcular valores de gorjeta e total a pagar.

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tipo would you tike to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill * (1 + tip / 100)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person shouyld pay: ${final_amount}")



