import random
import os
from itertools import count
from operator import indexOf

"""
    zasady gry w kosci :>
    gracz rzucza tak dlugo dopuki nie uzyska 0 punktow z rzutu
    gracz moze zachowac kosci, jezeli straci ture to traci tez punkty uzyskane w danej turze
    gracz po kazdym rzucie moze zakonczyc ture 
    gra trwa tak dlugo dopuki ktos nie uzyska celu punktow
    
    liczba oczek = punkty:
    1 = 100 pkt, 5 = 50 pkt
    Trójki: 1 = 1000 pkt, inne liczby = liczba * 100
"""

liczba_graczy = 2
cel_punktow = 5000
punkty_graczy = list()# bedzie przechowywac punkty graczy


def menu_glowne():
    wiadomosc = ""
    while True:
        print("****************************\n             Gra w kości             \n****************************")
        print("----------------------------\n1 - start\n2 - ustawienia\n3 - wyjście")
        if len(wiadomosc) != 0: print(wiadomosc)
        menuSel = int(input(": "))
        wiadomosc = ""
        os.system("cls")
        if menuSel == 1:
            start()
            menuSel = 0
        elif menuSel == 2:
            ustawienia()
        elif menuSel == 3:
            break
        else: wiadomosc = "Podano błędną liczbę"


def ustawienia():
    global liczba_graczy, cel_punktow
    while True:
        print("******* USTAWIENIA *******")
        print("liczba graczy:",liczba_graczy)
        print("ilosc punktow do wygrania:", cel_punktow)
        print("-------------------------------")
        print("1 - zmiana liczby graczy\n2 - zmiana ilosci punktow do wygranej\n3 - wyjscie")
        wybor = int(input(": "))
        if wybor == 1:
            while True:#petla do wprowadzenia odpowiedniej liczby graczy
                print("Wprowadz liczbe graczy(2-4)")
                num_of_players = int(input(": "))
                if num_of_players >= 2 and num_of_players <= 4:
                    liczba_graczy = num_of_players
                    break
            break
        elif wybor == 2:
            while True:#petla do wprowadzenia odpowiedniej liczby graczy
                print("Wprowadz liczbe punktow do wygrania(1000-10000)")
                to_win = int(input(": "))
                if to_win >= 1000 and to_win <= 10000:
                    cel_punktow = to_win
                    break
            break
        elif wybor == 3:
            break


def start():
    global punkty_graczy
    wygrany = 0
    punkty_graczy = [0 for i in range(0, liczba_graczy)]
    while wygrany == 0 :
        for i in range(0,liczba_graczy):
            if wygrany != 0: return
            print("Runda gracza ",i+1," ma ",punkty_graczy[i]," punktow")
            instrukcja()
            rozgrywka(i)
        for i in range(0,liczba_graczy):
            if punkty_graczy[i] >= cel_punktow:
                wygrany = i
                break
    print("Wygrał gracz",wygrany)






def rozgrywka(id):
    punkty = rzut()

    print("Gracz",id+1,"zdobyte punkty:",punkty,"| posiadane punkty(bezpieczne):",punkty_graczy[id])

    if punkty == 0: return
    else: punkty_graczy[id] += punkty
    if punkty >= cel_punktow: return

    while True:
        print("chcesz grac dalej?(t/n)")
        want_play = input(": ")
        if want_play == "n": return
        elif want_play == "t": break
        else: print("blad")

    while True:
        print("ile chcesz rzucic kosci(1-6)")
        dice = int(input(": "))
        if dice >= 1 and dice <= 6:
            break
    rozgrywka(id)
    return

def rzut():
    punkty = 0
    kosci = [random.randint(1, 6) for i in range(0, 6)]  # rzut 6sciu kosci
    for i in kosci:  # dodawanie punktow na bazie jednego oczka
        if i == 1:
            punkty += 100
        elif i == 5:
            punkty += 50
    for i in kosci:
        if kosci.count(i) == 3:
            if i == 1:
                punkty += 1000
            else:
                punkty += i * 100
    return punkty

def instrukcja():
    print("***** Informacje pomocnicze: \n zasady gry w kosci :> \n"
          "gracz rzucza tak dlugo dopuki nie uzyska 0 punktow z rzutu\n"
          "gracz moze zachowac kosci, jezeli straci ture to traci tez punkty uzyskane w danej turze\n"
          "gracz po kazdym rzucie moze zakonczyc ture \n"
          "gra trwa tak dlugo dopuki ktos nie uzyska celu punktow\n"
          "liczba oczek = punkty:\n"
          "1 = 100 pkt, 5 = 50 pkt\n"
          "Trójki: 1 = 1000 pkt, inne liczby = liczba * 100 np. 2,3,3,3,6,4 punkty 300")

menu_glowne()