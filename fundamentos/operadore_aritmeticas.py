# Calculos aritméticas

"""
Operadores aritméticas
Adição: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão inteira: //
Módulo: %
Exponenciação: **
Calculo de raiz quadrada: ** 0.5
(2+5)*10 = 70 O calculo é feito primeiro dentro dos parenteses, depois a multiplicação.
'A' * 5 = 'AAAAA' O operador de multiplicação também pode ser usado para repetir strings.
'A'+ 3 = 'A3' O operador de adição pode ser usado para concatenar uma string com um número, convertendo o número em string.
'A'+'B' = 'AB' O operador de adição pode ser usado para concatenar strings.
2.5 % 2 = 1 O operador de módulo retorna o resto da divisão de 2.5 por 2, que é 1.
2.5 // 2 = 1 O operador de divisão inteira retorna o quociente da divisão de 2.5 por 2, que é 1.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma de {num1} e {num2} é: {soma}")
subtracao = num1 - num2
print   (f"A subtração de {num1} e {num2} é: {subtracao}")
multiplicacao = num1 * num2     
print(f"A multiplicação de {num1} e {num2} é: {multiplicacao}")
divisao = num1 / num2
print(f"A divisão de {num1} e {num2} é: {divisao}")
divisao_inteira = num1 // num2
print(f"A divisão inteira de {num1} e {num2} é: {divisao_inteira}")
modulo = num1 % num2
print(f"O módulo de {num1} e {num2} é: {modulo}")
exponenciacao = num1 ** num2
print(f"A exponenciação de {num1} e {num2} é: {exponenciacao}")
raiz_quadrada = num1 ** 0.5
print(f"A raiz quadrada de {num1} é: {raiz_quadrada}")