vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = ['a','b','c','d','e','f','g','h','i','j']
vetor3 = []
#for x in range(10):
    #vetor1.insert(x,int(input('digite um numero ')))
#for x in range(19):
    #vetor3.insert(x,0)
aux = 0
for x in range(5):
    vetor3.extend([vetor1[aux]])
    vetor2.extend([vetor2[aux]])
    aux = aux + 1

   
    
   
    
print(vetor3)
