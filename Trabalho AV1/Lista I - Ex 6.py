#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de 
#um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
#usando este link (em minutos)


tamanho = int(input('qual o tamanho em MB do arquivo desejado '))
velocidade = int(input('qual a velocidade em Mbps da sua internet '))

tempo = ((tamanho*8)/velocidade)/60

print('Aproximadamente %.2f minutos para baixar' %tempo)
