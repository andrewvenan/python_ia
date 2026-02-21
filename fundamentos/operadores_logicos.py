# Operadores logicos

"""
Operadores logicos
E: and
Ou: or
Não: not
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))      
if num1 > 0 and num2 > 0:
    print("Ambos os números são positivos.")
elif num1 > 0 or num2 > 0:
    print("Pelo menos um dos números é positivo.")
elif not num1 > 0:
    print("O primeiro número não é positivo.")
elif not num2 > 0:
    print("O segundo número não é positivo.")
else:
    print("Nenhum dos números é positivo.")