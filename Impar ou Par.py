from random import randint
from time import sleep
v = 0
while True:
    jogador = int(input('Valor desejado: [0 a 10] '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
        print(f'Jogador digitou {jogador} e computador {computador} a soma vale {total}')
        print('_'*18)
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador VENCEU!')
            v += 1
        else:
            print('Jogador PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Jogador GANHOU!')
            v += 1
        else:
            print('Jogador PERDEU!')
            break
print('Finalizando...')
sleep(2)
print('OBRIGADO POR JOGAR :)')