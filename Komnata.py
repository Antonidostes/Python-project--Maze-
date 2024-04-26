class Komnata:
    def __init__(self, key):
        """
        Jest to metoda inicjalizująca klasy.

        :param number: identyfikator komnaty
        :type number: int
        :param connections: slownik poloczen danej komnaty
        :type connections: dict
        :param stwor: zmienna okreslajaca, jaki stwor jest w komnacie
        :type stwor: object
        :param obiekt: zmienna okreslajaca, jaki obiekt jest w komnacie
        :type obiekt: object
        :param czy_wyjscie: zmienna okreslajaca, czy dana komnata to wyjscie
        :type czy_wyjscie: bool

        """
        if type(key) is not int:
            raise TypeError("Id komnaty musi być kluczem!")
        self.number = key
        self.connections = {}
        self.stwor = None
        self.obiekt = None
        self.czy_wyjscie = False

    def get_number(self):
        """
        Metoda ta zwraca numer komnaty.

        :return:
                int
        """
        return self.number

    def add_neighbor(self, nbr):
        """
        Metoda ta tworzy polaczenie miedzy komnatami.

        :param nbr: obiekt reprezentujacy komnate (object)

        :return:
        """
        self.connections[nbr] = nbr.number

    def __str__(self):
        """
        Metoda ta wypisuje numer komnaty, numery komnat, z ktorymi dana
        komnata jest polaczona oraz czy jest ona wyjsciem, czy tez nie.

        :return:
                string
        """
        if self.czy_wyjscie:
            return f"{self.number} połaczony z: {[x.number for x in self.connections]}, jest to wyjście."
        else:
            return f"{self.number} połączony z: {[x.number for x in self.connections]}, nie jest to wyjście."




