termo = 0
ini = 0
fin = 1
while(termo < 500):
    termo = ini + fin
    ini = fin
    fin = termo
    print(f"{termo}")