import os
c: str
compra: float; cv: float; co:float; ct: float

compra = 0
cv = 0
cp = 0

for n in range (1, 3):
    os.system("cls")
    print(f'dados da {n}ª venda ')
    c = input (f'Digite o código da compra (V - à vista ou P - à prazo): ').upper()
    if c == "V":
        compra = float(input("Digite o valor da compra: R$ "))
        cv = cv + compra
    elif c =="P":
        compra = float(input("Digite o valor da compra: R$ "))
        cp = cp + compra
    

print(f"o valor total à vista: R${cv:.2f}")
print(f"o valor total à prazo: R${cp:.2f}")
print(f"O valor total das compras: R${cp + cv:.2f}")
print(f"O valor da primeia prestação das compras a prazo juntas: R${cp/3:.2f}")