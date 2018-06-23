class Pessoa():
    nome = ""
    endereco = ""
    idade = 0
    nome_mae = ""
    nome_pai = ""

    
    def __init__(self, nome, nome_mae, nome_pai=None):# init é um contrutor - None dado "null"
        self.nome = nome
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
    
    def dormir(self):
        print('Hora de dormir...')
        
    def caminhar(self):
        print('Caminhando...')

    def comer(self):
        print('Hora de comer...')

    def set_idade(self, idade):
        if idade>0:
            self.idade = idade
    
        
    