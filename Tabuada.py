while True:
    n = int(input('De qual número você quer a tabuada? (NEGATIVO para sair) '))
    print('--'*20)
    if n < 0:
        break

    print('T A B U A D A')
    print('--'*20)

    for i in range(1, 11):
        r = i * n
        print(f'{n:<2} X {i:>2} = {r:>2}')
        i += 1

    print('=='*20)