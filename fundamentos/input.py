# input - Recebendo informações do usuário

""" 
Em Python, você pode usar a função input() para receber informações do usuário. 
A função input() exibe uma mensagem para o usuário e espera que ele digite algo. 
O valor digitado pelo usuário é retornado como uma string. 
Aqui está um exemplo de como usar a função input() para receber informações do usuário:
"""

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
salario = input("Digite seu salário: ")
status = input("Digite seu status: ")

print("Olá, " + nome + " " + sobrenome + "! Você tem " + idade + " anos, ganha " + salario + " e seu status é " + status + ".")
