from unittest import result

from zmq import PUSH


vetor = [31,-41,59,26,-53,58,97,-93,-23,84]
result=[]
for index,x in enumerate(vetor):
    
   
    if index== (len(vetor) - 1):
        result.append(x + vetor[index - 1])
    else:
        result.append(x + vetor[index + 1]) 

    print(result[index])


max(result)
print(f"maior valor {max(result)}")