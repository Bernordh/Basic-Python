tempo = 24720
tempo1 = 1980
tempo2 = 2592
tempof = tempo + tempo1 + tempo2
tnorm = (tempof / 60) / 60
thoras = round(((tempof / 60) / 60) - 0.5)
tmin = tnorm - thoras
min = round(tmin * 60)
print(f"Você vai chagar em casa as {thoras} horas e {min} minutos")