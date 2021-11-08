d = float(input('Depósito inicial:'))
t = float(input('Taxa de juros ao ano:'))
taxa = t / 100
dobro = d * 2
q = 0

while  d < dobro:
    valor = d * taxa
    d += valor
    q += 1
print(f'O valor inicial será dobrando após {q} ano(s)')
