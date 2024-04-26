class Przejscie:
    def __init__(self, A, czy_drzwi, czy_wyjscie, id, B=None):
        """
        Jest to metoda inicjalizująca klasy.

        :param A: komnata
        :type id: object
        :param czy_drzwi: Prawda lub Falsz
        :type id: bool
        :param czy_wyjscie: Prawda lub Falsz
        :type id: bool
        :param id: identyfikator
        :type id: int
        :param B: komnata (object) lub None (NoneType)
        :type id: object lub None

        """
        self.id = id
        self.komnata_A = A
        self.komnata_B = B
        self.czy_drzwi = czy_drzwi
        self.czy_wyjscie = czy_wyjscie