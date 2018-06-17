class Convidado():
    nome = ''
    _idade = 0

    def set_idade(self, idade):
        if idade >= 18:
            self._idade = idade
            print('Entrada Liberada, boa festa!!!')
        else:
            print('Você não tem permissão para entrar nessa festa!!!')
