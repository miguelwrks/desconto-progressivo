
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print('---> Programa Desconto Progressivo <---\n')
valorTotal = float(input('Insira o valor da sua compra em R$: ')) #float por estar trabalhando com numeros que podem ser deciamais e com decimais (para fazer a porcentagem)

if valorTotal < 200:
    #desconto de 5%
    descontocinco = (valorTotal*0.05)
    #descontocinco = acha o valor do desconto fazendo a porcentagem (5% do valor total) para depois esse desconto ser subtraído no finalcinco (variavel que vai armazenar o valor com desconto já)
    finalcinco = valorTotal - descontocinco
    print(f'Sua compra deu o total de: R${finalcinco} (com desconto).\nO desconto foi de {descontocinco}(5%) e o valor original da sua compra era de: R${valorTotal}')
    
elif valorTotal >=200 and valorTotal<300:
    #desconto de 10%
    descontodez = (valorTotal*0.10)
        #descontodez = acha o valor do desconto fazendo a porcentagem (10% do valor total) para depois esse desconto ser subtraído no finaldez (variavel que vai armazenar o valor com desconto já)
    finaldez = valorTotal - descontodez
    print(f'Sua compra deu o total de: R${finaldez} (com desconto).\nO desconto foi de {descontodez}(10%) e o valor original da sua compra era de: R${valorTotal}')
    
#elif valorTotal>=300: (outra maneira de estrutura de decisão pro final)
else:   
    #desconto de 15%
    descontoquinze = (valorTotal*0.15)
        #descontoquinze = acha o valor do desconto fazendo a porcentagem (15% do valor total) para depois esse desconto ser subtraído no finalquinze (variavel que vai armazenar o valor com desconto já)
    finalquinze = valorTotal - descontoquinze
    print(f'Sua compra deu o total de: R${finalquinze} (com desconto).\nO desconto foi de {descontoquinze}(15%) e o valor original da sua compra era de: R${valorTotal}')
    

print("\n\nPrograma desenvolvido por: Miguel Gonçalves.")