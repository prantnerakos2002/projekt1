#objektumok

class Teglalap:
    alakzat = "téglalap"

    def __init__(self, alap=10, magassag=5):
        self.alap = alap
        self.magassag = magassag

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")
        print(f"A {self.alakzat} magassága = {self.magassag}")

    def kerulet(self):
        return 2 * self.alap + 2 * self.magassag

    def terulet(self):
        return self.alap * self.magassag


class Negyzet(Teglalap):
    alakzat = "négyzet"

    def __init__(self, alap=5):
        super().__init__(alap=alap, magassag=alap)

    def adatok(self):
        print(f"A {self.alakzat} oldala = {self.alap}")


class Haromszog(Teglalap):
    alakzat = "derékszögű háromszög"

    def __init__(self, alap=10, magassag=5):
        super().__init__(alap=alap, magassag=magassag)

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")

    def terulet(self):
        return (self.alap * self.magassag) / 2

tegla = Teglalap(alap=20, magassag=15)
tegla.adatok()
print("A téglalalp kerülete =", tegla.kerulet())
print("A téglalalp területe =", tegla.terulet())
print()


negy = Negyzet(8)
negy.adatok()
print("A négyzet kerülete =", negy.kerulet())
print("A négyzet területe =", negy.terulet())


harom = Haromszog()
print(harom.adatok())
print("A háromszög területe = ", harom.terulet())