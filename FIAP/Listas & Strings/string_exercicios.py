import os
os.system('cls')


'''
EXERCICIOS
'''

# 1. Utlizando SOMENTE os métodos apresentados nesta apresentação, faça um
# subalgoritmo de nome vogal_maiuscula(string) que passe uma string por parâmetro
# e retorne-a com as vogais conver das em maiúsculas.

# EXEMPLO:

'''

                -> PROGRAMA PRINCIPAL <-
                
                
                texto = “Edson de Oliveira”
                new_texto = vogal_maiuscula(texto) 
                print(new_texto)

                    EdsOn dE OlIvEIrA
'''

# def vogal_maiuscula(texto):
#     vogais = 'aeiou'
    
#     new_texto = ''
    
#     for caractere in texto:
#         if caractere in vogais:
#             new_texto += caractere.upper()
#         else: 
#             new_texto += caractere
#     return new_texto
       
       
       
# texto = 'Vinicius Eira'
# new_texto = vogal_maiuscula(texto)

# print(new_texto)


# -> VInIcIUs EIrA <-

'''

USANDO O METODO REPLACE()


def vogal_maiuscula(texto):
    vogais = 'aeiou'
    
    new_texto = ''
    
    for i in range(len(texto)):
        if texto[i] in vogais:
            new_texto = texto.replace(texto[i], texto.upper())
            
    return new_texto

'''


# SEM USAR FUNCAO

# texto = 'Vinicius Eira'
# vogais = 'aeiou'

# new_texto2 = ''

# for caractere in texto:
#     if caractere in vogais:
#         new_texto2 += caractere.upper()
#     else:
#         new_texto2 += caractere
    

# print(new_texto2)



#___________________________________________

os.system('cls')

'''
2. Dada uma lista e um caractere por parâmetro, faça uma função que retorne em 
uma lista com índices onde os caracteres forma encontrados.
 
 
            
                -> PROGRAMA PRINCIPAL <-
                
                        0123456789012
                Nome = 'Vinicius Eira'
                print(retorna_indices(nome, 'e))
                
                >>[12]
                
                print(retorna_indices(nome, i))
                
                >>[1, 3, 5, 10]
                
                print(retorna_indices(nome, a))
                
                >>[]
            
'''


def retorna_indice(lista: list, caractere: str ) -> list:
    indices = []
    
    for i, elemento in enumerate(lista):
        if elemento == caractere:
            indices.append(i)
            
    return indices


nome = 'Vinicius Eira'

print(retorna_indice(nome, 'i'))




'''
Dada uma lista com notas, faça uma função que retorne outra lista somente com 
as notas maiores ou igual a 6.
'''


#                   -> Programa Principal <-

                    # lista = [5, 6, 0, 8, 2, 4, 9]


                    # lista_aprovados = verifica_aprovados(lista)

                    # print(lista_aprovados)

                    # >> [6, 8, 9]






# def verifica_aprovados(lista):
#     nova_lista = []
#     for i in range(len(lista)):
#         if lista[i] >= 6:
#             nova_lista.append(lista[i])
        
#     return nova_lista




