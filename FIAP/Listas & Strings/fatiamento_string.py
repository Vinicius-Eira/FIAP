import os
os.system("cls")

#         0   1   2   3   4   5   6   7   8  <=== índice positivo
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#        -9  -8  -7  -6  -5  -4  -3  -2  -1  <=== índice negativo

print(lista[4]) # -> 50
print(lista[-1]) # -> 90

# lista[inicio: fim: passo]
print(lista[2:5]) # -> 30, 40, 50
 
parte_lista = lista[3: 8] # -> 40, 50, 60, 70, 80
print(parte_lista) # -> 20, 30, 40, 50, 60
print(lista[-8:-3]) # -> 20, 30, 40, 50, 60
print(lista[0:9:2]) # -> 10, 30, 50, 70, 90
print(lista[-9:-1:1]) # -> 10, 20, 30, 40, 50, 60, 70, 80
print(lista[9:0:-1]) # -> 90, 80, 70, 60, 50, 40, 30, 20
print(lista[::3]) # -> 10, 40, 70



#_______________________________________________


#        012345678901234567890123456789012345678901
frase = "Dia 29 é aniversário de alguem, quem será?"

print(frase)
print(frase[0]) # -> D
print(frase[5:25]) # -> 9 é aniversário de a
print(frase[::-1]) # -> ?áres meuq ,meugla ed oirásrevina é 92 aiD | Inverso
print(frase[0:30:3]) # -> D  avsidau


#_______________________________________________


frase = "Agora veremos como o fatiamento funciona com strings"
print("1. " + frase)
print("2. " + frase[2])
print("3. " + frase[7:15])
print("4. " + frase[::-1])
print("5. " + frase[32:5:-3])
print("6. " + frase[2:20:2])

'''
1. Agora veremos como o fatiamento funciona com strings

2.0

3. eremos c

4. sgnirts moc anoicnuf otnemaitaf o omoc somerev arogA

5. ftmt ocor

6. oavrmscm
'''