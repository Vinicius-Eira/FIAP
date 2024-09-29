'''
EXERCICIOS
'''


#   1. Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista 
#   passada por parâmetro.


# ---------------- SUBALGORITMOS
def preenche_lista(lista) -> None: # l: parâmetro -> local
    while True:
        elem = input("Elemento: ")
        if elem != '.':
            lista.append(elem)
        else:
            break

def exibe_lista(lista) -> None:
    for i in range (len(lista)):
        print(f"{i}-{lista[i]} | ", end='')

# ---------------- PROGRAMA PRINCIPAL
import os
os.system("cls")
lista = list() # lista -> global

preenche_lista(lista)


exibe_lista(lista)
