class Stwor():
    def __init__(self, typ, nk):
        """

        :param typ: typ (string)

        :param nk: numer komnaty (int)
        """
        self.type = typ
        self.komnata = nk

    def name(self):
        """
        Metoda ta sluzy do wypisania nazwy stwora.

        :return:
                string
        """
        if self.type == "T":
            print("Troll, walcząc możesz albo się zablokować (jeśli masz miecz) albo zrobić unik.")
        if self.type == "G":
            print("Goblin, jest szybki ale słaby, więc zadawane obrażenia są losowe, jednak Ty zadajesz większe.\n"
                  "Jeśli ukradł Ci przedmiot, to zabijając go możesz go odzyskać.")
        if self.type == "K":
            print("Krasnolud")
        if self.type == "E":
            print("Elf")
