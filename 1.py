class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    def esmayordeedad(self):
        if self.edad >= 18:
            return True
        else:
            return False
person = Persona("rika", 15, "21560158")
person.mostrar()
print("¿La persona es mayor de edad?:", person.esmayordeedad())