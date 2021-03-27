import pygame
import random  # generacja losowej liczby

# rozpoczęcie gry
pygame.init()

# tworzenie ekranu gry
screen = pygame.display.set_mode((800, 600))  # szerokość, wysokość

# nazwa gry
pygame.display.set_caption('ZgadnijLiczbę')








# Moje
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
            liczba_prob += 1
        if x > liczba:
            x = int(input('Podaj mniejszą liczbę: '))
            liczba_prob += 1

    if x == liczba:
        print('Brawo zgadłeś, ta liczba to: ', x, '. Zgadłeś w ', liczba_prob, 'próbach')
        gra = input('Czy chcesz zagrać jeszcze raz, wybierz Tak/Nie ')

print('Miło było zagrać do zobaczenia następnym razem')