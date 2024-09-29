import os
os.system("cls")


inicio = int(input("Inicio: ")) # 4
fim = int(input("Fim: ")) # 16

# limite de 10

while inicio <= fim:
    print(f"{inicio} ", end='') # 4 5 6
    if inicio == 10:
        break
    inicio += 1
else:    
    print("\nObrigado por utilizar o nosso sistema.")
    print("Todos os direitos são reservados.")
# inicio    fim
# 4         6
# 5
# 6
# 7


'''
# Ler o valor inicial - NÃO
inicio = int(input("Inicio: "))
# Ler o valor final - NÃO
fim = int(input("Fim: "))

# ------------------------ inicio do laço
while inicio <= fim:
    # Exibir os números - SIM
    print(inicio)
    # Somar 1 para o próximo número - SIM
    inicio = inicio + 1
# ------------------------ final do laço
'''