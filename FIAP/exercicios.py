import os
os.system("cls")

"""
1. Dada uma nota, verificar se ela é válida (entre 0 a 10 inclusive)
2. Dadas duas notas, calcular a média e verificar se está aprovado. A média é 6.
3. Dadas 3 notas, descartar a menor e calcular a media simples das outras duas, se esta aprovado ou reprovado. Média 6
4. Dado um número, informar se ele é positivo, negativo ou nulo.
"""


# 1:

# nota = int(input('Digite uma nota: '))

# if nota >= 0 and nota <= 10:
#     print(f"A nota '{nota:.1f}' é valida ;)")
# else:
#     print(f" A nota '{nota:.1f}' é invalida :(")
    
    
    
# 2:

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# notas = (nota1, nota2) # ou como lista [nota1, nota2]
# media = (notas) / 2

# if media >= 6:
#     print('Aprovado')
# elif media >= 5 and media < 6:
#     print('Recuperação')
# else:
#     print('Reprovado')

# # 3:

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota:  '))
# nota3 = float(input('Digite a terceira nota: '))

# menor = nota1

# if nota2 < menor:
#     menor = nota2
    
# if nota3 < menor:
#     menor = nota3
    
# media = (nota1 + nota2 + nota3 - menor) / 2

# if media >=6:
#  print(f'A média é {media}')

# 4:

# num = int(input('Digite um número: '))

# if num > 0:
#     print(f'O número {num}é positivo')
# elif num == 0:
#     print(f'O número {num} é nulo')
# else:
#     print(f'O número {num} é negativo')

# # agora sem o elif

# num = int(input('Digite um número: '))

# if num > 0:
#     print(f'O número {num} é positivo')
# else:
#  if num < 0:
#      print(f'O número {num} é negativo')
     
#  else:
#      print(f'O número {num} é nulo') 
# ______________________________________________________________________________

"""

CHECKPOINT 1 REFAZENDO

"""

# REAJUSTE
# Salário mínimo: 1302
#  - Até 2 SM: reajuste de 6.45%
#  - Mais que 2 e até 5 Sm: reajuste de 4.55%
#  - Mais de 5 SM: 2.89%
# BONIFICAÇÂO (BONÛS)
# - Bônus de 1000 para quem não faltou

#  Faremos partes por partes

"""# Solicitando o salário
salario = float(input('Salários: '))


# Verifica se o salário é válido
if salario >= 0:
    # Se é válido, o código é executado
    ate_2_sm = 2 * 1302
    ate_5_sm = 5 * 1302
    if salario <= ate_2_sm:
        salario_reajustado = salario * 1.0645
    elif salario > ate_5_sm:
        salario_reajustado = salario * 1.0289
    else:
        salario_reajustado = salario * 1.0455


# Verifica o número de faltas e se a pessoa tem ou não o bônus
    faltas = int(input('Faltas: '))
    if faltas <= 0:
        bonus = 1000
    else:
        bonus = 0

        
    print(f'Salário: {salario:.2f}')
    print(f'Salário Reajustado: {salario_reajustado:.2f}')
    print(f'Bônus: {bonus:.2f}')
  # salário válido
    
# Se o salário não for válido, o código não é executado
else:
    print('ERRO! Digite um salário positivo!')"""
    
# ______________________________________________________________________________

# lendo a placa como texto
# placa = input("Digitos da Placa: ")
 
# # verifiquei se o texto só contem numeros
# if placa.isnumeric():
#     # Se for só numeros, converter o texto para numero
#     placa = int(placa)
 
#     # calcular o ultimo digito
#     ultimo_digito = placa % 10
 
#     # verificar o digito | dia do rodizio
#     match ultimo_digito:
#         case 1 | 2:
#             print("Segunda-feira")
#         case 3 | 4:
#             print("Terça-feira")
#         case 5 | 6:
#             print("Quarta-feira")
#         case 7 | 8:
#             print("Quinta-feira")
#         case 9 | 0:
#             print("Sexta-feira")
# else:
#     # Caso o valor digitado não seja numero
#     print("O valor digitado não é numero!")   

# ______________________________________________________________________________
"""Exercício utilizando while -> 04/04/24"""


# 1 -> Pedir dois números e exibir os números do intervalo sem considera-los

# Exemplo: entrada -> 2         9        saída -> 3 4 5 6 7 8


# inicio = int(input("Inicio: ")) # 4
# fim = int(input("Fim: "))

# while inicio < fim:
#     print(f'{inicio} ' , end= '')
#     if inicio == 10:
#         break
#     inicio += 1
# else:    
#     print("\nObrigado por utilizar o nosso sistema.")
#     print("Todos os direitos são reservados.")
    
    
# 2 -> Pedir dois números ao usuario e exibir em ordem decrescente

