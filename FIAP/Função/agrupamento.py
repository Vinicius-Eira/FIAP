import os
os.system('cls')

# Escreva um programa Python que calcule a média de três checkpoints inseridos 
# pelo usuário. Cada checkpoint deve ser um número real. O programa deve calcular
# a média dos checkpoints, excluindo o menor valor entre os três.

# Instruções:

# Defina uma função chamada menor3notas que aceite três parâmetros, n1, n2 e n3, 
# representando os checkpoints. Esta função deve retornar o menor valor entre 
# os três.

# Defina uma função chamada mediacp que aceite três parâmetros, n1, n2 e n3, 
# representando os checkpoints. Esta função deve retornar a média dos checkpoints,
# excluindo o menor valor entre os três. Para calcular a média, você pode somar
# os três checkpoints e subtrair o menor deles antes de dividir por 2.

# No programa principal:

# Solicite ao usuário que insira o valor do primeiro checkpoint.

# Solicite ao usuário que insira o valor do segundo checkpoint.

# Solicite ao usuário que insira o valor do terceiro checkpoint.

# Chame a função mediacp com os três checkpoints inseridos.

# Imprima a média dos checkpoints calculada.


def menor3notas(cp1, cp2, cp3):
     menor = cp1
     if cp2 < menor:
         menor = cp2
     else:
         menor = cp3
     return menor
 
def mediacp(cp1, cp2, cp3):
    return (cp1 + cp2 + cp3 - menor3notas(cp1, cp2, cp3)) / 2

# -> PROGRAMA PRINCIPAL

cp1 = float(input('Digite a nota do 1° Checkpoint: '))
cp2 = float(input('Digite a nota do 2° Checkpoint: '))
cp3 = float(input('Digite a nota do 3° Checkpoint: '))

media = mediacp(cp1, cp2, cp3)

print(f'A média do aluno é: {media}')
 