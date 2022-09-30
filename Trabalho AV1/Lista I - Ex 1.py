#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu 
#peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7


altura = float(input('Digite sua altura em metros usando ponto [.]'))
sexo = int(input('1 para homem 2 para mulher'))

if (sexo == 1):
    peso = (72.7*altura) - 58
    print('o peso ideal sera %.2f'%peso)
elif (sexo == 2):
    peso = (62.1*altura) - 44.
    print('o peso ideal sera %.2f'%peso)
else: 
    print('invalido')
