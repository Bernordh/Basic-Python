num = int(input("Insira o tamanho da lista: "))
if num <= 100 and num >= 0:
    lista = []
    x = 0
    soma = 0
    while(x < num):
        lista.append(int(input(f"Digite o número {x} da sequência: ")))
        x += 1
    rlista = sorted(lista)

    for i in range(num):
        soma = soma + lista[i]

    print(f"O menor valor da lista é: {rlista[0]}")
    print(f"O maior valor da lista é: {rlista[x - 1]}")
    print(f"A soma dos valores é {soma}")
else:
    print("Valor inválido, tente novamente!")