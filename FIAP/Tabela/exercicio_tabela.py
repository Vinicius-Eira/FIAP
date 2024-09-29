"""Crie um dicionário com 5 keys e faça um sistema coma seguinte sugestão de menu:

0 - SAIR
1 - Cadastrar
2 - Consultar
3 - Alterar
4 - Excluir

"""

import os
os.system('cls')

cadastro_pessoa = []

def exibir_opcoes():
    print('0 - SAIR')
    print('1 - Cadastrar')
    print('2 - Consultar')
    print('3 - Alterar')
    print('4 - Excluir')

# Função para cadastrar pessoa física
def cadastrar():
    pessoa_fisica = {}
    pessoa_fisica['nome'] = input('Digite o nome: ')
    pessoa_fisica['cpf'] = input('Digite o CPF: ')
    pessoa_fisica['idade'] = int(input('Digite a idade: '))
    pessoa_fisica['gênero'] = input('Digite o gênero: ')
    pessoa_fisica["email"] = input('Digite o email: ')
    
    while True:
        altura_input = input('Digite a altura (em metros, ex: 1.75): ')
        try:
            pessoa_fisica["altura"] = float(altura_input)
            break  # Se a conversão para float for bem-sucedida, sai do loop
        except ValueError:
            if ',' in altura_input:
                print("\nPor favor, utilize ponto (.) em vez de vírgula (,). Exemplo: 1.75")
            else:
                print("\nValor inválido. Digite um número no formato correto.")
    
    cadastro_pessoa.append(pessoa_fisica)
    print("\nCadastro realizado com sucesso!")
    voltar_ao_menu_principal()

# Função para consultar todas as pessoas cadastradas
def consultar():
    if len(cadastro_pessoa) == 0:
        print("\nNenhuma pessoa cadastrada.")
    else:
        print("\nLista de pessoas cadastradas:")
        for i, pessoa in enumerate(cadastro_pessoa, 1):
            print(f"\nRegistro {i}:")
            print(f"Nome....: {pessoa['nome']}")
            print(f"Idade...: {pessoa['idade']}")
            print(f"Sexo....: {pessoa['sexo']}")
            print(f"Email...: {pessoa['email']}")
            print(f"Altura..: {pessoa['altura']} metros")
    
    voltar_ao_menu_principal()

# Função para alterar cadastro de uma pessoa
def alterar():
    nome = input('Digite o nome da pessoa a ser alterada: ')
    for pessoa in cadastro_pessoa:
        if pessoa['nome'] == nome:
            print(f"\nDados atuais: {pessoa}")
            pessoa['nome'] = input('Digite o novo nome: ')
            pessoa['cpf'] = input('Digite o novo CPF: ')
            pessoa['idade'] = int(input('Digite a nova idade: '))
            pessoa['sexo'] = input('Digite o novo sexo: ')
            pessoa['email'] = input('Digite o novo email: ')
            
            while True:
                altura_input = input('Digite a nova altura (em metros, ex: 1.75): ')
                try:
                    pessoa["altura"] = float(altura_input)
                    break
                except ValueError:
                    if ',' in altura_input:
                        print("\nPor favor, utilize ponto (.) em vez de vírgula (,). Exemplo: 1.75")
                    else:
                        print("\nValor inválido. Digite um número no formato correto.")
            
            print("\nDados alterados com sucesso!")
            break
    else:
        print("\nPessoa não encontrada.")
    voltar_ao_menu_principal()

# Função para excluir uma pessoa
def excluir():
    nome = input('Digite o nome da pessoa a ser excluída: ')
    for pessoa in cadastro_pessoa:
        if pessoa['nome'] == nome:
            cadastro_pessoa.remove(pessoa)
            print("\nPessoa excluída com sucesso!")
            break
    else:
        print("\nPessoa não encontrada.")
    voltar_ao_menu_principal()

# Função para voltar ao menu principal com limpeza de tela
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu')
    os.system('cls')  # Limpar a tela antes de voltar ao menu
    menu()

# Função do menu principal
def menu():
    while True:
        exibir_opcoes()
        opcao = int(input('\nEscolha uma opção: '))
        if opcao == 0:
            print('Saindo...')
            exit()  # Fecha o programa
        elif opcao == 1:
            cadastrar()
        elif opcao == 2:
            consultar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            excluir()
        else:
            print('Opção inválida. Tente novamente.')

# Executar o menu principal
menu()


