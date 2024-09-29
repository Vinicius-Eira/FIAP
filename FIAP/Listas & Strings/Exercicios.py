import os
os.system('cls')

"""
1. Fazer uma rotina que exiba o primeiro elemento de vetor.
        >> 45
        

2. Fazer uma rotina que exiba somente os números negativos contidos no vetor.
        >> - 89 -12


3. Fazer uma rotina que exiba a soma dos elementos do vetor.
        >> 9

4. Fazer uma rotina que exiba a média dos elementos do vetos.


5. Fazer uma rotina que exiba na tela os números ímpares contidos no vetor.


6. Fazer um procedimento que exiba na tela o primeiro e ultimo elemento do vetor. 
        >> 45 33

"""

v = [45,-89, 32,-12, 33]

# 1

print("\n1. Primeiro elemento do vetor")
print(f'\nV= {v[0]}')


# 2
print('_____________________')
print("\n2. números negativos contidos no vetor.")
print(f'\nV = {v[1]:6.1f}, {v[3]:6.1f}')

# ou de outra forma
print('\n_________OUTRA FORMA___________')

for i in range(0, 5, 1):
    if v[i] < 0:
        print(f"\nV[{i}] = {v[i]:6.1f}")



# 3

print('_____________________')
print('\n3. Soma dos elementos')
soma = 0

for i in range(0,5,1):
        soma += v[i]
        
print(f'\nSoma = {soma}')
        

# 4

print('_____________________')
print("\n4. Média dos elementos")
        
media = soma / 5

print(f'\nMédia = {media}')


# 5

print('\n5. Números ímpares contidos no vetor')
for i in range(0,5,1):
        if v[i] % 2 != 0:
          print(f'\nV[{i}] =  {v[i]:4.1f}')

