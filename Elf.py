from Stwor import Stwor


class Elf(Stwor):
    def __init__(self,typ, nk, item):
        super().__init__(typ, nk)
        self.item = item
        self.experience = 0

    def heal(self):
        """
        Metoda ta pozwala elfowi uzdrowic gracza, zwraca liczbe punktow zdrowia w zaleznosci od doswiadczenia elfa.

        :return:
                int
        """
        self.experience = self.experience + 1
        if self.experience == 0:
            return 10
        if self.experience > 0:
            return 25


