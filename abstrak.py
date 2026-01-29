from abc import ABC, abstractmethod

class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()


class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("--- PERANG DIMULAI ---")

for pahlawan in pasukan:
    pahlawan.serang()
