from Labirynt import Labirynt
from Gracz import Gracz
from Przejscie import Przejscie
from Krasnolud import Krasnolud
from Elf import Elf
from Troll import Troll
from Goblin import Goblin
from Zlotamoneta import Zlotamoneta
from Zlotykielich import Zlotykielich
from Klucz import Klucz
from Miecz import Miecz
from Apteczka import Apteczka

import random


class Gra:

    def convertable_to_int(self, n):
        """
        Metoda ta zwraca, czy dana liczba jest konwertowalna na liczbe calkowita, czy tez nie (True or False).

        :param n: zmienna (docelowo int)

        :return:
                boolean
        """
        try:
            int(n)
            return True
        except ValueError:
            return False

    def convertable_to_float(self, n):
        """
        Metoda ta zwraca, czy dana liczba jest konwertowalna na liczbe rzeczywista, czy tez nie (True or False).

        :param n: zmienna (docelowo float lub int)

        :return:
                boolean
        """
        try:
            float(n)
            return True
        except ValueError:
            return False

    def required(self, N):
        """
        Metoda ta sprawdza, czy podana przez uzytkownika liczba jest z wlasciwego zakresu.

        :param N: liczba komnat (int)

        :return:
                boolean
        """
        if (20 >= N >= 10) or N == 5:
            return True
        else:
            return False

    def required_real(self, P, a, b):
        """
        Metoda ta sprawdza, czy podana przez uzytkownika liczba jest z wlasciwego zakresu.

        :param P: prawdopodobienstwo utworzenia poloczenia miedzy danymi komnatami (float)

        :param a: dolne ograniczenie danego zakresu

        :param b: gorne ograniczenie danego zakresu

        :return:
                boolean
        """
        if b >= P >= a:
            return True
        else:
            return False

    def command_entering(self, a, b):
        """
        Metoda ta wypisuje mozliwe do wprowadzenia przez uzytkownika polecenia.

        :param a: numer kolejki (int)

        :param b: identyfikator komnaty (int)

        :return:
                string
        """
        print(f"\n Aktualna kolejka to {a}. Jesteś w komnacie {b}. Zdecyduj proszę, co chcesz robić.")
        print("Możesz wprowadzić następujące komendy:"
              "a - sprawdzenie swojego stanu zdrowia, liczby oraz rodzaju sprzętu i posiadanych przedmiotów. \n"
              "b - uleczenie się (oczywiście jeśli posiadasz apteczkę, jeśli jesteś w pełni zdrowy polecenie nie "
              "działa.\n"
              "c - zobaczenie jaki stwór jest w komnacie, można decydować, czy się wchodzi z nim w interakcje. "
              "(elf może nas uleczyć, za pierwszym razem tylko o 10, później o 25 punktów zdrowia, "
              "u krasnoluda możemy naprawić miecz i dokonać zakupu, a z goblinem oraz trollem "
              "walczymy),\n"
              "gobliny sa sprytne - może Ci on coś ukraść, a Ty nawet go nie zobaczysz.\n"
              "d - wejście w interakcje ze stworem.     "
              "e - zobaczenie jaki obiekt jest w komnacie. \n"
              "f - zabranie z komnaty danego obiektu.   "
              "g - poznanie parametrów danej komnaty, tzn. jej numeru, połączeń oraz czy jest wyjściem. \n"
              "h - przejście do innej komnaty - koniec kolejki.     "
              "i - decyzja o wyjściu z labiryntu - jeśli możliwe - zwycięstwo! ")

    def play(self):
        """
        Metoda ta kontroluje gre.

        :return:
        """

        lista_komend = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        win = False

        print("Czy chcesz zagrać w grę labirynt? Jeśli tak wpisz 1, jeśli nie dowolną inną liczbę całkowitą.")

        liczba = input("Podaj liczbę: ")
        while Game.convertable_to_int(liczba) is not True:
            liczba = input("Podaj liczbę, 1 lub dowolną inną liczbę całkowitą: ")
        liczba = int(liczba)

        if liczba == 1:
            print("\nZaczynasz grę w labirynt. Twoim zadaniem jest wyjść z labiryntu w ciągu 20 kolejek zdobywając "
                  "przy tym 2 złote monety i 1 złoty kielich.\n Zaczynasz z komnaty nr. 1. Wyjście jest tylko w jednej "
                  "z wszystkich komnat. W każdej komnacie poza startową znajduje się stwór oraz przedmiot.\n")

            print("Rozpoczynam losowanie labiryntu oraz stanu początkowego gry, \n"
                  "podaj proszę następujące parametry lub wpisz 0, wtedy zostanie ustawiona domyślna wartość tego "
                  "parametru \n"
                  "lub wpisz 5 dla parametru N, wtedy dla każdego parametru zostanie ustalona domyślna wartość: \n"
                  "N – liczba naturalna od 10 do 20, która będzie liczbą komnat w labiryncie, (domyślnie 10)\n"
                  "P – prawdopodobieństwo połączenia między komnatami, wartości od 0,2 do 0,8, (domyślnie 0,4)\n"
                  "D – prawdopodobieństwo, że przejście to drzwi, wartości od 0,1 do 0,3, (domyślnie 0,2)")

            domyslne = False

            N = input("Podaj N: ")
            if self.convertable_to_int(N) is True:
                N = int(N)
            else:
                raise TypeError("N powinno być liczbą całkowitą.")
            if self.required(N) is not True:
                raise ValueError("Podano niewłaściwą wartość N.")
            if N == 5:
                N = 10
                P = 0.4
                D = 0.2
                domyslne = True
            else:
                if N == 0:
                    N = 10

            if domyslne is not True:
                P = input("Podaj P: ")
                if self.convertable_to_float(P) is True:
                    P = float(P)
                else:
                    raise TypeError("P powinno być liczbą rzeczywistą.")
                if self.required_real(P, 0.2, 0.8) is not True:
                    raise ValueError("Podano niewłaściwą wartość P.")
                if P == 0:
                    P = 0.4

                D = input("Podaj D: ")
                if self.convertable_to_float(D) is True:
                    D = float(D)
                else:
                    raise TypeError("D powinno być liczbą rzeczywistą.")
                if self.required_real(D, 0.1, 0.3) is not True:
                    raise ValueError("Podano niewłaściwą wartość D.")
                if D == 0:
                    D = 0.2

            L = Labirynt()
            G = Gracz()

            for i in range(N):
                L.add_room(i + 1)

            L.drawing_method(P, D)
            L.BFS_modificated(N, D)

            id_przedmiotu = 1
            for komnata in L:

                o = random.choices(["ZM", "ZK", "K", "M", "A"], [0.4, 0.2, 0.1, 0.2, 0.2])[0]
                s = random.choices(["K", "E", "T", "G"], [1/4, 1/4, 1/4, 1/4])[0]

                if s == "K":
                    komnata.stwor = Krasnolud("K", komnata.number)
                elif s == "E":
                    item = random.choice(["ZM", "ZK", "K", "M", "A"])
                    komnata.stwor = Elf("E", komnata.number, item)
                elif s == "T":
                    komnata.stwor = Troll("T", komnata.number)
                elif s == "G":
                    komnata.stwor = Goblin("G", komnata.number)

                if o == "ZM":
                    komnata.obiekt = Zlotamoneta(id_przedmiotu, "ZM", komnata.number)
                elif o == "ZK":
                    komnata.obiekt = Zlotykielich(id_przedmiotu, "ZK", komnata.number)
                elif o == "K":
                    komnata.obiekt = Klucz(id_przedmiotu, "K", komnata.number)
                elif o == "M":
                    komnata.obiekt = Miecz(id_przedmiotu, "M", komnata.number)
                elif o == "A":
                    komnata.obiekt = Apteczka(id_przedmiotu, "A", komnata.number)

                id_przedmiotu = id_przedmiotu + 1

            G.room_id = 1

            G.equipment.append(Miecz(id_przedmiotu, "M", None))
            id_przedmiotu = id_przedmiotu + 1

            L.rooms[1].stwor = None
            L.rooms[1].obiekt = None

            ls = []
            for i in range(N):
                ls.append(i + 1)
            wyjsciowa = random.choice(ls)
            wyjscie = Przejscie(wyjsciowa, False, True, L.id_tran, None)
            L.rooms[wyjsciowa].czy_wyjscie = True

            kolejka = 1
            aktywnosc = 1

            while kolejka < 21:

                if L.rooms[G.room_id].stwor is not None and aktywnosc == 1:
                    if L.rooms[G.room_id].stwor.type == "G":
                        l = random.random()
                        if l < 0.5:
                            L.rooms[G.room_id].stwor.steal(G.items)
                aktywnosc = 0

                Game.command_entering(kolejka, G.room_id)
                komenda = input("Podaj komende: ")
                while komenda not in lista_komend:
                    print("Nie istnieje taka komenda. Spróbuj ponownie.")
                    Game.command_entering(kolejka, G.room_id)
                    komenda = input("Podaj komende: ")

                if komenda == "a":
                    print(G)
                elif komenda == "b":
                    G.heal()
                elif komenda == "c":
                    if L.rooms[G.room_id].stwor is not None:
                        L.rooms[G.room_id].stwor.name()
                    else:
                        print("W danej komnacie nie ma żadnego stwora.")
                elif komenda == "d":
                    if L.rooms[G.room_id].stwor is None:
                        print("Nie można wejść w interakcje ze stworem, bo nie ma w tej komnacie stwora.")
                        continue
                    elif L.rooms[G.room_id].stwor.type == "T":

                        decyzja = "N"

                        m = False
                        for i in G.equipment:
                            if isinstance(i, Miecz):
                                m = True
                                break
                        if m:
                            decyzja = input("Zdecyduj, czy się blokujesz (bezpieczniejsze, ale mniejsza szansa \n"
                                            "na zadanie później obrażeń i miecz się niszczy), \n"
                                            "czy też robisz unik (mniej bezpieczne, ale większa szansa na zadanie "
                                            "później obrażeń).\n"
                                            "Jeśli blok - wpisz B (oczywiście jeśli masz miecz, jeśli unik - wpisz A: ")

                            while decyzja != "A" and decyzja != "B":
                                decyzja = input("Podaj poprawną komende.")
                        else:
                            print("Zaatakował Ciebie Troll, ale nie masz miecza, więc musisz zrobić unik.")
                            decyzja = "A"

                        d = L.rooms[G.room_id].stwor.attacks(decyzja)
                        if decyzja == "B":
                            for i in G.equipment:
                                if isinstance(i, Miecz):
                                    i.wytrzymalosc = i.wytrzymalosc - 3
                                    if i.wytrzymalosc <= 0:
                                        G.equipment.remove(i)
                                        print("Straciłeś miecz!")
                                    break
                            if d == "w":
                                G.health = G.health - 20
                                print("Straciłeś 20 punktów zdrowia!")
                                if G.health <= 0:
                                    print("Przegrałeś")
                                    break
                            if d == "d":
                                print("Nic się nie stało")
                            if d == "l":
                                L.rooms[G.room_id].stwor.health = L.rooms[G.room_id].stwor.health - 10
                                print("Troll zranił się własną maczugą i stracił 10 punktów zdrowia!")
                                if L.rooms[G.room_id].stwor.health <= 0:
                                    L.rooms[G.room_id].stwor = None
                                    print("Zabiłeś trolla!")

                        if decyzja == "A":
                            if d == "w":
                                G.health = G.health - 50
                                print("Straciłeś 50 punktów zdrowia!")
                                if G.health <= 0:
                                    print("Przegrałeś")
                                    break
                            if d == "l":
                                L.rooms[G.room_id].stwor.health = L.rooms[G.room_id].stwor.health - 10
                                print("Troll zranił się własną maczugą i stracił 10 punktów zdrowia!")
                                if L.rooms[G.room_id].stwor.health <= 0:
                                    L.rooms[G.room_id].stwor = None
                                    print("Zabiłeś trolla!")
                                    continue
                        d = G.attack_troll(decyzja)
                        if decyzja == "B":
                            if d == "w":
                                L.rooms[G.room_id].stwor.health = L.rooms[G.room_id].stwor.health - 30
                                print("Troll stracił 30 punktów zdrowia!")
                                if L.rooms[G.room_id].stwor.health <= 0:
                                    print("Zabiłeś trolla!")
                                    L.rooms[G.room_id].stwor = None
                                    continue
                        if decyzja == "A":
                            if d == "w":
                                L.rooms[G.room_id].stwor.health = L.rooms[G.room_id].stwor.health - 100
                                print("Troll stracił 100 punktów zdrowia!")
                                if L.rooms[G.room_id].stwor.health <= 0:
                                    print("Zabiłeś trolla!")
                                    L.rooms[G.room_id].stwor = None
                                    continue

                    elif L.rooms[G.room_id].stwor.type == "G":
                        d = L.rooms[G.room_id].stwor.attacks()
                        G.health = G.health - d
                        if G.health <= 0:
                            print("Przegrałeś")
                            break
                        d = G.attack_goblin()
                        L.rooms[G.room_id].stwor.health = L.rooms[G.room_id].stwor.health - d
                        if L.rooms[G.room_id].stwor.health <= 0:
                            print("Zabiłeś goblina!")
                            for i in L.rooms[G.room_id].stwor.items:
                                G.items.append(i)
                            L.rooms[G.room_id].stwor.items = []
                            L.rooms[G.room_id].stwor = None

                    elif L.rooms[G.room_id].stwor.type == "K":
                        print(
                            "Jeśli chcesz naprawić miecz wpisz KR (koszt 1 ZM), jeśli chcesz zakupić kielich wpisz K "
                            "(koszt 3 ZM), a jesli miecz wpisz M. (koszt 2 ZM), jeśli podasz inną sekwencje, "
                            "nic się nie wydarzy.")
                        tekst = input("Podaj odpowiednią komendę: ")
                        if tekst == "K":
                            G.purchase(tekst)
                            L.rooms[G.room_id].stwor.repair(3)
                        if tekst == "M":
                            G.purchase(tekst)
                            L.rooms[G.room_id].stwor.repair(2)
                        if tekst == "KR":
                            ZM = False
                            for i in G.items:
                                if isinstance(i, Zlotamoneta):
                                    ZM = True
                                    break
                            if ZM:
                                for i in G.equipment:
                                    if isinstance(i, Miecz):
                                        if i.wytrzymalosc < 10:
                                            i.wytrzymalosc = 10
                                            L.rooms[G.room_id].stwor.repair(1)
                                            for i in G.items:
                                                if isinstance(i, Zlotamoneta):
                                                    G.items.remove(i)
                                                    break
                                            break
                            else:
                                print("Nie posiadasz niestety złotych monet, nie możesz naprawić miecza.")

                    elif L.rooms[G.room_id].stwor.type == "E":
                        print("Jeśli chcesz się uleczyć u elfa wpisz H, jeśli podasz inną sekwencje,"
                              "nic się nie wydarzy.")
                        tekst = input("Podaj odpowiednią komendę: ")
                        if tekst == "H":
                            h = L.rooms[G.room_id].stwor.heal()
                            G.health = min(100, G.health + h)
                            print(
                                f"Zostałeś uleczony. Aktualne doświadczenie elfa: {L.rooms[G.room_id].stwor.experience}")

                elif komenda == "e":
                    if L.rooms[G.room_id].obiekt is not None:
                        L.rooms[G.room_id].obiekt.name()
                    else:
                        print("W danej komnacie nie ma żadnego obiektu.")
                elif komenda == "f":
                    if L.rooms[G.room_id].obiekt is None:
                        print("Nie można wziąć przedmiotu, bo w tej komnacie nie ma żadnego.")
                    else:
                        G.take_item(L.rooms[G.room_id].obiekt)
                        L.rooms[G.room_id].obiekt = None
                elif komenda == "g":
                    print(L.rooms[G.room_id])
                elif komenda == "h":
                    n = input("Podaj numer komnaty, do której chcesz przejść: ")
                    while Game.convertable_to_int(n) is not True:
                        n = input("Podaj numer komnaty, do której chcesz przejść, nie inny znak:")
                    n = int(n)
                    czy_klucz = False
                    czy_przejscie = False
                    for przejscie in L.transitions.values():
                        if (przejscie.komnata_A == G.room_id and przejscie.komnata_B == n) or (
                                przejscie.komnata_B == G.room_id and przejscie.komnata_A == n):
                            czy_przejscie = True
                            if przejscie.czy_drzwi:
                                for i in G.equipment:
                                    if isinstance(i, Klucz):
                                        czy_klucz = True
                                        G.change_room(n)
                                        aktywnosc = 1
                                        kolejka = kolejka + 1
                                        break
                                if not czy_klucz:
                                    print("Niestety nie masz klucza stąd nie możesz otworzyć drzwi.")
                                    break
                            else:
                                G.change_room(n)
                                aktywnosc = 1
                                kolejka = kolejka + 1
                    if not czy_przejscie:
                        print("Z tej komnaty nie da się przejść do komnaty o tym numerze lub taka komnata nie istnieje "
                              "lub już jesteś w tej komnacie.")
                elif komenda == "i":
                    if L.rooms[G.room_id].czy_wyjscie:
                        licznik1 = 0
                        licznik2 = 0
                        for i in G.items:
                            if isinstance(i, Zlotamoneta):
                                licznik1 = licznik1 + 1
                            if isinstance(i, Zlotykielich):
                                licznik2 = licznik2 + 1
                        if licznik1 > 1 and licznik2 > 0:
                            print("Zwycięstwo!")
                            win = True
                            break
                        else:
                            print(
                                "W tej komnacie jest wyjście, ale nie masz przynajmniej 2 złotych monet "
                                "i złotego kielicha.")
                    else:
                        print('W tej komnacie nie ma wyjścia.')
            if win is not True:
                print("Przegrałeś!")

        if liczba != 1:
            print("Okej, zapraszam innym razem")


Game = Gra()
Game.play()
