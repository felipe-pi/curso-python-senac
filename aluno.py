class Aluno():
    _nome = 'Felipe'# para colocar o atributo privado usa-se "_" é convenção
    _idade = 36
    _endereco = 'Teresina/PI'

    def set_idade(self, idade):
        if idade >0:
            self._idade = idade