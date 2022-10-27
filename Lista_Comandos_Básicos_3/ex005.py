from distutils.command.install_scripts import install_scripts


pais_a = int(input("Insira o o número de habitantes de algum país: "))
pais_b = int(input("Insira o o número de habitantes de algum país: "))
taxa1 = float(input("Insira a taxa de crescimento do primeiro país. (Ex: 1.5 ou 3): "))
taxa2 = float(input("Insira a taca de crescimento do segundo país. (Ex: 1.5 ou 3): "))
anos = 0
taxar_1 = taxa1 / 100 + 1
taxar_2 = taxa2 / 100 + 1

if pais_b > pais_a:

    while(pais_a <= pais_b):

        pais_a = pais_a * taxar_1
        pais_b = pais_b * taxar_2
        anos = anos + 1
    print(f"O país A tem {pais_a:.0f} habitantes")
    print(f"O país B tem {pais_b:.0f} habitantes")
    print(f"Para chegar até esses valores foram gastos {anos} anos")

else:
    print("Insira o pais com menor número de habitantes primeiro!")
    