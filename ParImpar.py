import random
wins = s = sPI = 0
while True:
    n = int(input('Que número você escolhe? '))
    PI = str(input('PAR OU ÍMPAR? ').upper())
    print('=='*20)

    CPU = random.randint(0, 10)

    s = CPU + n
    sPI = s % 2

    if sPI == 0 and PI == 'PAR':
        print(f'Deu {s}!')
        print('VOCÊ VENCEU!')
        print("--"*20)
        wins += 1
    elif sPI != 0 and (PI == 'ÍMPAR' or PI == 'IMPAR'):
        print(f'Deu {s}!')
        print('VOCÊ VENCEU!')
        print("--" * 20)
        wins += 1
    else:
        print(f'Deu {s}!')
        print('VOCÊ PERDEU!')
        print('--'*20)
        print(f'Você venceu {wins} jogo(s) seguido(s)!')
        print('--'*20)
        break