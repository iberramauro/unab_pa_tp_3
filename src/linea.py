class Linea:

    def __init__(self, punto_a: int, punto_b: int):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, num: float):
        if num >= 0:
            self._punto_a.x += num
            self._punto_b.x += num

    def mueve_izquierda(self, num: float):
        if num >= 0:
            self._punto_a.x -= num
            self._punto_b.x -= num

    def mueve_arriba(self, num: float):
        if num >= 0:
            self._punto_a.y += num
            self._punto_b.y += num

    def mueve_abajo(self, num: float):
        if num >= 0:
            self._punto_a.y -= num
            self._punto_b.y -= num


