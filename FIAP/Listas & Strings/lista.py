import os
os.system('cls')


# -> Métodos para lista <-


# -> list() ou [] | Cria uma lista vazia


# lista1 = list() 
# print(lista1)

#  >> []


# lista2 = []
# print(lista2)

#  >> [] | Criou a lista1 e lista2 como vazias
 
#__________________________________________________

#  -> append() |  Adiciona um dado no final da lista


# lista = []
# lista.append(22)
# lista.append("Lógica")
# print(lista)

#  >> [22, 'Lógica'] | #  Adicionou os elementos 22 e “lógica”



#__________________________________________________

# -> insert(posição, elemento) |  Insere um dado numa posição da lista


# lista = [22, "Lógica"]

#  >> [22, 'Lógica']


# lista.insert(1, 57.7)

#  >> [22, 57.7, 'Lógica'] | #  Inseriu o elemento 57.7 na posição cujo índice é 1



#__________________________________________________

# -> pop(posição) | Remove o elemento com  a posição informada. Se não for
# informada a posição, remove o ultimo elemento


# lista = [22, 57.7, "Lógica"]
# lista.pop(0)

# >> [57.7, 'Lógica']


#  lista.pop()

#  >> [57.7] | #  Remove o elemento com o índice 0 (zero) depois remove o
               #  último elemento



#__________________________________________________

# -> remove(elemento) |  Remove o elemento pelo conteúdo


# lista = [22, 57.7, "Lógica"]
# lista.remove(57.7)

#  >> [22, “Lógica”] | Remove o elemento com o conteúdo 57.7 da lista


#__________________________________________________

# -> index(elemento) |  Retorna o índice do elemento passado por parâmetro


# lista = [22, 57.7, "Lógica"]
# indice = lista.index("Lógica")
# print(f"Índice = {indice}")

# >> Índice = 2 | Retorna o índice 2 do elemento “Lógica” passado por parâmetro. 
                # Caso o elemento não exista, haverá um erro de compilação.


#__________________________________________________

#  -> count(elemento) | Conta quantos elementos específicos existem na lista


# lista = [22, 22, 57.7, "Lógica"]
# qtd = lista.count(22)
# print(f"Quantidade = {qtd}")
 
#  >> Quantidade = 2 | Retorna 2 porque existem 2 elementos 22 na lista

#__________________________________________________

#  ->  len(lista) |  Conta quantos elementos existem na lista


# lista = [22, 22, 57.7, "Lógica"]
# qtd_elementos = len(lista)
# print(f"Quantidade = {qtd_elementos}")

#  >> Quantidade = 4 | Retorna 2 porque existem 2 elementos 22 na lista

#__________________________________________________

#  -> sum(lista) |  Soma os elementos da lista caso todos sejam numéricos


# lista = [22, 22, 57.7, "Lógica"]
# qtd = lista.count(22)
# print(f"Quantidade = {qtd}")

# >> Quantidade = 2 |  Retorna 2 porque existem 2 elementos 22 na lista

#__________________________________________________

# -> extend(lista) | Adiciona ao final da lista outra lista


# lista1 = [1, 2, 3]
#  print(f"Lista1 = {lista1}")

#  >> Lista1 = [1, 2, 3] 


# lista2 = [4, 5, 6]
# print(f"Lista2 = {lista2}")

# >> Lista2 = [4, 5, 6] 


# lista2.extend(lista1)

# >> Lista2 = [4, 5, 6, 1, 2, 3]

# print(f"Lista2 = {lista2}") | Criou a lista1 e lista2 e adicionou no final 
                                # da lista2 a lista1
                                
#__________________________________________________

# -> copy() | Copia uma lista em outra


# lista1 = [1, 2, 3]
# lista2 = lista1.copy()
# print(f"Lista1 = {lista1}")

# >> Lista1 = [1, 2, 3]

# print(f"Lista2 = {lista2}")

# >> Lista2 = [1, 2, 3]

#__________________________________________________

# ->  sort(reverse) | Ordena os elementos da lista. O parâmetro reverse=True 
                    # permite que seja ordenada em ordem decrescente
              
                    

# lista = [19, 4, 25, 33, -5]
#  lista.sort()
#  print(lista)

#  >> [-5, 4, 19, 25, 33]


#  lista.sort(reverse=True)
#  print(lista)
#  >> [33, 25, 19, 4, -5] | Ordenou a lista em ordem crescente, depois em ordem 
                          # decrescente

#__________________________________________________

# ->  reverse() | Inverte a ordem dos elementos dentro da lista


#  lista = [19, 4, 25, 33, -5]
#  lista.reverse()
#  print(lista)

#  >> [-5, 33, 25, 4, 19] | Inverteu os elementos da lista, colocando o último
                        # elemento como primeiro e primeiro como último e assim 
                        # sucessivamente.

#__________________________________________________

# -> clear() | Apaga todos os elementos da lista


#  lista = [19, 4, 25, 33, -5]
#  lista.clear()
#  print(lista)

#  >> [] |  Removeu todos os elementos da lista, mas ela continua existindo

#__________________________________________________

# -> del(lista) | Exclui (desaloca) a lista da memória

# lista = [19, 4, 25, 33, -5]
#  del(lista)
 
#  >> a lista não existe mais |  Excluiu a lista da memória com todos os seus 
                                # elementos
                                
 #__________________________________________________


# -> Operador de iden dade ‘in’ <-


# O operador in retorna True caso o elemento esteja dentro de uma lista, caso
# contrário retorna False.

num = 4

if num in [1, 2, 3, 4, 5]:
    print(f'o número {num} está na lista.')
else:
    print(f'O número {num} não está na lista.')


# OUTRO EXEMPLO UTILIZANDO STRING


nome = 'Felipe Melo de Franca'

if 'Eira' not in nome:
    print(f"'Eira' NÂO está cotindo no {nome}")
else:
    print(f"'de' ESTA contido no {nome}")