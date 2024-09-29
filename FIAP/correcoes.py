import os
os.system("cls")

# Exercício 1. Dado um numero pelo usuário, calcular o dobro

# numero = float(input('Digite um número: '))

# dobro = numero * 2

# print(dobro)
 
#  _____________________________________________________________________________
 
# Exercício 2. Dado um numero pelo usuário, calcular o quadrado
 
 
# numero = float(input('Digite um número: '))

# quadrado = numero ** 2

# print(quadrado)

#  _____________________________________________________________________________
 
# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior

# numero = int(input('Digite um número: '))

# anterior = numero - 1
# posterior = numero + 1

# print(f'O número anterior é {anterior} e o posterior é {posterior}')

#  _____________________________________________________________________________
 
# Exercício 4. Dados dois numeros pelo usuário, calcular a potencia

# base = int(input('Digite a base do número: '))
# expoente= int(input('Digite o expoente do número: '))

# potencia = base ** expoente

# print(f'O resultado de, {base} elevado a expoente é´{potencia} ')

 
# Exercício 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5

# numero = int(input("Digite um número inteiro: "))
# proximo_multiplo_5 = numero // 5 + 5 * 5
# print(f'O próximo múltiplo de 5 após , {numero} é , {proximo_multiplo_5}')

# ______________________________________________________________________________


# Exercicio 6. Dada uma quantia pelo usuário, informar quantas cédulas de 100, 50, 20 e 10 s"ao necessárias para compor esta quantia
 
# quantia = int(input("Digite uma quantia R$: "))

# cedulas100 = quantia // 100
# quantia %= 100
# cedulas50 = quantia // 50
# quantia %= 50
# cedulas20 = quantia // 20
# quantia %= 20
# cedulas10 = quantia // 10

# print(f'\nR$100\t-> {cedulas100}\nR$50\t-> {cedulas50}\nR$20\t-> {cedulas20}\nR$10\t-> {cedulas10}')

#  _____________________________________________________________________________
 
 
# Exercicio 7. Dados 4 numeros, calcular a media
 
 
# soma = 0
# for i in range(4):
#     numero = float(input(f"Digite o {i + 1}º número: "))
#     soma += numero

# media = soma / 4
# print("A média dos números é", media)
 
 
 
# Exercicio 8. Dados os dias de vida de uma pessoa, informar quantos anos, meses e dias ela tem de vida


# dias_vida = int(input("Digite o número de dias de vida: "))
# anos = dias_vida // 365
# meses = (dias_vida % 365) // 30
# dias = (dias_vida % 365) % 30
# print(f'A pessoa tem, {anos}, anos,, {meses}, meses e, {dias}, dia de vida.') 
# ______________________________________________________________________________

# Calculo do delta / baskara

# a = -1
# b = 2
# c = 3

# delta = b ** 2 - 4 * a * c


# x1 = (-b + delta ** (1/2)) / 2 * a # ou voce usa 0.5 no lugar do 1/2

# x2 = (-b - delta ** (1/2)) / 2 * a


# print(f'O delta é {delta}\nO valor de x1 é {x1}\nO valor de x2 é {x2}')


# O delta é 16
# O valor de x1 é -1.0
# O valor de x2 é 3.0
# ______________________________________________________________________________


# valor = float(input("Valor: R$ "))
# print("""
#     1 - Cartão de crédito
#     2 - Outros
# """)
# forma_pagamento = int(input("Escolha: "))
# if forma_pagamento == 1:
#     valor_reajustado = valor * 1.02
# else:
#     valor_reajustado = valor * 0.95

# print(f"""
#       Compra.....R$ {valor:.2f}
#       Reajuste...R$ {valor_reajustado:.2f}
# """)

#_______________________________________________________________________________
"""Exercício utilizando while -> 04/04/24"""


# 1 -> Pedir dois números e exibir os números do intervalo sem considera-los

# Exemplo: entrada -> 2         9        saída -> 3 4 5 6 7 8



# while True:

#     inicio = int(input("Inicio: "))
#     fim = int(input("Fim: "))

#     inicio += 1

#     while inicio < fim:
#         print(inicio)
#         inicio += 1

#     opcao = input("Continuar, s ou n?")
#     if opcao == 'n':
#         break

#     print("\nObrigado por utilizar o nosso sistema.")
#     print("Todos os direitos são reservados.")



# 2 -> Pedir dois números ao usuario e exibir em ordem decrescente

# Exemplo: entrada -> 8     1     saída -> 7 6 5 4 3 2 1


# ordem decrescente
# inicio = int(input("Inicio: "))
# fim = int(input("Fim: "))

# while inicio >= fim:
#     print(inicio)
#     inicio -= 1
    
    
# 3 -> Dado um número, exibir os seus 10 primeiros múltiplos

# Exemplo: entrada -> 5     saída -> 5 10 15 20 25 30 35 40 45 50


# numero = int(input('Digite um número: '))
# limite = int(input("Digite um limite para encontrar os múltiplos: "))

# i = 1

# while i <= limite:
#     if i % numero == 0:
#         print(i, end=' ')
#     i += 1


# 4 -> Dados 10 números pelo usuario, exibir o de maior valor

# Exemplo: entrada -> 5 3 9 8 1 7 15 34 -53   saída -> maior: 34


# volta = 1

# print("Digite 10 numeros:")
# num = int(input(f"{volta}.o = "))
# maior = num

# while volta < 10:
#     num = int(input(f"{volta + 1}.o = "))
#     if num > maior:
#         maior = num
#     volta += 1

# print(f"Maior = {maior}")
