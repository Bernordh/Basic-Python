tabuada = int(input("Insira o número da tabuada: "))
ini = int(input("Começar tabuada pelo número: "))
fin = int(input("Finalizar no número: "))
fin += 1

for x in range(ini, fin, 1):
    r = tabuada * x
    print(f"{tabuada} * {x} = {r}")