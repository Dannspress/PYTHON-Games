import random
from time import sleep
Nome = str(input('Olá! Como você se chama? '))
print('Prazer, {}! Vamos jogar JOKENPÔ?'.format(Nome))

print('--' * 20)
print('J O K E N P Ô')
print('--' * 20)
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
op = int(input('Escolha: '))

jogadas = ['pedra', 'papel', 'tesoura']
P2 = random.choice(jogadas)

if op == 1 or op == 2 or op == 3:
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
    P2 = random.choice(jogadas)
    if op == 1:
        print('Jogador escolheu: PEDRA')
    elif op == 2:
        print('Jogador escolheu: PAPEL')
    else:
        print('Jogador escolheu: TESOURA')
else:
    print('OPÇÃO INVÁLIDA!')

print('O computador escolheu...')
sleep(3)
print('{}!'.format(P2))
print('--' * 20)

if op == 1 and P2 == 'PAPEL':
    print('DEU PERDEU!')
elif op == 1 and P2 == 'TESOURA':
    print('VOCÊ VENCEU!')
elif op == 2 and P2 == 'TESOURA':
    print('VOCÊ PERDEU!')
elif op == 2 and P2 == 'PEDRA':
    print('VOCÊ VENCEU!')
elif op == 3 and P2 == 'PEDRA':
    print('VOCÊ PERDEU!')
elif op == 3 and P2 == 'PAPEL':
    print('VOCÊ GANHOU!')
else:
    print('DEU EMPATE!')
