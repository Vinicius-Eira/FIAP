"""
Uma turma tem 10 alunos. E o professor desenvolveu uma rotina para ter o 
gerenciamento dos alunos.

A média anual se dá por:

-Checkpoint: São 3, e a média comum das duas maiores notas vale 20% da média.

- Challenge: São 2 sprints que é calculada com média simples das duas e também
vale 20% da média final.

- GLobal solution: apenas uma nota que vale 60 % da média final.


REQUISITOS:

- A média final irá passar é ao menos 6, senão estará reprovado

- Toda vez que for digitada uma nota inválida ( fora de 0 e 10 ), advertir
e pedir novamente a digitação da mesma nota.


RELATORIO:

- Para cada aluno exibir todas as notas que ele tirou, as médias calculadas e 
se ele está aprovado ou não.

- No final da digitação das notas dos des alunos, ebibir:

     - quantos foram aprovados
     - quantos foram reprovados
     - quantos tiraram a média final maxima (nota 10)"""
     
     
'''
IMPLEMENTAÇÕES
- Colocar as porcentagens dos status
- verificar se são numeros as notas
- Exibir aprovado, reprovado e maximo do relatorio final em ordem decrescente
- exibir os status do relatório final no singular ou plural
'''
    
# import os
# os.system('cls')

# # Inicialização das variáveis de contagem
# aprovados = 0
# reprovados = 0
# nota_maxima = 0

# # Loop para cada aluno de 1 a 10
# for aluno in range(1, 11):
#     # Informações do aluno
#     print(f'\nInformações do {aluno}° aluno')

#     # Captura das notas dos checkpoints, com validação de entrada
#     cp1 = float(input('\nDigite a nota do 1° Checkpoint: '))
#     while cp1 < 0 or cp1 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp1 = float(input('\nDigite a nota do 1° Checkpoint novamente: '))

#     cp2 = float(input('Digite a nota do 2° Checkpoint: '))
#     while cp2 < 0 or cp2 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp2 = float(input('\nDigite a nota do 2° Checkpoint novamente: '))

#     cp3 = float(input('Digite a nota do 3° Checkpoint: '))
#     while cp3 < 0 or cp3 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp3 = float(input('\nDigite a nota do 3° Checkpoint novamente: '))

#     # Cálculo da média dos checkpoints, descartando a menor nota
#     if cp1 < cp2 and cp1 < cp3:
#         menor = cp1
#     elif cp2 < cp1 and cp2 < cp3:
#         menor = cp2
#     else:
#         menor = cp3

#     media_checkpoint = (cp1 + cp2 + cp3 - menor) / 2

#     # Captura das notas dos challenges, com validação de entrada
#     challenge_1 = float(input('\nDigite a nota do 1° Sprint: '))
#     while challenge_1 < 0 or challenge_1 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         challenge_1 = float(input('\nDigite a nota do 1° Sprint novamente: '))

#     challenge_2 = float(input('Digite a nota do 2° Sprint: '))
#     while challenge_2 < 0 or challenge_2 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         challenge_2 = float(input('\nDigite a nota do 2° Sprint novamente: '))

#     # Cálculo da média dos challenges
#     media_challenge = (challenge_1 + challenge_2) / 2

#     # Captura da nota do global solution, com validação de entrada
#     global_solution = float(input('\nDigite a nota do global solution: '))
#     while global_solution < 0 or global_solution > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         global_solution = float(input('\nDigite a nota do Global Solution novamente: '))

#     # Cálculo da média final, considerando pesos de cada componente
#     media_final = (media_checkpoint * 0.2) + (media_checkpoint * 0.2) + (global_solution * 0.6)

#     # Impressão da média final do aluno
#     print('\n--Média Final do aluno--')
#     print(f'\nCheckpoint: {cp1}, {cp2}, {cp3}')
#     print(f'\nChallenge: {challenge_1}, {challenge_2}')

#     # Verificação do status do aluno (aprovado ou reprovado) e contagem
#     if media_final >= 6:
#         print(f'\n--STATUS-- => O aluno está aprovado: | {media_final:.1f} | ')
#         print('--------------------------')
#         aprovados += 1
#     else:
#         print(f'\n-- STATUS-- => O aluno está reprovado: | {media_final:.1f} |')
#         print('--------------------------')
#         reprovados += 1
        
#     # Contagem de alunos que obtiveram nota máxima
#     if media_final == 10:
#         nota_maxima += 1 

