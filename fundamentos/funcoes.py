# Funçoes

""""
Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem
organizar o código, melhorar a legibilidade e facilitar a manutenção. Em Python, as funções são definidas usando 
a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter parâmetros.
"""
# Exemplo de função sem parâmetros
def saudacao():
    print("Olá! Bem-vindo ao curso de Python!")

# Chamando a função
saudacao()  # Saída: Olá! Bem-vindo ao curso de Python!

# Exemplo de função com parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso de Python!")

# Chamando a função com um argumento
saudacao_personalizada("Andrew")  # Saída: Olá, Andrew! Bem-vindo ao curso de Python!


# Exemplo de função com retorno
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # Saída: 8