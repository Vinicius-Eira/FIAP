import os
os.system('cls')

lista = [5, 8, 4, "Edson", 12, 44]

# inicio da função principal
def verifica_numeros_inteiros(lista):
    for item in lista:
     if not (str(item).isdigit() or str(item).isnumeric()):
      return False
    return True

if verifica_numeros_inteiros(lista):
    print('Todos os elementos contidos no laço são inteiros')
else:
    print('Nem todos os elementos contidos no laço são inteiros')
    

print(verifica_numeros_inteiros(lista))

lista = [5, 8, 4, 12, 44]

if verifica_numeros_inteiros(lista):
    print('Todos os elementos contidos no laço são inteiros')
else:
    print('Nem todos os elementos contidos no laço são inteiros')
    
print(verifica_numeros_inteiros(lista))


# -> OUTRA FORMA DE SER FEITO


# inicio da função principal
def eh_lista_int(l: list) -> bool: 

    # inicio do procedimento encadeado
    def transforma_str(l: list) -> None: 
        for i in range(len(l)):
            l[i] = str(l[i])
    # final do procedimento encadeado

    transforma_str(l) # chamada do precedimento encadeado
    lista_int = True
    for i in range(len(l)):
        if not l[i].isnumeric(): 
            lista_int = False
            break
    
    return lista_int


# -> OUTRA FORMA DE SER FEITO SEM USAR FUNÇOES


# Teste 1
os.system("cls")

lista = [45, 34, -23, 12, 55]
if eh_lista_int(lista):
    print("Lista totalmente de inteiros")
else:
    print("Lista não totalmente de inteiros")

# Teste 2
lista = [45, 29, "aniversario", "Edson", 55]
if eh_lista_int(lista):
    print("Lista totalmente de inteiros")
else:
    print("Lista não totalmente de inteiros")






