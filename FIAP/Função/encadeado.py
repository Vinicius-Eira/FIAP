# DEFINIÇÃO DOS SUBALGORITMOS

# Escreva um programa Python que calcule a média de duas notas inseridas 
# pelo usuário. Cada nota deve ser um número entre 0 e 10. Se uma das notas
# inseridas não estiver dentro deste intervalo, o programa deve imprimir 
# "Nota(s) inválida(s)!


# Instruções:

# Defina uma função chamada media2notas que aceite dois parâmetros, n1 e n2,
# representando as duas notas. Esta função deve retornar a média das duas notas
# se ambas forem válidas (entre 0 e 10), caso contrário, deve retornar -1.

# Dentro da função media2notas, defina uma função interna chamada notaValida que
# aceite um parâmetro n e retorne True se n estiver entre 0 e 10, caso contrário, 
# retorne False.

# No programa principal:

# Solicite ao usuário que insira a primeira nota.

# Solicite ao usuário que insira a segunda nota.

# Chame a função media2notas com as duas notas inseridas.

# Se o retorno da função for igual a -1, imprima "Nota(s) inválida(s)!".

# Caso contrário, imprima a média calculada.

import os
os.system('cls')

def media2notas(n1, n2):
    
    def notaValida(n: float):
        return n >= 0 and n <= 10
        
    if notaValida(n1) and notaValida(n2):
        return (n1 + n2) / 2
    else:
        return -1 # retornará -1 caso um dos parâmetros não seja uma nota válida
    


nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

retorno = media2notas(nota1, nota2)

if retorno != -1:
    print(f'A média do aluno foi: {retorno:.1f}')
else:
    print('Nota(s) inválida(s)!')