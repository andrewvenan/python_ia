# Listas, Dicionários e Tuplas

"""
Listas -> são mutáveis, ou seja, podemos alterar os seus elementos.
Podem ser alteradas (add, remove, modificar)
Usam colchetes []
Permitem itens repetidos
Podem misturar tipos de dados

lista.append()     # adiciona item
lista.remove()     # remove item pelo valor
lista.pop()        # remove pelo índice
lista.sort()       # ordena
len(lista)         # tamanho da lista
lista.clear()      # limpa a lista

#####################################

Dicionários -> são mutáveis, ou seja, podemos alterar os seus elementos.
Usam chaves { }
Estrutura chave → valor
Mutáveis
Não permitem chave repetida

dict.keys()      # retorna as chaves
dict.values()    # retorna valores
dict.items()     # chave + valor
dict.get()       # evita erro se chave não existir

######################################

Tuplas -> são imutáveis, ou seja, não podemos alterar os seus elementos.

Usam parênteses ()
Permitem repetição
Mais seguras (não podem ser modificadas)
Mais rápidas que listas

Quando usar tupla?
Coordenadas
Dados fixos
Configurações que não devem mudar

"""

# Listas
frutas = ["maçã", "banana", "uva"]

print(frutas[0])      # maçã
frutas.append("pera") # adiciona item
frutas[1] = "abacaxi" # altera item

print(frutas)

# Dicionários

aluno = {
    "nome": "Andrew",
    "idade": 32,
    "curso": "Python"
}

print(aluno["nome"])

aluno["nota"] = 9.5 # adiciona nova chave-valor
aluno["idade"] = 33 # altera valor da chave existente
print(aluno)

# Tuplas

coordenadas = (10, 20)
print(coordenadas[0])
# coordenadas[0] = 15 # isso causará um erro, pois tuplas são imutáveis
# coordenadas[0] = 50  # ERRO (imutável)

# Exemplo Prático (Misturando Tudo)

clientes = [
    {"nome": "João", "cidade": "Betim"},
    {"nome": "Maria", "cidade": "Contagem"}
]

print(clientes[0]["nome"])