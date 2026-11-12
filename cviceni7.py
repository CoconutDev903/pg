class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def secti(self, jiny_vektor):
        return Vektor(self.x + jiny_vektor.x, self.y + jiny_vektor.y)

    def vynasob(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)

if __name__ == "__main__":

    v1 = Vektor(10,5)
    print(v1)

    v2 = Vektor(3,8)
    v1.secti(v2)

    v1.vynasob(2)

    print(v1)