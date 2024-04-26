from Stwor import Stwor
import random

class Goblin(Stwor):
    def __init__(self, typ, nk):
        super().__init__(typ, nk)
        self.health = 50
        self.items = []

    def steal(self, ls):
        """
        Metoda pozwalajaca goblinowi ukrasc dany przedmiot nalezacy do gracza.

        :param ls: lista przedmiotow gracza (list)

        :return:
        """
        if len(ls) > 0:
            a = random.choice(ls)
            i = ls.index(a)
            a = ls.pop(i)
            self.items.append(a)

    def attacks(self):
        """
        Metoda losujaca i zwracajaca obrazenia zadawane przez goblina graczowi.

        :return:
                int
        """
        d = random.choice([5, 10])
        return d





