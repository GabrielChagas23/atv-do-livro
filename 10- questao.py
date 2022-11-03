num: float
numPrimo: int
numPar: int


for n in range (1,11):
    print(f'{n}º número')

    num = int(input("Digite um número: "))

if num % 2 == 0 :
    numPar += num
else:
    numPrimo += num


if numPar > 0 and numPrimo > 0:
    print(f'Esse é o resultado da soma dos numeros pares: {numPar}')
    print(f'Esse é o resultado da soma dos numeros primos: {numPrimo}')
elif numPar > 0 and numPrimo == 0:
    print(f'Esse é o resultado da soma dos numeros pares: {numPar}')
    print('Não foram informados números primos')
elif numPar == 0 and numPrimo > 0:
    print('Não foram informados números pares')
    print(f'Esse é o resultado da soma dos numeros primos: {numPrimo}')
else:
    print('Não foram informados números pares')
    print('Não foram informados números primos')