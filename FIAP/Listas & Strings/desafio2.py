import os
os.system('cls')


'''
Faça um função isfloat(string) que pegue uma string passada por parâmetro e
retorne True caso esta string represente um valor float ou False caso não
seja




->              PROGRAMA PRINCIPAL            <- 

        resp = isfloat('Edson)        >> False
        resp = isfloat('45.78)
        >> True
        resp = isfloat('78')
        >> False
        resp = isfloat('234.')
        >> True
        resp = isfloat('234,67')
        >> False
        resp = isfloat('12.567.34')
        >> True
        resp = isfloat('-12.5')
        >> True
        
'''


def isfloat(n: str) -> bool:
    if not n:  # Verifica se a string está vazia
        return False
    
    operadores = '+-'
    ponto = '.'
    numeros = '0123456789'
    ponto_count = 0  # Variavel que conta a qnt de pontos decimais

    # Verifica o primeiro caractere
    if n[0] not in operadores and n[0] not in numeros and n[0] != ponto:
        return False

    # Verifica cada caractere de números
    for i in range(1, len(n)):
        # Se o caractere não estiver nos numeros ou for diferente do ponto retorna Falso
        if n[i] not in numeros and n[i] != ponto:
            return False
        # Se o caractere foi igual o ponto adiciona ao pontos decimais
        if n[i] == ponto:
            ponto_count += 1
        if ponto_count <= 2:  # Até dois pontos decimais são permitidos
            return True

    # Para casos como '123.' ou '-123.' que são válidos floats
    if n[-1] == ponto and ponto_count == 1:
        return True

    return ponto_count == 1  # Retorna True apenas se houver um ponto decimal


# Abro um loop de repetição que será interrompido caso eu peça
while True:            
    decimal = input("\nNúmero: ")
    print(f"{decimal} é número float =  {isfloat(decimal)}")
    
     # Solicito ao usuário que decida se deseja inserir outro número ou encerrar o programa
    continuar = input('Você deseja digitara mais algum número?  sim/não: ')
    # Se a resposta não for 'sim', encerro o loop e imprimo que o programa foi encerrado
    if continuar.lower() != 'sim':
        print('PROGRAMA ENCERRADO')
        break # Encerra o loop e sai do programa
   
   
   
