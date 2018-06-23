from maioridade import Convidado

maioridade1 = Convidado()

maioridade1.set_idade(int(input('Qual a sua idade?')))
if(maioridade1._idade >= 18):
    print("VOCE PODE ENTRAR")   
else:
    print('VOCE NAO PODE ENTRAR')