# Exemplo: entrada -> 8     1     saída -> 7 6 5 4 3 2 1


# inicio = int(input("Inicio: ")) # 4
# fim = int(input("Fim: "))

# while inicio > fim:
#     print(f'{inicio} ' , end= '')
#     inicio -= 1
    
    
# 3 -> Dado um número, exibir os seus 10 primeiros múltiplos

# Exemplo: entrada -> 5     saída -> 5 10 15 20 25 30 35 40 45 50


# numero = int(input('Digite um número: '))
# limite = int(input("Digite um limite para encontrar os múltiplos: "))


# i = 1

# while i <= limite:
#     if i % numero == 0:
#         print(i)
#     i += 1
    

# 4 -> Dados 10 números pelo usuario, exibir o de maior valor

# Exemplo: entrada -> 5 3 9 8 1 7 15 34 -53   saída -> maior: 34

# volta = 0

# while volta < 10:
#     numero = int(input('Digite um número: '))
#     maior = numero
#     if numero > maior:
#         maior_ = numero
#     volta += 1
    
# print(f'O maior número é {maior}')
    
# ______________________________________________________________________________
"""Exercício utilizando while -> 04/04/24"""

# 1 -> Peça dois números ao usuário e os exiba em ordem crescente. Se o primeiro 
# for maior do que o segundo número, exibir o intervalo da mesma forma.

# Entrada 1: 5  8     Saída 1: 5 6 7 8
# Entrada 2: 8  5     Saída 2: 5 6 7 8

# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))

# if num1 > num2:
#     num1, num2 = num2, num1
    
# while num1 <= num2:
#     print(f'{num1}', end=' ')
#     num1 += 1



# 2. Peça dois numeros ao usuário e os exiba em ordem crescente se o primeiros for
# menor que o segundo ou em ordem decrescente se o primeiro numero for maior que o
# segundo.

# Entrada 1: 5  8     Saída 1: 5 6 7 8
# Entrada 2: 8  5     Saída 2: 8 7 6 5


# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))

# if num1 < num2:
#     while num1 <= num2:
#      print(f'{num1} ' , end= ' ' )
#      num1 += 1
# elif num1 > num2:
#     while num1 >= num2:
#      print(f'{num1} ' , end= ' ')
#      num1 -= 1



# 3. Peça dois numeros ao usuário e a ordem ("C"rescente ou "D"ecrescente) e exiba
# o intervalo devido.
# Entrada 1: 5  8  D   Saída 1: 8 7 6 5
# Entrada 2: 8  5  C   Saída 2: 5 6 7 8

# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# opcao = input("Digite a ordem (C para crescente, D para decrescente): ")

# if opcao == 'C':
#     if num1 > num2:
#         num1, num2 = num2, num1
        
#     while num1 <= num2:
#      print(f'{num1}', end=' ')
#      num1 += 1
     
# elif opcao == 'D':
#     if num1 < num2:
#         num1, num2 = num2, num1
  
#     while num1 >= num2:
#      print(f'{num1} ' , end= ' ')
#      num1 -= 1
     
#_______________________________________________________________________________
"""Utilizando o laço for"""


# 2. Peça dois numeros ao usuário e os exiba em ordem crescente se o primeiros for
# menor que o segundo ou em ordem decrescente se o primeiro numero for maior que o
# segundo. 
# Entrada 1: 5  8     Saída 1: 5 6 7 8
# Entrada 2: 8  5     Saída 2: 8 7 6 5


# num1 = int(input('Inicio: '))
# num2 = int(input('Fim: '))

# if num1 <= num2:
#     for i in range(num1, num2 + 1, 1):
#         print(i, end = ' ')
# else:
#     for i in range(num1, num2 -1, -1):
#         print(i, end = ' ')




# 3. Peça dois numeros ao usuário e a ordem ("C"rescente ou "D"ecrescente) e exiba
# o intervalo devido.
# Entrada 1: 5  8  D   Saída 1: 8 7 6 5
# Entrada 2: 8  5  C   Saída 2: 5 6 7 8


# num1 = int(input('Inicio: '))
# num2 = int(input('Fim: '))
# ordem = input("[C]rescente ou [D]ecrescente? ")

# if num1 < num2:
#     menor = num1
#     maior = num2
# else:
#     menor = num2
#     maior = num1

# # if ordem == 'c' or ordem == 'C':
# if ordem.upper() == 'C':
#     for i in range(menor, maior + 1, 1):
#         print(i, end = ' ')
# # elif ordem == 'd' or ordem == 'D':
# elif ordem.upper() == "D": # retorna um texto com todos os caracteres em letras maiúsculas
#     for i in range(maior, menor - 1, -1):
#         print(i, end = ' ')
# else:
#     print("Digite C ou D")
