#4. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu 
#respectivo índice. Imprima a idade e a altura na ordem inversa a ordem lida.



infosLista = []

indice_visual = 0
for x in range(5):
    infosLista.append(input(f'Digite a altura do indice {indice_visual} '))
    print(f'Digite a idade do indice {indice_visual} ', end=" ")
    infosLista.append(input())
    indice_visual += 1
print(infosLista,' ')

infosLista2 = []

y = 1
z = 0
for x in range(5):
    infosLista2.append(infosLista[y])
    y += 2
    infosLista2.append(infosLista[z])
    z += 2
print(infosLista2)    
