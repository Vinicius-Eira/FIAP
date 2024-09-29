'''

MENU

1 - Intervalo
2 - Intervalo Aberto e Fechado
3 - Intervalo em ordem crescente ou decrescente
0 - SAIR

Escolha:


'''

import os

contador_opcao_1 = 0
contador_opcao_2 = 0
contador_opcao_3 = 0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_opcoes():
    print('1 - Intervalo')
    print('2 - Intervalo Aberto e Fechado')
    print('3 - Intervalo em ordem crescente ou decrescente')
    print('0 - Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    menu()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def intervalo():
    global contador_opcao_1
    contador_opcao_1 += 1
    
    limpar_tela()
    print('INTERVALO')
    primeiro_numero = int(input('Primeiro número: '))
    segundo_numero = int(input('Segundo número: '))
    
    if primeiro_numero > segundo_numero:
        primeiro_numero, segundo_numero = segundo_numero, primeiro_numero
    
    print(f'\n[{primeiro_numero}', end=' ')
    for n in range(primeiro_numero + 1, segundo_numero):
        print(f'{n}', end=' ')
    print(f'{segundo_numero}]')
    
    voltar_ao_menu_principal()

def intervalo_aberto_fechado():
    global contador_opcao_2
    contador_opcao_2 += 1
    
    limpar_tela()
    print('INTERVALO ABERTO E FECHADO')
    primeiro_numero = int(input('Primeiro número: '))
    segundo_numero = int(input('Segundo número: '))
    
    if primeiro_numero > segundo_numero:
        primeiro_numero, segundo_numero = segundo_numero, primeiro_numero

    tipo_intervalo = input('\n][ - Aberto ou [] - Fechado? ')

    if tipo_intervalo == 'Aberto':
        print(f'\n]{primeiro_numero}', end=' ')
        for n in range(primeiro_numero + 1, segundo_numero):
            print(f'{n}', end=' ')
        print(f' {segundo_numero}[', end='')
    elif tipo_intervalo == 'Fechado':
        print(f'\n[{primeiro_numero}', end=' ')
        for n in range(primeiro_numero + 1, segundo_numero):
            print(f'{n}', end=' ')
        print(f'{segundo_numero}]')
    else:
        opcao_invalida()

    voltar_ao_menu_principal()

def intervalo_crescente_decrescente():
    global contador_opcao_3
    contador_opcao_3 += 1
    
    limpar_tela()
    print('INTERVALO - Em ordem crescente ou decrescente')
    primeiro_numero = int(input('Primeiro número: '))
    segundo_numero = int(input('Segundo número: '))
    
    if primeiro_numero < segundo_numero:
        print(f'[{primeiro_numero}', end=' ')
        for n in range(primeiro_numero + 1, segundo_numero):
            print(f'{n}', end=' ')
        print(f'{segundo_numero}]')
    elif primeiro_numero > segundo_numero:
        print(f'[{primeiro_numero}', end=' ')
        for n in range(primeiro_numero - 1, segundo_numero, -1):
            print(f'{n}', end=' ')
        print(f'{segundo_numero}]')
    else:
        print(f'[{primeiro_numero}]')

    voltar_ao_menu_principal()

def menu():
    limpar_tela()
    exibir_opcoes()
    
    opcao = input('Escolha: ')

    match opcao:
        case '1':
            intervalo()
        case '2':
            intervalo_aberto_fechado()
        case '3':
            intervalo_crescente_decrescente()
        case '0':
            print('Saindo do programa.')
            exibir_contadores()  
        case _:
            opcao_invalida()

def exibir_contadores():
    global contador_opcao_1, contador_opcao_2, contador_opcao_3
    print('\nNúmero de execuções de cada opção:')
    print('1 - Intervalo:', contador_opcao_1, 'vezes')
    print('2 - Intervalo Aberto e Fechado:', contador_opcao_2, 'vezes')
    print('3 - Intervalo em ordem crescente ou decrescente:', contador_opcao_3, 'vezes')

menu()
