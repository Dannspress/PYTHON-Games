import random
from time import sleep
Nome = str(input('Olá! Como você se chama? ').upper())
print('Prazer, {}! Vamos jogar JOKENPÔ?'.format(Nome))

print('--' * 20)
print('J O K E N P Ô -Plus-')
print('--' * 20)
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
print('4 - LAGARTO')
print('5 - SPOCK')
op = int(input('Escolha: '))

if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK']
    P2 = random.choice(jogadas)
    if op == 1:
        print('Jogador escolheu: PEDRA')
    elif op == 2:
        print('Jogador escolheu: PAPEL')
    elif op == 3:
        print('Jogador escolheu: TESOURA')
    elif op == 4:
        print('Jogador escolheu: LAGARTO')
    else:
        print('jogador escolheu: SPOCK')
else:
    print('OPÇÃO INVÁLIDA!')

print('O computador escolheu...')
sleep(3)
print('{}!'.format(P2))
print('--' * 20)

if op == 1 and (P2 == 'PAPEL' or P2 == 'SPOCK'):
    print('VOCÊ PERDEU!')
elif op == 1 and (P2 == 'TESOURA' or P2 == 'LAGARTO'):
    print('VOCÊ VENCEU!')
elif op == 2 and (P2 == 'TESOURA' or P2 == 'LAGARTO'):
    print('VOCÊ PERDEU!')
elif op == 2 and (P2 == 'PEDRA' or P2 == 'SPOCK'):
    print('VOCÊ VENCEU!')
elif op == 3 and (P2 == 'PEDRA' or P2 == 'SPOCK'):
    print('VOCÊ PERDEU!')
elif op == 3 and (P2 == 'PAPEL' or P2 == 'LAGARTO'):
    print('VOCÊ GANHOU!')
elif op == 4 and (P2 == 'TESOURA' or P2 == 'PEDRA'):
    print('VOCÊ PERDEU!')
elif op == 4 and (P2 == 'PAPEL' or P2 == 'SPOCK'):
    print('VOCÊ GANHOU')
elif op == 5 and (P2 == 'LAGARTO' or P2 == 'PAPEL'):
    print('VOCÊ PERDEU!')
elif op == 5 and (P2 == 'PEDRA' or P2 == 'TESOURA'):
    print('VOCÊ GANHOU')
else:
    print('DEU EMPATE!')
