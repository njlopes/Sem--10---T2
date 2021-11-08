num = 0
s = 0
cont = 0
m = 0
while True:
    n = int(input('Digite um valor:'))
    if n != 0:
        s += n
        cont += 1
        m = s / cont
    if n == 0: break


if m != 0:
    print (f'A média aritmética de todos os números lidos é igual a: {m:.2f}')
