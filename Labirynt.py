from Komnata import Komnata
from queue import Queue
from Przejscie import Przejscie

import random


class Labirynt:
    def __init__(self):
        """
        Jest to metoda inicjalizująca klasy.

        :param rooms: slownik o kluczach w liczbach naturalnych i wartosciach w kolejnych komnatach
        :type rooms: dict
        :param transitions: slownik o kluczach w liczbach naturalnych i wartosciach w kolejnych przejsciach
        :type transitions: dict
        :param id_tran: licznik kolejnych identyfikatorow (kluczy) przejsc
        :type id_tran: int
        :param colors: slownik o kluczach w komnatach i wartosciach w kolorach (bialy, szary, czarny)
        :type colors: dict

        """
        self.rooms = {}
        self.transitions = {}
        self.id_tran = 1
        self.colors = {}

    def add_room(self, key):
        """
        Metoda ta tworzy nowa komnate.

        :param key: identyfikator komnaty

        :return:
        """
        new_room = Komnata(key)
        self.rooms[key] = new_room

    def add_connection(self, a, b, D):
        """
        Metoda ta tworzy poloczenie miedzy komnatami.

        :param a: identyfikator komnaty (int)

        :param b: identyfikator komnaty (int)

        :param D: prawdopodobienstwo utworzenia drzwi miedzy komnatami
        o danych identyfikatorach (float)

        :return:
        """
        self.rooms[a].add_neighbor(self.rooms[b])
        self.rooms[b].add_neighbor(self.rooms[a])
        l = random.random()
        if l < D:
            przejscie = Przejscie(a, True, False, self.id_tran, b)
            self.transitions[self.id_tran] = przejscie
            self.id_tran = self.id_tran + 1
        else:
            przejscie = Przejscie(a, False, False, self.id_tran, b)
            self.transitions[self.id_tran] = przejscie
            self.id_tran = self.id_tran + 1

    def __iter__(self):
        """
        Metoda ta iteruje po kolejnych komnatach (instancjach klasy Komnata, zwraca je).

        :return:
                list
        """
        return iter(self.rooms.values())

    def drawing_method(self, P, D):
        """
        Metoda ta losuje labirynt, tzn. czy istnieja poloczenia miedzy danymi komnatami, czy tez nie.

        :param P: prawdopodobienstwo utworzenia poloczenia miedzy danymi komnatami (float)

        :param D: prawdopodobienstwo utworzenia drzwi miedzy komnatami (float)

        :return:
        """
        for i in self.rooms.keys():
            for j in self.rooms.keys():
                l = random.random()
                if l < P and i != j:
                    self.add_connection(i, j, D)

    def BFS_modificated(self, N, D):
        """
        Metoda ta przez zmodyfikowany algorytm BFS sprawdza, czy wszystkie komnaty tworza graf spojny.

        :param N: liczba komnat (int)

        :param D: prawdopodobienstwo utworzenia drzwi miedzy komnatami (float)
        :return:
        """
        ls = []
        while len(ls) < N:
            ls = []
            self.colors = {}
            for i in self.rooms:
                self.colors[i] = "white"

            kom_queue = Queue()

            kom_queue.put(self.rooms[1])
            ls.append(self.rooms[1])

            while not kom_queue.empty():
                current_kom = kom_queue.get()
                cur_key = current_kom.get_number()

                for nbr in current_kom.connections.keys():
                    nbr_key = nbr.get_number()
                    ls.append(nbr_key)
                    if self.colors[nbr_key] == 'white':
                        self.colors[nbr_key] = 'gray'
                        kom_queue.put(nbr)

                self.colors[cur_key] = 'black'

            ls = list(set(ls))
            if len(ls) < N:
                a = random.choice(ls)
                for i in self.rooms.keys():
                    if i not in ls:
                        self.add_connection(a, i, D)
                        break













