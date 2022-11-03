idade = int
peso = float

mediaPesosFaixa1a10 = float
mediaPesosFaixa11a20 = float
mediaPesosFaixa21a30 = float
mediaPesosFaixa31ACima = float

somaPesosFaixa1a10 = float
somaPesosFaixa11a20 = float
somaPesosFaixa21a30 = float
somaPesosFaixa31ACima = float

qtdPesosFaixa1a10 = float
qtdPesosFaixa11a20 = float
qtdPesosFaixa21a30 = float
qtdPesosFaixa31ACima = float

mediaPesosFaixa1a10 = 0
mediaPesosFaixa11a20 = 0
mediaPesosFaixa21a30 = 0
mediaPesosFaixa31ACima = 0

somaPesosFaixa1a10 = 0
somaPesosFaixa11a20 = 0
somaPesosFaixa21a30 = 0
somaPesosFaixa31ACima = 0


qtdPesosFaixa1a10 = 0
qtdPesosFaixa11a20 = 0
qtdPesosFaixa21a30 = 0
qtdPesosFaixa31ACima = 0

for n in range(1,4):
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    
    if idade >= 1 and idade <= 10:
        somaPesosFaixa1a10 += peso
        qtdPesosFaixa1a10 += 1
    if idade >= 11 and idade <= 20:
        somaPesosFaixa11a20 += peso
        qtdPesosFaixa11a20 += 1
    if idade >= 21 and idade <= 30:
        somaPesosFaixa21a30 += peso
        qtdPesosFaixa21a30 += 1
    if idade >= 31:
        somaPesosFaixa31ACima += peso
        qtdPesosFaixa31ACima += 1
    
    if qtdPesosFaixa1a10 > 0:
        mediaPesosFaixa1a10 = somaPesosFaixa1a10 / qtdPesosFaixa1a10
        print("A média das pessoas entre a faixa de 1 a 10 anos", mediaPesosFaixa1a10)
    else:
        print("Não houve idade entre a faixa etária de 1 a 10 anos!: ")
    if qtdPesosFaixa11a20 > 0:
        mediaPesosFaixa11a20 = somaPesosFaixa11a20 / qtdPesosFaixa11a20
        print("A media das pessoas entre a faixa de 11 a 20 anos", mediaPesosFaixa11a20)
    else:
        print("Não houve idade entre a faixa etária de 11 a 20 anos!")
    if qtdPesosFaixa21a30 > 0:
        mediaPesosFaixa21a30 = somaPesosFaixa21a30 / qtdPesosFaixa21a30
        print("A média das pessoas entre a faixa de 21 a 30 anos", mediaPesosFaixa21a30)
    else:
        print("Não houve idade entre a faixa etária de 21 a 30 anos!")
    if qtdPesosFaixa31ACima > 0:
        mediaPesosFaixa31ACima = somaPesosFaixa31ACima / qtdPesosFaixa31ACima
        print("A média das pessoas com 30 anos ou acima", mediaPesosFaixa31ACima)
    else:
        print("Não houve idades na faixa acima de 31 anos!")
        


