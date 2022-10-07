altura = float(input("Insira a sua altura (em centimetros): "))
genero = input("Você é Homem ou Mulher? ")
print(" ")
if genero == "Mulher" or genero == "mulher":
    peso_ideal = (62.1 * (altura / 100)) - 44.7
    print(f"Seu peso ideal é {round(peso_ideal, 2)}kg")

elif genero == "Homem" or genero == "homem":
    peso_ideal = (72.7 * (altura / 100)) - 58
    print(f"Seu peso ideal é {round(peso_ideal, 2)}kg")