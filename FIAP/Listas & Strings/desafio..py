# Sabemos que o método isdigit() e/ou isnumeric() analisam uma string passado por parâmetro e retorna true caso tenha somente números ou false caso um dos caracteres não seja Numerico.

# x = "123"
# print(x.isdigit())
# # True

# x = "A123"
# print(x.isdigit())
# # False

# # Porém a falha deste método é a de retornar false caso algum texto com numero inicie com + ou -.
# x = '-453'
# print(x.isdigit())
# # False

#___________________________________________
import os


# def eh_numero (n:str) -> bool:
#     operadores = '+-'
#     numeros = '0123456789'
#     resultado = True or False # essa variavel não é necessaria mas ajuda na lógica
                                # para ele retornar verdadeiro ou falso
    
#     if n[0] in operadores or n[0] in numeros:
#         resultado = True
#     else:
#         resultado = False
#     for i in range (1, len(n),1):
#             if n[i] in numeros:
#                 resultado = True
#             else:
#                 return False
        
#     return resultado # poderia trocar pelo True uma das duas formas
    


# inteiro = input("Número: ")

# print(f"{inteiro} é número inteiro =  {eh_numero(inteiro)}")
# #True



#                       -> OUTRA FORMA <-


os.system('cls')

def eh_numero(n: str) -> bool:
    operadores = '+-'
    numeros = '0123456789'
    resultado = True or False # essa variavel não é necessaria mas ajuda na lógica
                              # para ele retornar verdadeiro ou falso
                              
    # Se a string estiver fazia retorna falso                          
    if not n:
        return False
    
    
    # Verifica o primeiro caractere: deve ser um operador ou um número
    if n[0] not in operadores and n[0] not in numeros:
        return False
    
       # Verifica os caracteres restantes: devem ser todos números
    for i in range(1, len(n)):
        if n[i] not in numeros:
            return False
        
        
     # Se todas as verificações forem passadas, retorna verdadeiro   
    return resultado # poderia trocar pelo True uma das duas formas



# Loop principal do programa
while True:
    # Solicita ao usuário um número
    inteiro = input("Número: ")
    # Verifica se o número inserido é válido e imprime o resultado
    print(f"{inteiro} é número inteiro? = {eh_numero(inteiro)}")
    
    # Pergunta ao usuário se deseja continuar
    continuar = input('Deseja continuar? (sim/não): ').lower()
    # Se a resposta não for 'sim', o programa encerra
    if continuar != 'sim':
        print('PROGRAMA ENCERRADO!')
        break
    
    
# OUTRA FORMA
    
    
# Define uma função chamada isinteiro que recebe uma string s e retorna um valor
                                                     # booleano (True ou False). 
def isinteiro(s: str) -> bool:
    
    #Define uma string contendo todos os caracteres que são dígitos válidos.
    digito = "0123456789"
    
    #Assume inicialmente que a string s é válida.
    valido = True # True
    
    #Verifica se o primeiro caractere de s é um sinal de mais +, menos -, ou um
               # dígito. Se sim, prossegue para verificar os outros caracteres;
               # caso contrário, marca valido como False
    if s[0] in "+-" or s[0] in digito:
    #    False      or True    
    
        # Itera sobre cada caractere na string s, começando do segundo caractere 
                                             # (índice 1) até o final da string.
        for i in range (1, len(s)):
            
            
            # Dentro do loop, verifica se cada caractere não é um dígito. 
            # Se encontrar um caractere não numérico, define valido como False
            # e interrompe o loop (break).
            if s[i] not in digito:
                valido = False
                break
            
    # Se o primeiro caractere não for +, - ou um dígito, define valido como False        
    else:
        valido = False
 
 
    # Retorna True se todos os caracteres foram válidos, caso contrário, retorna False
    return valido

#_______________________________________________________________________________
 
# print(isinteiro("j1234")) # False
# print(isinteiro("99")) # True
# print(isinteiro("-45")) # True
# print(isinteiro("+44.")) # False
# print(isinteiro("+232")) # True
# if isinteiro("345"):
#     print("é inteiro")
# else:
#     print("não é inteiro"


'''
Faça um função isfloat(string) que pegue uma string passada por parâmetro e
retorne True caso esta string represente um valor float ou False caso não
seja




->              PROGRAMA PRINCIPAL

        resp = isfloat('Edson)
        >> False
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