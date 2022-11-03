import os

idade = int
op = int
regular = int
bom = int
otimo = int
mediaIdadeOtimo = float
somaIdadeOtimo = float
perBom = float

idade = 0
op = 0
regular = 0
bom = 0
otimo = 0
mediaIdadeOtimo = 0
somaIdadeOtimo = 0
perBom = 0

for n in range(1, 4):
    idade = int(input("Informe a sua idade: "))
    op = float(input("\nÓtimo - 3\nBom - 2\nRegular - 1: Informe a sua opinião: "))
    
    os.system("cls")
    somaIdadeOtimo += idade
    
    if op == 3:
        otimo += 1
        mediaIdadeOtimo += idade
    if op == 1:
        regular += 1
    if op == 2:
        bom += 1
        
mediaIdadeOtimo = somaIdadeOtimo / otimo
perBom = bom / 15 * 100

print("A média das idades das pessoas que responderam Ótimo:",  mediaIdadeOtimo)
print("A quantidade de pessoas que responderam Regular: ", regular )
print("A percentagem de pessoas que responderam bom: ", perBom)
    
    
    
