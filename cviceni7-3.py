class ChybnaCastka(Exception):
    pass

class BankovniUcet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.__zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self.__zustatek} kc"

    def vloz(self, castka):
        # vlozit jde pouze kladna castka, jinak vyhodit vyjimku (pomoci raise)
        if castka <= 0:
            raise ChybnaCastka("Nemuzu vlozit zapornou castku")
        self.__zustatek += castka

    def vyber(self, castka):
        # vybrat jde pouze kladna castka nizsi nez je __zustatek, jinak vyhodit vyjimku (pomoci raise)
        if castka <= 0:
            raise ChybnaCastka("xxx")
        if castka > self.__zustatek:
            raise ChybnaCastka("Nemuzu vybrat vic, nez je na ucte")
        self.__zustatek -= castka

    def pricti_uroky(self):
        # navys zustatek uctu o nasobek uroku, tzn. pokud je urok 0.05 -> zustatek += zustatek * 0.05
        self.__zustatek += self.__zustatek * self.urok


if __name__ == "__main__":
    ucet = BankovniUcet("sporici", 0.05)
    ucet.vloz(-200)
    ucet.vyber(100)
    ucet.pricti_uroky()
    print(ucet)