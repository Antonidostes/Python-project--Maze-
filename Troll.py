from Stwor import Stwor
from Gracz import Gracz
import random


class Troll(Stwor):
    def __init__(self, typ, nk):
        super().__init__(typ, nk)
        self.health = 150

    def attacks(self, d):
        """

        :param d: decyzja gracza o tym, czy sie blokuje, czy robi unik (string)

        :return:
                string
        """
        if d == "B":
            a = random.choices(["l", "d", "w"], [0.2, 0.4, 0.4])[0]
            return a
        if d == "A":
            a = random.choices(["l", "w"], [0.7, 0.3])[0]
            return a
