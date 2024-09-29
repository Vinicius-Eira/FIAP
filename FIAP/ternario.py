# TERNÁRIO
"""
Sintaxe:
[<variavel> = ] <comando True> if <condicao> else <comando False>
"""
# Sem usar variavel
import os
os.system("cls" if os.name == 'nt' else "clear")
# os.system("dir" if os.name == 'nt' else "ls")
idade = 19
print("Maior de idade") if idade >= 18 else print("Menor de idade")

"""
Sintaxe:
[<variavel> = ] <comando True> if <condicao> else <comando False>
"""
venda = 500
bonus = 50 if venda > 1000 else 30
print(venda, bonus)

"""
Sintaxe:
[<variavel> = ] <comando True> if <condicao> else <comando False>
"""
venda = 7000
desconto = venda - (venda * 0.1 if venda > 1000 else venda * 0.05)
print(venda, desconto)