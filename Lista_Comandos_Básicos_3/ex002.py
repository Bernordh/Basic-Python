nome = input("Insira o nome de usuário: ")
senha = input("Insira uma senha: ")
while(nome == senha):
    print("Valores iguais, insira novamente!")
    nome = input("Insira o nome de usuário: ")
    senha = input("Insira uma senha: ")
print("Cadastro Realizado")