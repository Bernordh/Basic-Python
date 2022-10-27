pais_a = 80000
pais_b = 200000
anos = 0
while(pais_a <= pais_b):
    pais_a = pais_a * 1.03
    pais_b = pais_b * 1.015
    anos = anos + 1
print(f"O país A tem {pais_a:.0f} habitantes")
print(f"O país B tem {pais_b:.0f} habitantes")
print(f"Para chegar até esses valores foram gastos {anos} anos")