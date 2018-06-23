from pessoa import Pessoa

class Aluno(Pessoa):
    
    matricula = ""
    serie = ""

    def estudar(self):
        print('Hora de estudar...')
    def dormir(self):
        print('Hora de dormir as 22h...')
    #comportamentos e Metodos