class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade 
        self.cargo = cargo
    
    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
    
    def promover(self, novo_cargo):
        print(f'{self.nome} foi promovido(a) para {novo_cargo}.')    

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'{self.nome} agora tem {nova_idade} anos.')
        else:
            print(f'Idade inválida. A idade de {self.nome} permanece {self.idade} anos.')    

       
        
colaborador1 = Pessoa('Ane', 28, 'Confeiteira')
colaborador2 = Pessoa('Andrew', 32, 'Suporte Técnico')

colaborador1.informacoes()
colaborador1.promover('Gerente de Confeitaria')
colaborador1.atualizar_idade(25)
