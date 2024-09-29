import os


# resp = "s"
# while resp == "s":
#     resp = input("Continuar? <s>im ou <n>ão? ")
#     if resp == "n":
#         break

#     if resp != 's' and resp != 'n':
#         print("Amigão, digite s ou n!")
#         resp = 's'
#         continue

#     if resp == "s":
#         print("Bom dia")
# else: # executa o else somente se o laço não for interrompido
#     print("Terminou o programa!")



opcao = 's'

while opcao == 's':
    os.system("cls")
    # ########################################### trecho que será repetido
    inicio = int(input("Inicio: ")) # 4
    fim = int(input("Fim: ")) # 16

    # limite de 10

    while inicio <= fim:
        print(f"{inicio} ", end='') # 4 5 6
        if inicio == 10:
            break
        inicio += 1
    else:    
        print("\n\nObrigado por utilizar o nosso sistema.")
        print("Todos os direitos são reservados.\n\n")    
    # ########################################### trecho que será repetido
    
 



    