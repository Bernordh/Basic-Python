nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira o valor do seu salário: "))
sexo = input("Insira seu sexo (f ou m): ")
estcivil = input("Insira seu estado civil (s, c, v, d): ")

while(len(nome) < 3):
    nome = input("Nome muito pequeno, insira um nome válido: ")

while(idade < 0 or idade > 150):
    idade = int(input("Idade inválida, insira um valor válido: "))

while(salario < 0):
    salario = float(input("Sálario inválido, insira um valor válido"))

while(sexo != "f" and sexo != "m"):
    sexo = input("Sexo inválido, insira um sexo válido: ")

while(estcivil != 's' and estcivil != 'c' and estcivil != 'v' and estcivil != 'd'):
    estcivil = input("Estado civil inválido, insira um valor válido")

print(f"Seu nome é {nome}")
print(f"Você tem {idade} anos")
print(f"Você ganha {salario:.2f} reais")
print(f"Você é do sexo {sexo}")
print(f"Seu estado civil no momento é {estcivil}")