""" Modularização é o processo de dividir um programa em partes menores e mais gerenciáveis, chamadas de módulos.
Cada módulo é responsável por uma parte específica do programa, o que torna o código mais organizado, 
facil de entender e fácil de reutilizar e manter.
Em Python, um módulo é simplesmente um arquivo que contém definições de funções, classes e variáveis.
Para criar um módulo, basta criar um arquivo com a extensão `.py` e definir as funções, classes e variáveis 
que você deseja exportar para o módulo dentro dele. Para usar um módulo em outro arquivo, você pode importá-lo 
usando a palavra-chave `import`.
"""

# Exemplo de módulo (arquivo: saudacao.py)
def saudacao():
    print("Olá! Bem-vindo ao curso de Python!")