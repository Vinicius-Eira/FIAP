# Nome: Vinicius

import os
import json


def limpar_tela():
    os.system("cls" if os.name == 'nt' else "clear")
    
limpar_tela()

with open('dados.txt', 'w') as dados_file:
    dados_file.write('12345t, edson@fiap.com.br\n')
    dados_file.write('01020d, maria@hotmail.com\n')
    dados_file.write('1abcde, estela@ig.com.br\n')
    dados_file.write('123abd, vania@terra.com.br\n')


logins = []
emails = []

with open('dados.txt', 'r') as dados_file:
    for linha in dados_file:
        login, email = linha.strip().split(', ')
        logins.append(login)
        emails.append(email)


with open('login.txt', 'w') as login_file:
    for login in logins:
        login_file.write(login + '\n')


with open('email.txt', 'w') as email_file:
    for email in emails:
        email_file.write(email + '\n')


print("login.txt")
with open('login.txt', 'r') as login_file:
    print(login_file.read())

print("email.txt")
with open('email.txt', 'r') as email_file:
    print(email_file.read())


dados_dict = {"login": logins, "email": emails}


with open('dados.json', 'w') as json_file:
    json.dump(dados_dict, json_file, indent=4)


print("dados.json")
with open('dados.json', 'r') as json_file:
    print(json_file.read())
