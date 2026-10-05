# listas
nomes = ["Lira", "Gui", "Thalia"]
numeros = [1, 2, 3, 4, 5]

# pegar uma informação da lista
primeiro = nomes[0]
print(primeiro)

# adicionar um item na lista
nomes.append("Michely")
print(nomes)

# dicionarios
pessoa = {"nome": "Lira", "idade": 25, "cidade": "São Paulo", "peso": 70}

peso = pessoa["peso"]
print(peso)

## como vamos usar
lista_mensagens = []

mensagem1 = {"role": "user", "content": "fala galera"}
mensagem2 = {"role": "assistant", "content": "resposta da IA"}

lista_mensagens.append(mensagem1)
lista_mensagens.append(mensagem2)

print(lista_mensagens)