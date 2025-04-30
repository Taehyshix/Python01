from biblioteca import estoque
produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade no estoque: "))

estoque(produto,quantidade,valor)
