import os
os.system("cls")


# ALGORITMO.
"""Uma empresa dará um REAJUSTE aos seus funcionários e os BONIFICARÁ (eventualmente) conforme os 
critérios abaixo:
SOBRE O REAJUSTE:

Sabemos que o salário-mínimo é de R$ 1302,00 (hipoteticamente). 
• Se o funcionário ganhar até dois salários-mínimos, terá o reajuste de 6,45%. 
• Se ganhar mais de dois até cinco salários-mínimos, terá o reajuste de 4,55% .
• Se for mais de cinco salários-mínimos, o reajuste será de 2,89%

SOBRE O BONUS:
Receberá o bônus de 1000 reais o funcionário que não teve falta(s) no último ano. 
Sendo assim, dado o salário e a quantidade de faltas de um funcionário, fazer um programa que atenda à 
necessidade acima e exiba os resultados como nas telas abaixo
"""

"""REQUISITOS:
• Este Algoritmo deve ser executado para penas um funcionário (usuário).
• Deixar a execução do programa parecido com as informações contidas nastelas de execução (abaixo).
• Se for digitado um salário negativo, exibir a mensagem: “ERRO! Digite um salário positivo!” e o 
programa deve terminar.
• Caso seja digitado um número negativo na quantidade de faltas, considerar que não tem faltas e 
prosseguir com os cálculos e exibições.
• Não serão testados valores não numéricos (não se preocupe com isso)."""



"""salario_usuario = float(input("Informe o salário: "))
salario_minimo = 1302.00
bonus = 0
if salario_usuario < 0:
    print("ERRO! Digite um salário positivo!") # poderia por a mensagem no final do código

quantidade_faltas = int(input("Digite a quantidade de faltas: "))
if quantidade_faltas <0:
    print("Número inválido, digite um número positivo") # não era necessário
if salario_usuario == 1:
  reajuste = salario_usuario * 1.0645
if salario_usuario == 2:
 reajuste = salario_usuario * 1.0455 # inverti a ordem dos números multiplicados
else:
 reajuste = salario_usuario * 1.0289
 
if quantidade_faltas == 0:
  bonus = bonus + 1000
  
print(f"Salário:{salario_usuario: 2.0f}")
print(f"Qtd.de faltas:{quantidade_faltas: 2.0f}")

print(f"Salário..............:{salario_usuario: 1.2f}")
print(f"Salário Reajustado...:{reajuste: 1.2f}")
print(f"Bônus................:{bonus: 1.2f}")
"""



# SEMPRE FAZER ANOTAÇÔES DO QUE FOI REALIZADO


"""

CORREÇÂO CHECKPOINT 1

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
    
    
    
    
