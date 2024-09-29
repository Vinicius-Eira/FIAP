import os
os.system("cls")


def eh_numero(texto: str) -> bool:
    if texto >= "0" and texto <= "9":
        return True
    else:
        return False


valor = input("Digite um numero: ")
print(f"{valor} - {eh_numero(valor)}")


# lendo a placa como texto
placa = input("Digitos da Placa: ")

# verifiquei se o texto só contem numeros
if placa.isnumeric(): # ou isdigit()
    # Se for só numeros, converter o texto para numero
    placa = int(placa)

    # calcular o ultimo digito
    ultimo_digito = placa % 10

    # verificar o digito | dia do rodizio
    match ultimo_digito:
        case 1 | 2:
            print("Segunda-feira")
        case 3 | 4:
            print("Terça-feira")
        case 5 | 6:
            print("Quarta-feira")
        case 7 | 8:
            print("Quinta-feira")
        case 9 | 0:
            print("Sexta-feira")
else:
    # Caso o valor digitado seja não numero
    print("O valor digitado não é numero!")   
