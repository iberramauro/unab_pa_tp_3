class Persona:
    def __init__(self, apellido: str, nombre: str):
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return (f"{self.apellido}, {self.nombre}")

class Libro:

    def __init__(self,
    titulo: str = "",
    autor: object = None,
    ISBN: str = "",
    paginas: int = 0,
    edicion: str = "",
    editorial: str = "",
    lugar: str = "",
    fecha_edicion: str = ""
    ):
        self._titulo = titulo
        self._autor = autor
        self._ISBN = ISBN
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._lugar = lugar
        self._fecha_edicion = fecha_edicion

    @property
    def titulo(self):
        return (self._titulo)

    @titulo.setter
    def titulo(self, valor: str):
        if not valor:
            print ("ERROR: No hay titulo.")
        else:
            self._titulo = valor

    @property
    def autor(self):
        return (self._autor)

    @autor.setter
    def autor(self, valor: str, valor2: str):
        if not valor or not valor2:
            print ("ERROR: Falta Nombre o Apellido.")
        else:
            self._autor = Persona(valor, valor2)

    @property
    def ISBN(self):
        return (self._ISBN)

    @ISBN.setter
    def ISBN(self, valor: str):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._ISBN = valor


    @property
    def paginas(self):
        return (self._paginas)

    @paginas.setter
    def paginas(self, valor: int):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._paginas = valor

    @property
    def edicion(self):
        return (self._edicion)

    @edicion.setter
    def edicion(self, valor: str):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._edicion = valor

    @property
    def editorial(self):
        return (self._editorial)

    @editorial.setter
    def editorial(self, valor: str):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._editorial = valor

    @property
    def lugar(self):
        return (self._lugar)

    @lugar.setter
    def lugar(self, valor: str):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._lugar = valor

    @property
    def fecha_edicion(self):
        return (self._fecha_edicion)

    @fecha_edicion.setter
    def fecha_edicion(self, valor: str):
        if not valor:
            print ("ERROR: No hay datos.")
        else:
            self._fecha_edicion = valor


    def leer_informacion(self):
        print ("\n--Carga de datos del Libro--")
        self.titulo = input ("Titulo: ")
        ape = input ("Apellido del autor: ")
        nom = input ("Nombre del Autor: ")
        self.autor = ape, nom
        self.ISBN = input ("ISBN: ")
        self.paginas = int (input ("Paginas: "))
        self.edicion = input ("Edicion: ")
        self.editorial = input ("Editorial: ")
        self.lugar = input ("Lugar: ")
        self.fecha_edicion = input ("Fecha de edicion: ")

    def mostrar_informacion(self):
        print (f"\nTitulo: {self._titulo} {self._edicion} edicion.")
        print (f"Autor: {self._autor}")
        print (f"ISBN: {self._ISBN}")
        print (f"{self._editorial}, {self._lugar}")
        print(f"{self._fecha}")
        print(f"{self._paginas} paginas")

