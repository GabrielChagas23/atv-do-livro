from re import S


sexo = str
resposta = str
totalSim = int
totalNao = int
mulheresSim = int
homensNao = int
homensSim = int
homensTotal = int
perHomens = float

sexo = ""
resposta = ""
totalSim = 0
totalNao = 0
mulheresSim = 0
homensNao = 0
homensSim = 0
homensTotal = 0
perHomens = 0

for n in range(1, 4):
    sexo = str(input("Informe seu sexo (F - Feminino ou M - Masculino): "))
    resposta = str(input("Qual a sua resposta (S - Sim ou N - Não): "))
    
    if resposta == "S":
        totalSim += 1
        if sexo == "F":
            mulheresSim += 1
        else:
            homensSim += 1
    
    if resposta == "N":
        totalNao += 1
        if sexo == "M":
            homensNao += 1
            
homensTotal = homensNao + homensSim
perHomens = homensNao / homensTotal * 100

print("O número de pessoas que responderam sim: ", totalSim)
print("O número de pessoas que responderam não: ", totalNao)
print("O número de mulheres que responderam sim: ", mulheresSim)
print("A percentagem de homens que responderam não: ", perHomens)