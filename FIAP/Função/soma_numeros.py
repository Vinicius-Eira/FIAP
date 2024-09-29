import os

def soma_numeros(*args): #-> args 
    soma = 0 
    for i in range(0, len(args), 1):
        soma += args[i]
    return soma


os.system('cls')

print(soma_numeros(56, 77, 45, 68, 8 ,36))