N = int(input('Digite o número que deseja saber a tabuada: '))

print('T A B U A D A:')
print('--'*20)
for i in range(1, 11):
    mlt = i * N
    print('{} x {:2} = {}'.format(N , i, mlt))
