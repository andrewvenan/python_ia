# Condiçoes

"""
if: Se o resultado da condição for verdadeira, o bloco de código dentro do if será executado
elif: Se o resultado da condição for falsa, o bloco de código dentro do elif será executado
else: Se nenhuma das condições anteriores for verdadeira, o bloco de código dentro do else será executado
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))      
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num1} é menor que {num2}")
else:
    print(f"{num1} é igual a {num2}")   