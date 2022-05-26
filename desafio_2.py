vetor = [2, 1, 4, 5, 3]
vetorOrdenado = []
i = 0;
for idx, x in enumerate(vetor):

    for index, x in enumerate(vetor):

   
        if(min(vetor) == x):
            i += index
            del vetor[index]
        
        vetorOrdenado.append(min)

print(i)