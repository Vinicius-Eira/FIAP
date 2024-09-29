import os
import oracledb
import pandas as pd

try:
    conn = oracledb.connect(user="pf1530",password="fiap",dsn='oracle.fiap.com.br:1521/ORCL')
    # criar os cursores
    inst_cadastro = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    print("Falha na conexão!! :[")
    conexao = False
else:
    print("Conexão aberta com sucesso! :]")
    conexao = True

while conexao:
    os.system("cls")
    print(""" 
    MENU
    ----
    0 - SAIR
    1 - Cadastrar pet
    """)
    escolha = int(input("Escolha: "))
    match escolha:
        case 0:
            break
        case 1:
            try:
                tipo = input("Tipo do pet: ")
                nome = input("Nome do pet: ")
                idade = int(input("Idade do pet: "))
                cadastro = f"""INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES ('{tipo}','{nome}',{idade})"""
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                print("Mano! digite um numero na idade cara!")
            except:
                print("Erro na transação como BD")
            else:
                print("Dados gravados com sucesso!")
