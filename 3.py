class Persona:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def estado_peso(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"
        
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

persona = Persona(peso, altura)
print("Tu IMC es:", persona.calcular_imc())
print("Tu estado de peso es:", persona.estado_peso())