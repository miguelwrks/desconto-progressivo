# agr, criar uma variavel para no final, subtrair o valor da compra pelo desconto e exibir o valor final ( mais o desconto) e testar o else no lugar do elif final

print('---> Programa Desconto Progressivo <---\n')
valorTotal = float(input('Insira o valor da sua compra em R$: '))

if valorTotal < 200:
    #desconto de cinco %
    descontocinco = (valorTotal*0.05)
    finalcinco = valorTotal - descontocinco
    print(finalcinco)
    
elif valorTotal >=200 and valorTotal<300:
    #desconto de dez%
    descontodez = (valorTotal*0.10)
    finaldez = valorTotal - descontodez
    print(finaldez)
    
elif valorTotal>=300:
    #desconto de 15%
    descontoquinze = (valorTotal*0.15)
    finalquinze = valorTotal - descontoquinze
    print(finalquinze)