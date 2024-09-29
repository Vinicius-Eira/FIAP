import os
os.system('cls')


'''
Métodos para string
'''


# -> find(substring, inicio, fim) <-

'''

Este método procura um trecho de string em uma outra maior, caso encontre, 
retorna o índice de início da primeira localização, se não encontrar, retorna -1.

'''


#        012345678901234567890123456789012345678901234567890
frase = "Veremos agora os métodos de manipulação de strings."

print(frase. find("agora")) # Pesquisa a palavra 'agora'na frase que começa na posição 8

#  8

print(frase. find("m")) # pesquisa a primeira letra 'm'na frase

# 4

print(frase.find("listas")) # pesquisa uma palavra que não existe na frase

# -1

print(frase. find("m",10,20)) # pesquisa a letra 'm' no intervalo entre 10 e 20

# 17


#_______________________________________________________________________________


# -> join(lista_de_strings) <-

'''
O método join() pega uma lista contendo elementos strings e transforma em 
apenas uma string.

'''

# Em outras palavras, este método junta strings.

nome = ["Edson", "de", "Oliveira"]

print(" ".join(nome)) # Cria uma string com a lista separando por espaço

# Edson de Oliveira

print("-".join(nome)) # Cria uma string com a lista separando com '-'

# Edson-de-Oliveira

print(",".join(nome)) # Cria uma string com a lista separando com ','

# Edson,de,Oliveira


#_______________________________________________________________________________

# -> split(str_separadora) <-

'''
O método join() pega uma lista contendo elementos strings e transforma em 
apenas uma string.

Em outras palavras, este método junta strings. Repare que ela extrai o texto
passado por parâmetro.

'''

nome = "Edson de Oliveira"

print(nome.split()) # Tornou a string em uma lista separada por espaço

# ['Edson', 'de', 'Oliveira']

print(nome.split('e')) # Tornou a string em uma lista separada por 'e'

# ['Edson d', ' Oliv', 'ira']

print (nome.split('de')) # Tornou a string em uma lista separada por 'de'

# ['Edson ', ' Oliveira']

#_______________________________________________________________________________


# -> replace(procura, troca, cont) <-

'''

Este método substitui em uma string uma substrings especificada por outra 'cont'
vezes solicitada.

'''

nome1 = "Edson de Oliveira"

nome.replace('e', 'E') # Troca os 'e' por 'E'
print (nome1)

# Edson dE OlivEira

nome2 = nome.replace('de', 'DE') # Troca o 'de' por 'DE
print (nome2)

# Edson DE Oliveira

nome3 = nome.replace(' ', '_',1)
print(nome3)

# Edson_de Oliveira


#_______________________________________________________________________________


# -> strip() <-

'''

Este método elimina os eventuais espaços que existirem no início e final da string.

'''

texto =" Strip elimina os espaços "

tamanho_texto = len(texto)
print(f"O texto '{texto}' tem o tamanho: {tamanho_texto}.")

# O texto ' Strip elimina os espaços ' tem o tamanho: 26.

texto = texto.strip() # Elimina os espaços antes e depois do texto

tamanho_texto_strip = len(texto)
print(f"O texto '{texto}' tem o tamanho: {tamanho_texto_strip}.")

# O texto 'Strip elimina os espaços' tem o tamanho: 24.