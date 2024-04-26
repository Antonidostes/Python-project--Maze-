class Obiekt():
    def __init__(self, id: int, typ: str, nk: int):
        """
        Jest to metoda inicjalizująca klasy.

        :param id: identyfikator
        :type id: int
        :param typ: typ obiektu (jeden z pieciu)
        :type typ: str
        :param nk: numer komnaty,w ktorej sie on znajduje
        :type nk: int

        """
        self.id = id
        self.type = typ
        self.nk = nk

    def name(self):
        """
        Metoda ta sluzy do wypisania nazwy obiektu.

        :return:
                string
        """
        if self.type == "ZK":
            print("Złoty kielich")
        if self.type == "ZM":
            print("Złota moneta")
        if self.type == "K":
            print("Klucz")
        if self.type == "A":
            print("Apteczka")
        if self.type == "M":
            print("Miecz")


