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