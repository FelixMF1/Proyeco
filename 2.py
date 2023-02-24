
class Perro:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("Guau guau")

    def envejecer(self):
        self.edad += 1
        