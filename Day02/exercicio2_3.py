# Calculo de até os 90 anos quanto tempo você tem de vida, com anos, dias, meses, semanas.
age = input("What is your current age? ")

# dias_ano = 365
# semanas_ano = 52
# meses_ano = 12

anos_ate_90 = tempo = 90 - int(age)
total_dias = tempo * 365
total_semanas = tempo * 52
total_meses = tempo * 12

print(f"Até os 90 anos você tem {anos_ate_90} anos, {total_dias} dias, {total_semanas} semanas e o total de {total_meses} meses para viver")