# # Impressão do total de alunos aprovados, reprovados e com nota máxima
# print(f'\nForam aprovados: {aprovados} alunos.')
# print(f'\nForam reprovados: {reprovados} alunos.')
# print(f'\nPassaram com nota máxima (10): {nota_maxima} aluno(s).')



# ______________________________________________________________________________


"""

CODIGO COM AS IMPLEMENTAÇÕES

"""


# os.system('cls')

# # Inicialização das variáveis de contagem
# aprovados = 0
# reprovados = 0
# nota_maxima = 0
# total_alunos = 10

# # Loop para cada aluno de 1 a 10
# for aluno in range(1,11):
#     # Informações do aluno
#     print(f'\nInformações do {aluno}° aluno')

#     # Captura das notas dos checkpoints, com validação de entrada
#     cp1 = float(input('\nDigite a nota do 1° Checkpoint: '))
#     while cp1 < 0 or cp1 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp1 = float(input('\nDigite a nota do 1° Checkpoint novamente: '))

#     cp2 = float(input('Digite a nota do 2° Checkpoint: '))
#     while cp2 < 0 or cp2 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp2 = float(input('\nDigite a nota do 2° Checkpoint novamente: '))

#     cp3 = float(input('Digite a nota do 3° Checkpoint: '))
#     while cp3 < 0 or cp3 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         cp3 = float(input('\nDigite a nota do 3° Checkpoint novamente: '))
        
#     if cp1 < cp2 and cp1 < cp3:
#         menor = cp1
#     elif cp2 < cp1 and cp2 < cp3:
#         menor = cp2
#     else:
#         menor = cp3

#     # Cálculo da média dos checkpoints, descartando a menor nota
#     media_checkpoint = (cp1 + cp2 + cp3 - menor) / 2


#     # Captura das notas dos challenges, com validação de entrada
#     challenge_1 = float(input('\nDigite a nota do 1° Sprint: '))
#     while challenge_1 < 0 or challenge_1 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         challenge_1 = float(input('\nDigite a nota do 1° Sprint novamente: '))

#     challenge_2 = float(input('Digite a nota do 2° Sprint: '))
#     while challenge_2 < 0 or challenge_2 > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         challenge_2 = float(input('\nDigite a nota do 2° Sprint novamente: '))

#     # Cálculo da média dos challenges
#     media_challenge = (challenge_1 +challenge_2) / 2

#     # Captura da nota do global solution, com validação de entrada
#     global_solution = float(input('\nDigite a nota do global solution: '))
#     while global_solution < 0 or global_solution > 10:
#         print('Nota inválida! Digite uma nota entre 0 e 10')
#         global_solution = float(input('\nDigite a nota do Global Solution novamente: '))

#     # Cálculo da média final, considerando pesos de cada componente
#     media_final = (media_checkpoint * 0.2) + (media_checkpoint * 0.2) + (global_solution * 0.6)
    
    
#     # Impressão da média final do aluno
#     print('\n--Média Final do aluno--')
#     print(f'\nCheckpoint: {cp1:.1f} | {cp2:.1f} | {cp3:.1f}')
#     print(f'\nChallenge: {challenge_1:.1f} | {challenge_2:.1f}')
#     print(f'\nGlobal Solution: {global_solution:.1f}')
#     print(f'\nMédia Final: {media_final:.1f}')
#     print('_________________________________')

#     # Determinação do status do aluno e contagem
#     if media_final >= 6:
#          print(f'\n--STATUS-- => O aluno está aprovado: | {media_final:.1f} | ')
#          print('--------------------------')
#          aprovados += 1
#     else:
#          print(f'\n-- STATUS-- => O aluno está reprovado: | {media_final:.1f} |')
#          print('--------------------------')
#          reprovados += 1
        
#     if media_final == 10:
#         nota_maxima += 1


# # Cálculo das porcentagens
# porcentagem_aprovados = (aprovados / total_alunos) * 100
# porcentagem_reprovados = (reprovados / total_alunos) * 100
# porcentagem_nota_maxima = (nota_maxima / total_alunos) * 100

# # Impressão das porcentagens
# print('_________________________________')
# print(f'\n Alunos Aprovados: |{aprovados}| - {porcentagem_aprovados:.2f}%\n')
# print(f'\n Alunos Reprovados: |{reprovados}| - {porcentagem_reprovados:.2f}%\n')
# print(f'Alunos que passaram com Nota Máxima (10): |{nota_maxima}| - {porcentagem_nota_maxima:.2f}%\n')

