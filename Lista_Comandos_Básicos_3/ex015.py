n = int(input("Insira até qual termo voçê quer: "))
x = 0
ini = 0
fin = 1
while(x <= n):
    termo = ini + fin
    ini = fin
    fin = termo
    x = x + 1
    print(f"{termo}")