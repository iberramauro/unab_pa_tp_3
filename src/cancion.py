class Cancion:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        print (f"El nombre de la cancion es {self.titulo}.")

    def get_autor(self):
        print (f"El nombre del autor es {self.autor}.")

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def set_autor(self, autor: str):
        self.autor = autor

