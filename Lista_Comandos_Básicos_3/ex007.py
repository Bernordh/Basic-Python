num1 = float(input("Insira um número: "))
num2 = float(input("Insira um número: "))
num3 = float(input("Insira um número: "))
num4 = float(input("Insira um número: "))
num5 = float(input("Insira um número: "))

ordem = [num1, num2, num3, num4, num5]
newor = sorted(ordem)
print(f"O maior número é o {newor[4]}")