from random import randint
from time import sleep

Nome = input('Olá! Como você se chama? ').upper()
print('Prazer, {}! Eu irei sortear um número, você consegue adivinhar qual? '.format(Nome))

num = randint(0, 5)

print('-==-' * 20)
tent = 0
while tent != num:
     tent = int(input('De 0 a 5, que número foi sorteado? '))
     print('LOADING...')
     sleep(2)
     if tent != num:
        print('Você colocou {}? ERRADO! Tente de novo:'.format(tent, num))
     elif tent == num:
        print('Você colocou {}? PARABÉNS! Você venceu!'.format(tent))