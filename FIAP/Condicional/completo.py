import os
os.system("cls")

"""
Caso a pessoa fique em exame, pedir a nota de exame e recalcular 
a media simples (exame com a media), se a nova media for maior ou
igual a 6, o aluno está aprovado em exame, caso contrario, reprovado em 
exame. Em ambos os casos exibir a media final
"""


"""nota1 = float(input("Nota 1: "))
if nota1 < 0 or nota1 > 10:
    print(f"Nota inválida: '{nota1}'")
else:
    nota2 = float(input("Nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print(f"Nota inválida: '{nota2}'")
    else:
        nota3 = float(input("Nota 3: "))
        if nota3 < 0 or nota3 > 10:
            print(f"Nota inválida: '{nota3}'")
        else:
            # verificar qual a menor
            menor = nota1

            if nota2 < menor:
                menor = nota2

            if nota3 < menor:
                menor = nota3

            # Calcular a média
            media = (nota1 + nota2 + nota3 - menor)
            
            
            if media >= 6: 
                print(f"Aprovado {media}")
            elif media < 4:
                print(f"Reprovado {media}")
            else:
                print(f"Exame {media}")"""


    


"""nota1 = float(input("Nota 1: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Nota 3: "))
        if nota3 >= 0 and nota3 <= 10:
            # verificar qual a menor
            menor = nota1

            if nota2 < menor:
                menor = nota2

            if nota3 < menor:
                menor = nota3

            # Calcular a média
            media = (nota1 + nota2 + nota3 - menor) / 2
            
            if media >= 6: 
                print(f"Aprovado {media}")
            elif media < 4:
                print(f"Reprovado {media}")
            else:
                print(f"Exame {media}")

        else:
            print(f"Nota inválida: '{nota3}'")
    else:
        print(f"Nota inválida: '{nota2}'")
else:
    print(f"Nota inválida: '{nota1}'")"""


    

# """
# def minha_funcao_mamae(nota1: int, nota2:int, nota3:int) -> int:
#     menor = nota1

#     if nota2 < menor:
#         menor = nota2

#     if nota3 < menor:
#         menor = nota3   

#     return menor 


# n1 = 19
# n2 = 1
# n3 = 12

# maior = minha_funcao_mamae(n1, n2, n3)
# menor = min(n1, n2, n3)

# print(maior)


# """
# """
# # nota inválida FORMA 1
# nota = float(input("Nota: "))
# if nota >= 0 and nota <= 10:
#     print("Nota válida")
# else:
#     print("Nota invalida")


# # nota inválida FORMA 2
# if nota >= 0:
#     if nota <= 10:
#         print("Nota válida")
#     else:
#         print("Nota inválida")
# else:
#     print("Nota inválida")


# # nota inválida FORMA 3
# nota = float(input("Nota: "))

# if nota < 0 or nota > 10:
#     print("Nota inválida")
# else:
#     print("Nota valida")

"""# nota inválida FORMA 4
nota = float(input("Nota: "))
if not (nota < 0 or nota > 10): # 87
#  not (87 < 0 or 87 > 10)
#  not (False or True)
#  not (True)
#  False

    print("Nota válida")
else:
    print("Nota invalida")"""

# calcula a media e vê se está aprovado ou reprovado
"""nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 6: 
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("Exame")"""


# # Calcular a media das duas maiores notas
# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# nota3 = float(input("Nota 3: "))

# menor = nota1

# if nota2 < menor:
#     menor = nota2

# if nota3 < menor:
#     menor = nota3


# media = (nota1 + nota2 + nota3 - menor) / 2


# """


# """
# CENÁRIO 1:
# Nota 1: 45
# Nota inválida!

# CENÁRIO 2:
# Nota 1: 5
# Nota 2: -5
# Nota inválida!

# CENÁRIO 3:
# Nota 1: 5
# Nota 2: 4
# Nota 3: 423
# Nota inválida!

# CENÁRIO 4:
# Nota 1: 0
# Nota 2: 8
# Nota 3: 9
# Aprovado média 8.5 | Exame | Reprovado
# """

