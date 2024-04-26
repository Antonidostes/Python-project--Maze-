from Stwor import Stwor


class Krasnolud(Stwor):
    def __init__(self, typ, nk):
        super().__init__(typ, nk)
        self.coins = 0

    def repair(self, n):
        """
        Metoda zwiekszajaca liczbe monet krasnoluda

        :param n: liczba monet (int)

        :return:
        """
        self.coins = self.coins + n