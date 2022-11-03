import os
idade: int; idade50: int; alturaentre10e20: int; peso40: int; altura: float; peso: float; somaAltura: float

idade50 = 0
altura = 0
somaAltura = 0
alturaentre10e20 = 0
peso40 = 0

for n in range(1, 6):
    os.system("cls")
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))
    
    if idade > 50:
        idade50 += 1
    if idade >= 10 and idade <=20:
        somaAltura += altura
        alturaentre10e20 += 1
    if peso < 40:
        peso40 += 1

print(f"Existem {idade50} pessoas com idade superior a 50 anos. ")
    