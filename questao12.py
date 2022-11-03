num = int
primo = int

for n in range(1, num + 1):
    if num % n == 0:
        primo +=1
if primo == 2:
    print(f"O Nº {num} é primo!")
else:
    print("Não é primo.")
        
