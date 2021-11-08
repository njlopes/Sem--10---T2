num = 0
maior = 0
menor = 0
cont = 0
while True:
    n = int(input('Digite um valor:'))
    cont += 1
    if n == 0: break
    if cont == 1:
        maior = menor = n
    else:
        if n>maior:
            maior = n
        if n<menor:
            menor = n


if maior != 0:
    print(f'O maior valor é: {maior:.2f}')

if menor != 0:
    print(f'O menor valor é: {menor:.2f}')
                
