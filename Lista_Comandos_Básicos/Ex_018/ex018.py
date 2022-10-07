tamanho = float(input("Insira o tamanho do arquivo em Mb: "))
vel = float(input("Insira a velocidade da sua internet em Mbps: "))

tempo = (tamanho / vel) / 60
print(f"O seu download vai levar {round(tempo, 2)} minutos")