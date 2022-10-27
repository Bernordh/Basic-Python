num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira um número inteiro: "))

ordem = [num1, num2]
reordem = sorted(ordem)
diferenca = reordem[1] - reordem[0]
start = reordem[1] - diferenca + 1
while(start < reordem[1]):
    print(start)
    start = start + 1