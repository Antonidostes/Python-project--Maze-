from Apteczka import Apteczka
from Miecz import Miecz
from Klucz import Klucz
from Zlotykielich import Zlotykielich
from Zlotamoneta import Zlotamoneta
import random


class Gracz:
    def __init__(self):
        """
        Jest to metoda inicjalizująca klasy.

        :param health: liczba punktow zdrowia gracza
        :type health: int
        :param equipment: lista zawierajaca ekwipunek posiadany przez gracza
        :type equipment: list
        :param items: lista zawierajaca przedmioty posiadane przez gracza
        :type items: list
        :param room_id: identyfikator pokoju, w ktorym znajduje sie gracz
        :type room_id: int
        :param ides: liczba okreslajaca kolejne identyfikatory przedmiotow zakupowanych przez gracza
        :type ides: int

        """
        self.health = 100
        self.equipment = []
        self.items = []
        self.room_id = None
        self.ides = 100

    def heal(self):
        """
        Metoda pozwalajaca graczowi sie uzdrowic przez uzycie apteczki (jesli posiada on apteczke).

        :return:
                string
        """
        first_aid_kit = False
        if self.health != 100:
            for i in self.equipment:
                if isinstance(i, Apteczka):
                    first_aid_kit = True
                    self.health = min(self.health + 20, 100)
                    print("Zostałeś uleczony, liczba Twoich punktów zdrowia wzrosła o 20 lub do 100 (maksymalna wartość).")
                    self.equipment.remove(i)
                    break
            if first_aid_kit == False:
                print("Nie posiadasz niestety apteczki.")
        else:
            print("Jesteś w pełni zdrowy, nie użyto apteczki!")

    def attack_troll(self, d):
        """
        Metoda ta losuje obrazenia zadawane przez gracza trollowi w zaleznosci od podjetej przez uzytkownika decyzji.

        :param d: decyzja gracza o tym, czy sie blokuje, czy robi unik (string)

        :return:
                string
        """
        if d == "A":
            a = random.choices(["l", "w"], [0.2, 0.8])[0]
            return a
        if d == "B":
            a = random.choices(["l", "w"], [0.6, 0.4])[0]
            return a

    def attack_goblin(self):
        """
        Metoda ta losuje obrazenia zadawane przez gracza goblinowi.

        :return:
                int
        """
        d = random.choice([0, 15, 30])
        return d

    def purchase(self, tekst):
        """
        Metoda ta kontroluje zakup przez gracza danego przedmiotu.

        :param tekst: decyzja gracza, co chce on kupic (string)

        :return:
                string
        """
        licznik = 0
        for i in self.items:
            if isinstance(i, Zlotamoneta):
                licznik = licznik + 1
        if tekst == "K":
            if licznik > 2:
                print("Zakupiono kielich")
                self.items.append(Zlotykielich(self.ides, "ZK", None))
                self.ides = self.ides + 1
                counter = 3
                for i in self.items:
                    if isinstance(i, Zlotamoneta):
                        self.items.remove(i)
                        counter = counter - 1
                    if counter == 0:
                        break
        else:
            print("Niestety nie możesz kupić kielicha, masz za mało monet.")
        if tekst == "M":
            if licznik > 1:
                print("Zakupiono miecz")
                self.equipment.append(Miecz(self.ides, "M", None))
                self.ides = self.ides + 1
                counter = 2
                for i in self.items:
                    if isinstance(i, Zlotamoneta):
                        self.items.remove(i)
                        counter = counter - 1
                    if counter == 0:
                        break
        else:
            print("Niestety nie możesz kupić miecza, masz za mało monet.")

    def take_item(self, O):
        """
        Metoda pozwalajaca graczowi wziac przedmiot znajdujacy sie w komnacie.

        :param O: przedmiot lub ekwipunek (object)

        :return:
        """
        if isinstance(O, Miecz) or isinstance(O, Apteczka) or isinstance(O, Klucz):
            self.equipment.append(O)
        else:
            self.items.append(O)

    def change_room(self, n):
        """
        Metoda pozwalajaca graczowi zmienic komnate.

        :param n: numer komnaty (int)

        :return:
        """
        self.room_id = n

    def __str__(self):
        """
        Metoda wypisujaca stan gracza; liczbe punktow zdrowia, posiadane przedmioty i ekwipunek.

        :return:
                string
        """
        m = 0
        a = 0
        k = 0
        zk = 0
        zm = 0
        for i in self.equipment:
            if isinstance(i, Miecz):
                m = m + 1
                continue
            if isinstance(i, Apteczka):
                a = a + 1
                continue
            if isinstance(i, Klucz):
                k = k + 1
                continue
        for i in self.items:
            if isinstance(i, Zlotykielich):
                zk = zk + 1
                continue
            if isinstance(i, Zlotamoneta):
                zm = zm + 1
                continue

        return f"Twoja liczba punktów zdrowia to {self.health}. liczba posiadanych przedmiotów: miecze: {m}, apteczki: {a}, klucze: {k}, złote kielichy: {zk}, złote monety: {zm}."
