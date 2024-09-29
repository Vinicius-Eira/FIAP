import os
os.system("cls")

# ------- Cadastrar os candidatos
#             0   1   2
candidatos = ["", "", ""]
print("Digite os nomes dos candidatos:")
for i in range(3):
    candidatos[i] = input(f"{i + 1}. ")

# ------- Votação
cand1 = cand2 = cand3 = nulo = 0
margem = ' ' * 4
while True:
    os.system("clear")
    print(f"""
    CANDIDATOS

    1 - {candidatos[0]}
    2 – {candidatos[1]}
    3 – {candidatos[2]}
    0 – FIM DA VOTAÇÃO 
    """)
    voto = int(input(margem + "VOTO: "))
    match voto:
        case 0:
            break
        case 1:
            cand1 = cand1 + 1
        case 2:
            cand2 = cand2 + 1
        case 3:
            cand3 = cand3 + 1
        case _:
            nulo = nulo + 1   

# ------- Apuração
total_votos = cand1 + cand2 + cand3 + nulo
if total_votos > 0:
    perc1 = cand1 / total_votos * 100
    perc2 = cand2 / total_votos * 100
    perc3 = cand3 / total_votos * 100
    perc_nulo = nulo / total_votos * 100
else:
    perc1 = perc2 = perc3 = perc_nulo = 0

print(f"""
CANDIDATOS
TOTAS DE VOTOS: {total_votos}
1 – {candidatos[0]:15} -> {cand1:3d} votos -> {perc1:5.1f}%
2 – {candidatos[1]:15} -> {cand2:3d} votos -> {perc2:5.1f}%
3 – {candidatos[2]:15} -> {cand3:3d} votos -> {perc3:5.1f}%
    {"NULOS":15} -> {nulo:3d} votos -> {perc_nulo:5.1f}% 
""")


#_______________________________________________________________________________



# -> Utilizado Funções <-

os.system("cls")

# ======================== SUBALGORITMOS
# ------- Procedimento (não retorna valor)
def preenche_vetor(c: list) -> None:
    print("Digite os nomes dos candidatos:")
    for i in range(3):
        c[i] = input(f"{i + 1}. ")

def exibir_menu(c: list) -> None:
    print(f"""
    CANDIDATOS

    1 - {c[0]}
    2 – {c[1]}
    3 – {c[2]}
    0 – FIM DA VOTAÇÃO 
    """)

# ------- Função (retorna valor)
def acresc(cont_voto: int) -> int:
    return cont_voto + 1

def somatoria(c1: int, c2: int, c3: int, c4: int) -> int:
    return c1 + c2 + c3 + c4


def porcentagem(v: int, tv: int) -> float:
    return v / tv * 100

# ======================== PROGRAMA PRINCIPAL



# ------- Cadastrar os candidatos
#             0   1   2
candidatos = ["", "", ""]

preenche_vetor(candidatos) # *******************************************************

# ------- Votação
cand1 = cand2 = cand3 = nulo = 0
margem = ' ' * 4
while True:
    os.system("clear")

    exibir_menu(candidatos) # *******************************************************

    voto = int(input(margem + "VOTO: "))

    match voto:
        case 0:
            break
        case 1:
            cand1 = acresc(cand1)
        case 2:
            cand2 = acresc(cand2)
        case 3:
            cand3 = acresc(cand3)
        case _:
            nulo = acresc(nulo)  

# ------- Apuração
total_votos = somatoria(cand1, cand2, cand3, nulo)
if total_votos > 0:
    perc1 = porcentagem(cand1, total_votos)
    perc2 = porcentagem(cand2, total_votos)
    perc3 = porcentagem(cand3, total_votos)
    perc_nulo = porcentagem(nulo, total_votos)
else:
    perc1 = perc2 = perc3 = perc_nulo = 0

# fazer um procedimento que exiba esta aputação
print(f"""
CANDIDATOS
TOTAS DE VOTOS: {total_votos}
1 – {candidatos[0]:15} -> {cand1:3d} votos -> {perc1:5.1f}%
2 – {candidatos[1]:15} -> {cand2:3d} votos -> {perc2:5.1f}%
3 – {candidatos[2]:15} -> {cand3:3d} votos -> {perc3:5.1f}%
    {"NULOS":15} -> {nulo:3d} votos -> {perc_nulo:5.1f}% 
""")