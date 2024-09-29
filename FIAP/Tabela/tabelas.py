import os
os.system('cls')

# t = {
#   'nome': 'Edson',
#   'idade': 30,
#   'altura': 1.75
# }

tabela = list()

def exibe_tabela(t: list) -> None:
    print("Exibindo:")
    for i in range(0,len(tabela), 1):
        print(f"Registro {i+1}:")
        print(f"Nome....: {t[i]['nome']}\n")
        print(f"Idade...: {t[i]['idade']}\n")



contato = {
    'nome': 'Edson',
    'idade': 50,
}

contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))
tabela.append(contato.copy()) # copy() cria uma referência em outro espaço de memória

contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))
tabela.append(contato.copy())



exibe_tabela(tabela)


# criando uma chavee - (key) e valor (value)

# contato['email'] = 'prof@fiap.com.br'
# contato['idade'] = int(input("Idade: "))

# EXCLUIR UMA CHAVE - 2 MANEIRAS
# contato.pop('email) 
# del contato['email']
