tamanho = int(input('qual o tamanho em MB do arquivo desejado '))
velocidade = int(input('qual a velocidade em Mbps da sua internet '))

tempo = ((tamanho*8)/velocidade)/60

print('Aproximadamente %.2f minutos para baixar' %tempo)
