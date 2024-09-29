import os
os.system('cls')

# Dada uma lista preenchida por parâmetro, retornar True caso todos os elementos sejam int, caso
# contrário, retornar False.
# ---------- SUBALGORTIMOS

# ***** inicio da função principal
def eh_lista_int(lista) -> bool: 

    # ***** inicio do procedimento encadeado
    def transforma_str(lista) -> None: 
        for i in range(len(lista)):
            lista[i] = str(lista[i])
    # ***** final do procedimento encadeado

    transforma_str(lista) # chamada do precedimento encadeado
    lista_int = True
    for i in range(len(lista)):
        if not lista[i].isnumeric(): 
            lista_int = False
            break
    
    return lista_int
# ***** Final da função principal

# ---------- PROGRAMA PRINCIPAL

"""
mano, na boa cara! ja te falei mil vezes que o metodo isnumeric pega
como referencia um dado string para verificar se o seu conteudo é numerico
pela 15.o vez, voce esta comparando um dado nao string com esta funcao.
só poderia dar erro, né cara!
"""

lista = ["45", "34", "23", "Edson", "55"]
# Teste 1
import os
os.system("Clear")

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