"""Segue a tela de menu:
MENU
O - SAIR
1— Digite um nome completo
12 — Exibe separado o Nome do Sobrenome
3 — Conta quantas palavras há no nome completo
14 — Exibir em formato de bibliografia

Escolha:
Se o usuário escolher a opção 1 — Digite um nome Completo, deverá abrir uma tela para que ele
faça isso:
Edson de Oliveira Silva

Retornando ao menu, se o usuário escolher a opção 2 — Exibe separado o Nome do Sobrenome,
primeiramente verifica se há algum nome digitado, se houver o nome deverá ser apresentado da
seguinte forma:
Sobrenome: de Oliveira Silva

Retornando ao menu, se o usuário escolher a opção 3 — Conta quantas palavras há no nome
completo, deverá aparecer o nome completo e a quantidade de palavras no seguinte formato:
Retornando ao menu, se o usuário escolher a opção 4 — Exibir em formato de bibliografia, deverá
aparecer o último sobrenome em maiúsculo, a vírgula seguida do restante do nome.

Veja o formato:

REQUISITOS:
e Cadaopçãodo menu deve resolver somente o que é solicitado.
e Assim que executar uma opção, o fluxo do programa deve voltar ao menu principal (Sem
perguntar se quer continuar Sim ou Não, ou algo similar).
e Aoacessaras opções 2, 3 ou 4 caso o usuário não tenha digitado o nome (opção 1), exibir a
mensagem “Primeiramente digite um nome na opção 1”.
e Seo usuário digitar algo diferente de O, 1, 2, 3 ou 4, exibir a mensagem “Opção inválida,
digite um item de 0 a 4.”
e Asrotinas do menu devem ser feitas em subalgoritmos.
"""


import os

def exibir_menu():
    print("MENU")
    print("0 - SAIR")
    print("1 - Digite um nome completo")
    print("2 - Exibe separado o Nome do Sobrenome")
    print("3 - Conta quantas palavras há no nome completo")
    print("4 - Exibir em formato de bibliografia")
    print()  # Espaço extra para separar o menu das instruções

def opcao_digitar_nome():
    print("\nDigite o nome completo:")  # Linha em branco antes
    nome = input()
    print()  # Linha em branco depois
    return nome

def opcao_exibir_nome_sobrenome(nome):
    print()  # Linha em branco antes
    if nome:
        nome_separado = nome.split(" ")
        primeiro_nome = nome_separado[0]
        sobrenome = " ".join(nome_separado[1:])
        print(f"Nome: {primeiro_nome}")
        print(f"Sobrenome: {sobrenome}")
    else:
        print("Primeiramente digite um nome na opção 1")
    print()  # Linha em branco depois

def opcao_contar_palavras(nome):
    print()  # Linha em branco antes
    if nome:
        palavras = nome.split(" ")
        print(f"Nome completo: {nome}")
        print(f"Quantidade de palavras: {len(palavras)}")
    else:
        print("Primeiramente digite um nome na opção 1")
    print()  # Linha em branco depois

def opcao_exibir_bibliografia(nome):
    print()  # Linha em branco antes
    if nome:
        nome_separado = nome.split(" ")
        sobrenome = nome_separado[-1].upper()
        resto_nome = " ".join(nome_separado[:-1])
        print(f"{sobrenome}, {resto_nome}")
    else:
        print("Primeiramente digite um nome na opção 1")
    print()  # Linha em branco depois

def menu():
    nome = ""
    while True:
        # Limpeza de tela para melhorar a visualização (opcional)
        os.system('cls')
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("\nSaindo...\n")
            break
        elif escolha == "1":
            nome = opcao_digitar_nome()
        elif escolha == "2":
            opcao_exibir_nome_sobrenome(nome)
        elif escolha == "3":
            opcao_contar_palavras(nome)
        elif escolha == "4":
            opcao_exibir_bibliografia(nome)
        else:
            print("\nOpção inválida, digite um item de 0 a 4.\n")

        input("Pressione Enter para voltar ao menu.")

# Executar o programa principal
menu()
