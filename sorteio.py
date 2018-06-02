from random import randint

num_sorteado = randint(1, 10)

tenta = 1
lista_digitados = []

while tenta <= 3:
    tenta = tenta + 1
    num_digitado = int(input('Digite seu numero sorteado entre 1 e 10:'))
    lista_digitados.append = numero_digitado
    if num_digitado == num_sorteado:
        print('Que legal hoje é seu dia de sorte!\n Passe no caixa para receber seu prêmio.')
    elif num_digitado < num_sorteado:
        print ('O numero sorteado é menor que',format(lista_digitados[tenta]))
    elif num_digitado > num_sorteado:
        print ('O numero sorteado é maior que',format(lista_digitados[tenta-1])
    else:
        print('Lamento mas seu numero não foi sorteado')
        

            
                
