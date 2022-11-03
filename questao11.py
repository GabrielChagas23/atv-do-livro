valorCarro = float; PrecoAVista = float; TaxaDeJuros = float

valorCarro = 0.0
PrecoAVista = 0.0
TaxaDeJuros = 0.03

valorCarro = float(input("Informe o valor do carro: "))

PrecoAVista = valorCarro - (valorCarro*0.20)
print("Quantidade de parcelas - % de juros")
for n in range(6, 66, 6):
    print(f"{n} - {valorCarro + valorCarro * TaxaDeJuros}")
    TaxaDeJuros = TaxaDeJuros + 0.03
