# Operadores relacionais

"""
Operadores relacionais
Igual: ==
Diferente: !=
Menor que: <
Maior que: >
Menor ou igual: <=
Maior ou igual: >=
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print(f"{num1} é igual a {num2}")
elif num1 != num2:
    print(f"{num1} é diferente de {num2}")
elif num1 < num2:
    print(f"{num1} é menor que {num2}")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 <= num2:
    print(f"{num1} é menor ou igual a {num2}")
elif num1 >= num2:
    print(f"{num1} é maior ou igual a {num2}")
else:
    print("Erro")