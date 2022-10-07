area = float(input("Quantos metros quadrados serão pintados: "))
if area > 108:
    t = area / 108
    if t == round(t):
        p = t * 80
        print(f"Você vai precisar comprar {t} latas e isso vai te custar {p} reais")
    else:
        t = round(t + 0.5)
        p = t * 80
        print(f"Você vai precisar comprar {t} latas e isso vai te custar {p} reais")

else:
    print("Você vai precisar de uma lata de tinta, e isso vai te custar 80 reais")

if area > 21.6:
    t = area / 21.6
    if t == round(t):
        p = t * 25
        print(f"Você vai precisar comprar {t} latas e isso vai te custar {p} reais")
    else:
        t = round(t + 0.5)
        p = t * 25
        print(f"Você vai precisar comprar {t} latas e isso vai te custar {p} reais")

else:
    print("Você vai precisar de uma lata de tinta, e isso vai te custar 25 reais")