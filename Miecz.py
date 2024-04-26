from Obiekt import Obiekt


class Miecz(Obiekt):
    def __init__(self, id, typ, nk):
        super().__init__(id, typ, nk)
        self.wytrzymalosc = 10
