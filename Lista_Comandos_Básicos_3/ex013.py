base = int(input("Insira a base: "))
exp = int(input("Insira o expoente: "))
x = 1
r = 1
while(x <= exp):
    r = r * base
    x = x + 1
print(r)