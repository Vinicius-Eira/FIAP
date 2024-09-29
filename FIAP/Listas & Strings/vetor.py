import os
os.system('cls')

"""

Insere os elementos no vetor diretamente

0 1 2 3 4 <- INDICES

"""

v = [45, 89, 32, 12, 33]
print(f'Exibe a posição 2 do vetor: v[2] = {v[2]}')
print(f'Exibe o vetor inteiro: V = {v}')

# Mudando a primeira posição para 10

v[0] = 10
print(f'V = {v}')

# Saída | Exibe a posição 2 do vetor: v[2] = 32
# Exibe o vetor inteiro: V = [45, 89, 32, 12, 33]
# V = [10, 89, 32, 12, 33]

# ______________________________________________________________________________
os.system('cls')


v = [45,-89, 32,-12, 33]
print('Forma Bruta: ', v)

for i in range(0,5,1):
        print(f'\nV[{i}] =  {v[i]:6.2f}')
        
        
# Fazer uma rotina que permita ao usuário digitar os elementos do vetor e depois
# exibi-los

print('_________________')
v = [45,-89, 32,-12, 33]

print("\nForma Bruta: ",v)

# --------------- Preenchendo o vetor
print("\nPREENCHENDO:")
for i in range(0, 5, 1):
    v[i] = int(input(f"V[{i}] = "))

# --------------- Exibindo o vetor
print("EXIBINDO:")
for i in range(0, 5, 1):
    print(f"V[{i}] = {v[i]:6.1f}")




        
    