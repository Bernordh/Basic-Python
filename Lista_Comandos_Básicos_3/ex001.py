from xml.dom.minidom import TypeInfo


nota = 11
while(nota < 0 or nota > 10):
    nota = float(input("Insira sua nota: "))
print(f"Sua nota é {nota:.1f}")