x = 1
imp = 0
par = 0
while(x <= 10):
    num = int(input("Insira um número inteiro: "))
    div = num%2
    if(div > 0):
        imp = imp + 1
    else:
        par = par + 1
    x = x + 1
print(f"Você digitou {imp} números impares")
print(f"Você digitou {par} números pares")