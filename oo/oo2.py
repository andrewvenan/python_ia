"""
Classes e Objetos 
Exemplo de classe Carro com atributos e métodos para ligar, desligar e ligar a seta. A seta só 
pode ser ligada se o carro estiver ligado.
"""

class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = True
        self.seta = None # Atributo para indicar a direção da seta (esquerda, direita ou None) None significa que a seta está desligada
    
    def informacoes(self):
        print(f'A cor do carro e {self.cor}')
        print(f'O ano do carro e {self.ano}')
        
    def ligar(self):
        if not self.ligado: # Verifica se o carro não está ligado antes de ligar
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro ja esta ligado')  
        
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro ja esta desligado')    
            
    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro :) ')
            return # Sai da função para evitar ligar a seta quando o carro está desligado
        
        self.seta = direcao
        print(f'A seta foi ligada para a {self.seta}')
                
carro1 = Carro('Preto', 2021)
carro1.informacoes()
carro1.ligar()
carro1.ligar_seta('esquerda')
        
    