vetor1 = []
vetor2 = []
vetor3 = []

for x in range(10):
    vetor1.insert(x,int(input('digite um elemento (vetor 1) ')))
print('\nlimpa xx limpa xx limpa xx limpa\n')
for x in range(10):
    vetor2.insert(x,int(input('digite um elemento (vetor 2) ')))
    
aux = 0
for x in range(10):
    vetor3.extend([vetor1[aux]])
    vetor3.extend([vetor2[aux]])
    aux = aux + 1

print(vetor3)
