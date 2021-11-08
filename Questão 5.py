salário = float(input('Digite o valor do salário:'))
divida = float(input('Digite o valor da dívida:'))

aumento = 5 / 100
divi = 15 /100
inicio = 0
ano = 2016
mes = 10
    
while divida < salário:
    mes+=1
    div_atual = divida + divida * divi
    divida = div_atual
    if mes == 12:
        ano+=1
        mes = inicio
    if mes == 3:
            novo_salário  = salário * aumento
            salário += novo_salário
    if divida > salário: break
       

print(f'O valor da dívida será superior ao salário em: {mes}/{ano}')

    
    

