import random, time

def Gra():
    wybory = ("papier", "kamień", "nożyce")
    Gracz = None

    while Gracz not in wybory:
        wybór_komp = random.choice(wybory)
        Gracz = input("Wybierz papier kamień czy nożyce: ").lower()
        # Pierwszy przypadek
        if wybór_komp == Gracz:
            time.sleep(1)
            print(Gracz)
            time.sleep(1)
            print(wybór_komp)
            time.sleep(1)
            print("Remis !")
        # Drugi przypadek
        elif wybór_komp == ("kamień"):
            if Gracz == ("nożyce"):
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Przegrałeś !")
            else:
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Wygrałeś !")
        # Trzeci przypadek
        elif wybór_komp == ("nożyce"):
            if Gracz == ("papier"):
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Przegrałeś !")
            else :
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Wygrałeś !")
        # Czwarty przypadek
        elif wybór_komp == ("papier"):
            if Gracz == ("kamień"):
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Przegrałeś !")
            else:
                time.sleep(1)
                print(Gracz)
                time.sleep(1)
                print(wybór_komp)
                time.sleep(1)
                print("Wygrałeś !")

    time.sleep(1)
    print("Koniec gry !")
    return
while True:
    pytanie = input ("Czy chcesz zagrać w grę: ").lower()
    if pytanie == "tak":
        Gra()
    else:
        print ("Do widzenia")
        break










