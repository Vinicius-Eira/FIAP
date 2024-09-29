# Decisão simples
# Problema: Calcular o módulo matemático de um número
# |-6| -> 6
# |23| -> 23
import os
os.system("cls")
"""
# NARRATIVA:
# - Pedir um numero
num = int(input("Numero: ")) 
# - Se o numero for negativo
if num < 0:
    #   - transformo em positivo
    num = num * -1 # -56 * -1 -> 56
# - exibir o numero
print(num) 
"""

# Dado o valor de uma venda, dar desconto de 50 reais caso ela seja maior que 500 reais. No final exibir o valor final da venda

# venda = int(input("Venda: "))
# com_desconto = venda
# if venda > 500:
#     com_desconto = venda - 50
# print(f"""
# Valor da Venda..: R$ {venda:.2f}
# Valor Final.....: R$ {com_desconto:.2f}
# """)


# valor_da_compra = float(input("Digite o valor da compra: "))
# meio_de_pagamento = input("Pagamento: 1- cartão / 2- outros ")
 
# if meio_de_pagamento == "1":
#     modificador = 0.02
#     valor_final = valor_da_compra + (valor_da_compra * modificador)
# else:
#     modificador = 0.05
#     valor_final = valor_da_compra + (valor_da_compra * modificador)
# print(f"""
#       O valor da sua compra é de: {valor_da_compra}
#       O Valor do desconto é de: {modificador * 100}%
#       O valor final é: {valor_final}
#       """)