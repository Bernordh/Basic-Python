v_hora = float(input("Quanto você quer ganhar por hora: "))
horas = float(input("Quantas horas você quer trabalhar no mês: "))

s_total = v_hora * horas
imposto_r = s_total * 0.11
inss = s_total * 0.08
sind = s_total * 0.05
s_liquido = s_total - imposto_r - inss - sind
print(" ")
print(f"Salário Bruto: {s_total}")
print(f"Imposto de renda: {imposto_r}")
print(f"INSS: {inss}")
print(f"Sindicato: {sind}")
print(f"Salário Liquido: {s_liquido}")