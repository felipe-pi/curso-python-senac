from pessoa import Pessoa 

class Funcionario(Pessoa):
    matricula = ""
    cargo = ""
    atividade = ""
    
    def __init__(self, nome, matricula):
        pass

    # def __init__ super(Pessoa):
    #     pass

    def trabalha(self, atividade):
        if atividade == 1:
            return print("Funcionario trabalhando...")
        elif atividade == 0:
            return print("Funcionário fora do expediente...")
        else:
            print("Error")

