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

if area > 21.6:
    t = area / 21.6
    if t == round(t):
        p = t * 25
        print(f"Você vai precisar comprar {t} galões e isso vai te custar {p} reais")
    else:
        t = round(t + 0.5)
        p = t * 25
        print(f"Você vai precisar comprar {t} galões e isso vai te custar {p} reais")

if area > 108:
    l = area / 108
    l = round(l - 0.5)
    p1 = l * 80
    subarea = area - (l * 108)
    g = subarea / 21.6
    g = round(g + 0.5)
    p2 = g * 25
    p3 = p1 + p2
    print(f"Se você quiser economizar, você vai pode comprar {l} latas e {g} galões, oque vai te custar {p3} reais")

else:
    print("Você vai precisar de uma lata de tinta, e isso vai te custar 25 reais")
