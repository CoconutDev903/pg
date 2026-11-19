class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.__telefon = telefon
        self.__email = email
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @property
    def telefon(self):
        return self.__telefon
    
    @property
    def email(self):
        return self.__email

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno muze obsahovat pouze pismena")

    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("Cislo muze obsahovat pouze cislice")

    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("Email musi obsahovat @")
        if "." not in hodnota:
            raise InvalidData("Email musi obsahovat tecku")
        if hodnota.replace("@", "").replace(".", "").isalnum():
            self.__email = hodnota
        else:
            raise InvalidData("Email musi obsahovat pouze pismena a cislice")

    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

if __name__ == "__main__":
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    o.jmeno = "Tomas Novotny"  # kontrola, ze jmeno obsahuje pouze pismena
    o.telefon = "00456887876"  # kontrola, ze telefon obsahuje jenom cisla
    o.email = "xxx1@xxx.xx"  # kontrola, ze email obsahuje pouze pismena, cisla, zavinac a tecky

    print(o)