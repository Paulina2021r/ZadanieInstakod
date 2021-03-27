import random

print('Witam w grze Orzeł czy Reszka')
zaczynamy = input('kliknij enter aby zaczęć')
y = 'Tak'

a = 'orzeł' #1
b = 'reszka' #2

while y != 'Nie':
    x = random.randint(1, 2)
    if x == 1:
        print('Orzeł')
    else:
        print('Reszka')
    y = input('czy chcesz wylosować jeszcze raz odpowiedz Tak/Nie')
