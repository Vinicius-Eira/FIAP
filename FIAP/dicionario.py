dicionario = {
    "nome":"Edson",
    "idade": 30
}
import os
os.system("cls")
os.system("cls")
print(dicionario)

if dicionario.get("salario"):
    print("Existe")
else:
    print("nao existe")

print(list(dicionario.keys()))
print(dicionario.values())
print(dicionario.items())

print("Mostrando as chaves:")
for k in dicionario.keys():
    print(k)

print("Mostrando os valores:")
for v in dicionario.values():
    print(v)

print("Mostrando ambos:")
for k,v in dicionario.items():
    print(f"{k} -> {v}")

"""
os.system("cls")
dicionario2 = dict()
print (dicionario2)

dicionario2["Nome"] = input("Nome: ")
dicionario2["idade"] = int(input("Idade:"))
dicionario2["Idade"] = int(input("Idade:"))

del dicionario2["Idade"]

print(dicionario2)
"""
