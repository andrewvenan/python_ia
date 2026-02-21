# f-string 

"""
As f-strings, ou formatted string literals, são uma maneira conveniente e eficiente de 
formatar strings em Python.
"""

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
salario = input("Digite seu salário: ")
status = input("Digite seu status: ")

print(f"Olá, {nome} {sobrenome}! Você tem {idade} anos, ganha {salario} e seu status é {status}.")