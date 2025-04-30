def imprime_nome(nome):
    print(f"Nome: {nome}")
def solicite_nome():
    nome = input("Digite seu nome: ")
    return nome
def piramide(num):
    for x in range(1, num + 1, 1):
        for i in range(0, x):
            print(x, end=" ")
        print()
def conta_vogais (texto):
    cont = 0
    for x in range(len(texto)):
        if texto[x] in "aeiouAEIOU":
            cont = cont+1
    print(cont)
def estoque (produto, quantidade, valor):
    calculo = quantidade * valor
    print(f"Você tem R${calculo} de {produto} no seu estoque.")

def numero (num):
    if num != 0:
        if num>0:
            return "P"
        else: "N"
    else:
        return "Z"