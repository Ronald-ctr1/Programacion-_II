from datetime import date

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}")

class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Página {self.numero}: {self.contenido}")

class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i + 1, contenido) for i, contenido in enumerate(contenidos_paginas)]

    def leer(self):
        print(f"\nLeyendo libro: {self.titulo}")
        for pagina in self.paginas:
            pagina.mostrarPagina()

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre}, Código: {self.codigo}")

class Prestamo:
    def __init__(self, estudiante, libro):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"Préstamo -> Libro: {self.libro.titulo}, Estudiante: {self.estudiante.nombre}, Fecha: {self.fecha_prestamo}")

class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print(f"Horario: {self.dias} de {self.hora_apertura} a {self.hora_cierre}")

class Biblioteca:
    def __init__(self, nombre, dias, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.horario = Horario(dias, hora_apertura, hora_cierre)
        self.libros = []
        self.autores = []
        self.prestamos = []

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"\nSe realizó un préstamo del libro '{libro.titulo}' a {estudiante.nombre}")

    def mostrarEstado(self):
        print(f"\n--- Estado de la Biblioteca '{self.nombre}' ---")
        print("Autores registrados:")
        for a in self.autores:
            a.mostrarInfo()
        print("\nLibros disponibles:")
        for l in self.libros:
            print(f"- {l.titulo}")
        print("\nPréstamos activos:")
        for p in self.prestamos:
            p.mostrarInfo()
        print()
        self.horario.mostrarHorario()

    def cerrarBiblioteca(self):
        print(f"\nLa biblioteca '{self.nombre}' está cerrando. Se eliminan los préstamos activos.")
        self.prestamos.clear()


#Main
if __name__ == "__main__":
   
    autor1 = Autor("Gabriel García Márquez", "Colombiana")
    autor2 = Autor("Alcides Arguedas", "Bolivia")

    libro1 = Libro("Cien Años de Soledad", "123-232-543", ["En un lugar de Macondo...", "El hielo fue lo primero que vio."])
    libro2 = Libro("Raza de Bronce", "5443-656523-98", ["El rojo dominaba en el paisaje...", "Al amanecer del sigui..."])
    
    estudiante1 = Estudiante("1234567", "Juan Pérez")
    estudiante2 = Estudiante("7654321", "Antonio López")

    biblioteca = Biblioteca("Biblioteca Central UMSA", "Lunes a Viernes", "08:00", "18:00")

    biblioteca.agregarAutor(autor1)
    biblioteca.agregarAutor(autor2)
    biblioteca.agregarLibro(libro1)
    biblioteca.agregarLibro(libro2)

    biblioteca.prestarLibro(estudiante1, libro1)
    biblioteca.prestarLibro(estudiante2, libro2)

    biblioteca.mostrarEstado()

    libro1.leer()

    biblioteca.cerrarBiblioteca()
