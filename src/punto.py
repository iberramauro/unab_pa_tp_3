class Punto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def eje_x(self):
        print (f"El punto cruza por el eje X en {self.x")

    def eje_y(self):
        print (f"El punto cruza por el eje Y en {self.y}")

    def imprimir(self):
        return (f"({self.x},{self.y})")

    def opuesto(self, punto):
        return (punto * -1)
