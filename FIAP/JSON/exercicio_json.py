import os
import json

# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("0. Sair")
    print("1. Cadastrar novo Registro")
    print("2. Listar os Registros")
    print("3. Editar um Registro")

# Função para carregar dados do arquivo JSON
def carregar_dados():
    if os.path.exists("arquivo.json"):
        with open("arquivo.json", "r") as file:
            return json.load(file)
    return {}

# Função para salvar dados no arquivo JSON
def salvar_dados(pessoas):
    with open("arquivo.json", "w") as file:
        json.dump(pessoas, file, indent=4)

# Função para cadastrar um novo registro
def cadastrar_registro(pessoas):
    cpf = input("Digite o CPF: ")
    if cpf in pessoas:
        print("Registro já existe para esse CPF.")
        return
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")
    pessoas[cpf] = {'nome': nome, 'idade': idade, 'email': email}
    salvar_dados(pessoas)
    print("Registro cadastrado com sucesso!")

# Função para listar todos os registros
def listar_registros(pessoas):
    if not pessoas:
        print("Nenhum registro encontrado.")
        return
    for cpf, info in pessoas.items():
        print(f"\nCPF: {cpf}")
        for k, v in info.items():
            print(f"  {k}: {v}")

# Função para editar um registro existente
def editar_registro(pessoas):
    cpf = input("Digite o CPF do registro a ser editado: ")
    if cpf not in pessoas:
        print("Registro não encontrado.")
        return
    print(f"Editando registro de {cpf}:")
    nome = input(f"Digite o novo nome ({pessoas[cpf]['nome']}): ") or pessoas[cpf]['nome']
    idade = input(f"Digite a nova idade ({pessoas[cpf]['idade']}): ")
    email = input(f"Digite o novo email ({pessoas[cpf]['email']}): ") or pessoas[cpf]['email']
    pessoas[cpf] = {'nome': nome, 'idade': int(idade) if idade else pessoas[cpf]['idade'], 'email': email}
    salvar_dados(pessoas)
    print("Registro atualizado com sucesso!")

# Função principal do programa
def main():
    os.system("clear")
    pessoas = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao == '1':
            cadastrar_registro(pessoas)
        elif opcao == '2':
            listar_registros(pessoas)
        elif opcao == '3':
            editar_registro(pessoas)
        else:
            print("Opção inválida. Tente novamente.")

# Chamada direta da função principal
main()

