import os

idade = int
somaIdade = int
pesoSuperior90alturaInferior150 = int
idade10e30altura190 = int
peso = float
altura = float
mediaIdade = float

pesoSuperior90alturaInferior150 = 0
somaIdade = 0
idade10e30altura190 = 0

for n in range(1, 11):
    print(f"Dados para {n}ª pessoas: ")
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))
    
    os.system("cls")
    somaIdade += idade
    
    if peso > 90 and altura < 1.50:
        pesoSuperior90alturaInferior150 += 1
    if (idade >= 10 and idade <= 30) and altura > 1.90:
        idade10e30altura190 += 1
        
mediaIdade = somaIdade / 10

print(f"Média das idades das 10 pessoas: {mediaIdade:.2f}")
print(f"Quantidade de pessoas com peso superior a 90kg e altura inferior a 1.50 metros: {pesoSuperior90alturaInferior150}m.")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90 m: {idade10e30altura190/10*100:.1f}%.")