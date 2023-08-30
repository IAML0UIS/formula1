
class coche:
    def __init__(self, marca , modelo):
        self.marca = marca
        self.modelo = modelo
        self.sumadre = False
    def arrancar (self):
        self.sumadre = False
        print("El carro", self.marca, self.modelo, "ha arrancado") 

    def parar (self):
        self.sumadre = True
        print("El carro", self.marca, self.modelo, "se ha parado")        

ferrari = coche("ferrari", "f40")

print(type(ferrari))
print(ferrari.marca, ferrari.modelo)

ferrari.arrancar()
ferrari.parar()

print(ferrari.arrancar)

print(ferrari.parar)
