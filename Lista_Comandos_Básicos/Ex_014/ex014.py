peso_p = float(input("Qual o peso do peixe: "))
if peso_p > 50:
    multa = 4 * (peso_p - 50)
    print(f"Você deverá pagar {round(multa, 2)} R$ de multa")
else:
    print("Você não precisa pagar multa") 