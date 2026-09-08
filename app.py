# programa desconto progressivo 
#valor da compra
#descontos:
#    se o valor total da compra for menor do que R$ 200,00, o cliente recebe um desconto de 5%.
#    Se o valor total da compra for maior ou igual a R$ 200,00 e menor que R$ 300,00, o cliente recebe um desconto de 10%.
#    Se o valor total da compra for maior ou igual a R$ 300,00, o cliente recebe um desconto de 15%.
#  


print('---> Programa Desconto Progressivo <---\n')
valorTotal = float(input('Insira o valor da sua compra em R$: '))

if valorTotal < 200:
    #desconto de cinco %
    descontocinco = (valorTotal*0.05)
    print(descontocinco)
    
elif valorTotal >=200 and valorTotal<300:
    #desconto de dez%
    descontodez = (valorTotal*0.10)
    print(descontodez)
    
elif valorTotal>=300:
    #desconto de 15%
    descontoquinze = (valorTotal*0.15)
    print(descontoquinze)