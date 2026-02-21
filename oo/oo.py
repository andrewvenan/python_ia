# Orientação a Objetos

"""
Orientação a Objetos é um paradigma de programação que organiza o código em torno de "objetos", que são 
instâncias de "classes". Uma classe é uma estrutura que define as propriedades (atributos) e comportamentos 
(métodos) que os objetos criados a partir dela terão.

self é uma convenção em Python que se refere à instância atual da classe. Ele é usado para acessar os atributos 
e métodos da classe dentro de seus próprios métodos. Quando um método é chamado em um objeto, o objeto é passado 
automaticamente como o primeiro argumento para o método, e esse argumento é referenciado como self dentro do 
própriométodo.
""" 

# Definindo uma classe
class Casa:
    def __init__(self, cor, tamanho, quartos):
        self.cor = cor  # Atributo de instância
        self.tamanho = tamanho  # Atributo de instância 
        self.quartos = quartos  # Atributo de instância
        self.quartos += 1  # Incrementa o número de quartos
        
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor  # Altera o atributo cor
        print(f"A cor da casa foi alterada para {self.cor}.")
        
    def mostrar_informacoes(self):
        print(f"A casa é {self.cor} e tem {self.tamanho} metros quadrados e {self.quartos} quartos.")
        
        
        
# Criando um objeto (instância) da classe Casa
minha_casa = Casa("azul", 120, 3)
minha_casa2 = Casa("vermelha", 150, 4)
minha_casa3 = Casa("verde", 200, 5)

# Chamando um método do objeto
print('\nminha_casa: ')
minha_casa.mostrar_informacoes()  # Saída: A casa é azul e tem 120 metros quadrados.
print('\nminha_casa2: ')
minha_casa2.mostrar_informacoes()  # Saída: A casa é vermelha e tem 150 metros quadrados.
print('\nminha_casa3: ')
minha_casa3.mostrar_informacoes()  # Saída: A casa é verde e tem 200 metros quadrados.
        