import random


imie = input('Podaj swoje Imię: ')
print('Cześć ', imie,
      '. Miło cię poznać, zagrasz teraz w grę, w której Twoim zadaniem będzie zgadnąć o jakiej liczbie od 1 do 100 myśli komputer')

print('W takim razie zaczynajmy!')

gra = 'Tak'


while gra != 'Nie':
    liczba = random.randint(1, 100)
    x = int(input('podaj liczbę od 1 do 100: '))
    liczba_prob = 1

    while x != liczba:
        if x < liczba:
            x = int(input('Podaj większą liczbę: '))
            liczba_prob += 1  # można to zapisać liczba_prob = liczba_prob + 1
        if x > liczba:
            x = int(input('Podaj mniejszą liczbę: '))
            liczba_prob += 1

    if x == liczba:
        print('Brawo zgadłeś, ta liczba to: ', x, '. Zgadłeś w ', liczba_prob, 'próbach')
        gra = input('Czy chcesz zagrać jeszcze raz, wybierz Tak/Nie ')

    #if gra != 'Nie' or gra != 'Tak':
        #gra = 'Nie'


print('Miło było zagrać do zobaczenia następnym razem!')





