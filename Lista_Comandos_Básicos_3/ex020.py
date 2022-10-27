x = 1
while(x == 1):
    num = float(input("Insira um número: "))
    if num <= 16 and num >= 0:
        if(num == int(num)):
            par = 1
            res = 1
            while(par <= num):
                res = res * par
                par = par + 1
            print(res)
        else:
            print("Digite um número inteiro!") 
    if num == int(num):
        print("Você deseja saber outro fatorial?")
        print("1)Sim")
        print("2)Não")
        v = int(input(""))
        if v == 1:
            x = 1
        else:
            print("Obrigado por usar meu programa!")
            x = 2
    else:
        x = 1