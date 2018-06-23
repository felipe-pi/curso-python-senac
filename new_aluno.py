from alunoo import Aluno

aluno1 = Aluno(nome="Felipe", nome_mae="Dona Maria")#instanciando aluno

aluno1.set_idade(29)

aluno1.endereco = "Quadra I Cs. 28"
aluno1.matricula = "TMA10"
aluno1.serie = "6ª serie"

print('Nome:', aluno1.nome)
print('Idade', aluno1.idade)
print('Nome da mãe:', aluno1.nome_mae)
if aluno1.nome_pai is not None:
    print('Nome do Pai:', aluno1.nome_pai)

print('Endereço:', aluno1.endereco)
print('Matricula:', aluno1.matricula)
print('Matricula:', aluno1.serie)
aluno1.estudar()
aluno1.dormir()
