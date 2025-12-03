import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json 

class Horario:
    """Clase interna de Biblioteca (Composición)."""
    def __init__(self, dias, h_apertura, h_cierre):
        self.dias = dias
        self.h_apertura = h_apertura
        self.h_cierre = h_cierre
    
    def mostrarHorario(self):
        return f"Días: {self.dias}, Horario: {self.h_apertura} - {self.h_cierre}"

    def to_dict(self): #
        return {'dias': self.dias, 'h_apertura': self.h_apertura, 'h_cierre': self.h_cierre}

class Pagina:
    """Clase interna de Libro (Composición)."""
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido
    
    def mostrarContenido(self):
        return f"Pág. {self.numero}: {self.contenido[:50]}..." 

    def to_dict(self): #
        return {'numero': self.numero, 'contenido': self.contenido}

class Libro:
    """Representa un libro (Agregación con Biblioteca, Composición con Página)."""
    def __init__(self, titulo, isbn, paginas_data):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i + 1, contenido) for i, contenido in enumerate(paginas_data)]
    
    def leer(self):
        contenido = [p.mostrarContenido() for p in self.paginas]
        return f"Libro: {self.titulo}\n" + "\n".join(contenido)

    def to_dict(self):
        return {
            'titulo': self.titulo, 
            'isbn': self.isbn, 
            'paginas': [p.to_dict() for p in self.paginas]
        }
    
    def __str__(self):
        return f"Libro: {self.titulo} (ISBN: {self.isbn})"



class Autor:
    """Representa un Autor (Agregación con Biblioteca)."""
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}"

    def to_dict(self): 
        return {'nombre': self.nombre, 'nacionalidad': self.nacionalidad}
    
    def __str__(self):
        return self.nombre

class Estudiante:
    """Representa un Estudiante (Asociación con Préstamo)."""
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        return f"Estudiante: {self.nombre} (Cód: {self.codigo})"

    def to_dict(self): 
        return {'codigo': self.codigo, 'nombre': self.nombre}
    
    def __str__(self):
        return self.nombre

class Prestamo:
    """Representa un Préstamo (Asociación con Estudiante y Libro)."""
    def __init__(self, estudiante, libro, fecha_prestamo="Hoy", fecha_devolucion="Una semana"):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estudiante = estudiante
        self.libro = libro         

    def mostrarInfo(self):
        return (f"Préstamo:\n"
                f"  Libro: {self.libro.titulo}\n"
                f"  Estudiante: {self.estudiante.nombre}\n"
                f"  Fechas: {self.fecha_prestamo} a {self.fecha_devolucion}")

    def to_dict(self): 
        return {
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion,
            'estudiante_codigo': self.estudiante.codigo,
            'libro_isbn': self.libro.isbn
        }
    
    def __str__(self):
        return f"Préstamo: {self.libro.titulo} a {self.estudiante.nombre}"


class Biblioteca:
    """Clase principal que gestiona las relaciones."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []      
        self.autores = []    
        self.prestamos = []   
        self.horario = Horario("Lunes a Viernes", "8:00", "18:00") 

    def agregarLibro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Debe agregar un objeto Libro.")
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a la biblioteca."

    def agregarAutor(self, autor):
        if not isinstance(autor, Autor):
            raise TypeError("Debe agregar un objeto Autor.")
        self.autores.append(autor)
        return f"Autor '{autor.nombre}' registrado en la biblioteca."

    def prestarLibro(self, estudiante, libro):
        if not isinstance(estudiante, Estudiante) or not isinstance(libro, Libro):
            raise TypeError("Estudiante y Libro deben ser objetos válidos.")
        
        if libro not in self.libros:
            return f"Error: Libro '{libro.titulo}' no existe en el catálogo."
        if any(p.libro.isbn == libro.isbn for p in self.prestamos):
            return f"Error: Libro '{libro.titulo}' ya está prestado."
            
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        return f"Préstamo creado: {libro.titulo} prestado a {estudiante.nombre}."

    def mostrarEstado(self):
        estado = f"--- Estado de la Biblioteca: {self.nombre} ---\n"
        estado += self.horario.mostrarHorario() + "\n"
        estado += f"Total de Libros en Catálogo: {len(self.libros)}\n"
        estado += f"Total de Autores Registrados: {len(self.autores)}\n"
        estado += f"Préstamos Activos ({len(self.prestamos)}):\n"
        
        if self.prestamos:
            for p in self.prestamos:
                estado += f"  - {p.libro.titulo} (por {p.estudiante.nombre})\n"
        else:
            estado += "  - No hay préstamos activos.\n"
        return estado

    def cerrarBiblioteca(self):
        self.prestamos = []
        return f"¡Biblioteca {self.nombre} cerrada! Todos los préstamos activos han sido cancelados."

    def to_dict(self):
        """Convierte la Biblioteca y sus objetos contenidos a un diccionario JSON."""
        return {
            'nombre': self.nombre,
            'horario': self.horario.to_dict(),
            'libros': [l.to_dict() for l in self.libros],
            'autores': [a.to_dict() for a in self.autores],
            'prestamos': [p.to_dict() for p in self.prestamos]
        }
    
    @classmethod
    def from_dict(cls, data):
        """Reconstruye el objeto Biblioteca a partir de un diccionario JSON."""
        
        biblioteca = cls(data['nombre'])
        
        h_data = data.get('horario', {})
        biblioteca.horario = Horario(h_data.get('dias'), h_data.get('h_apertura'), h_data.get('h_cierre'))
 
        biblioteca.libros = []
        for l_data in data.get('libros', []):
            paginas_data = [p_data['contenido'] for p_data in l_data.get('paginas', [])]
            biblioteca.libros.append(Libro(l_data['titulo'], l_data['isbn'], paginas_data))

        biblioteca.autores = [Autor(a_data['nombre'], a_data['nacionalidad']) for a_data in data.get('autores', [])]
  
        biblioteca.prestamos = []
        libros_map = {l.isbn: l for l in biblioteca.libros}
        estudiantes_map = {} 

        for p_data in data.get('prestamos', []):
            libro = libros_map.get(p_data['libro_isbn'])
            estudiante_codigo = p_data['estudiante_codigo']
            estudiante_nombre = Estudiante(estudiante_codigo, "Desconocido")
 
            if estudiante_codigo not in estudiantes_map:
  
                estudiantes_map[estudiante_codigo] = estudiante_nombre 
            
            estudiante = estudiantes_map[estudiante_codigo]

            if libro:
                prestamo = Prestamo(estudiante, libro, p_data['fecha_prestamo'], p_data['fecha_devolucion'])
                biblioteca.prestamos.append(prestamo)
                
        return biblioteca

FILE_NAME = "biblioteca_umsa.json"

def guardar_biblioteca(biblioteca, filename=FILE_NAME):
    """Guarda el objeto Biblioteca en un archivo JSON."""
    data = biblioteca.to_dict()
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return f"Estado de la biblioteca guardado en {filename}"

def cargar_biblioteca(filename=FILE_NAME):
    """Carga el objeto Biblioteca desde un archivo JSON, o crea uno nuevo."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return Biblioteca.from_dict(data)
    else:
        return Biblioteca("Biblioteca Central UMSA")
#2
class BibliotecaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Biblioteca UMSA")
        master.geometry("700x500")
        master.configure(bg="#F0F8FF")

        self.biblioteca = cargar_biblioteca()

        self.label_titulo = tk.Label(master, text=self.biblioteca.nombre, 
                                     font=("Arial", 20, "bold"), bg="#F0F8FF", fg="#3A3A3A")
        self.label_titulo.pack(pady=10)

        self.frame_botones = tk.Frame(master, bg="#F0F8FF")
        self.frame_botones.pack(pady=20)

        tk.Button(self.frame_botones, text="Agregar Libro", command=self.ventana_agregar_libro, bg="#A9D0F5", fg="black").grid(row=0, column=0, padx=10, pady=10, ipadx=10)
        tk.Button(self.frame_botones, text="Registrar Autor", command=self.ventana_agregar_autor, bg="#A9D0F5", fg="black").grid(row=0, column=1, padx=10, pady=10, ipadx=10)
        tk.Button(self.frame_botones, text="Crear Préstamo", command=self.ventana_prestar_libro, bg="#A9D0F5", fg="black").grid(row=0, column=2, padx=10, pady=10, ipadx=10)
        tk.Button(self.frame_botones, text="Mostrar Estado", command=self.mostrar_estado, bg="#A9D0F5", fg="black").grid(row=1, column=0, padx=10, pady=10, ipadx=10)
        tk.Button(self.frame_botones, text="Guardar y Salir", command=self.guardar_y_salir, bg="#FF6347", fg="white").grid(row=1, column=1, padx=10, pady=10, ipadx=10)
        tk.Button(self.frame_botones, text="Cerrar Biblioteca", command=self.cerrar_biblioteca, bg="#FF6347", fg="white").grid(row=1, column=2, padx=10, pady=10, ipadx=10)

        self.estado_texto = tk.Text(master, height=12, width=80, font=("Courier", 10))
        self.estado_texto.pack(pady=10)
        self.mostrar_mensaje(self.biblioteca.mostrarEstado())

    def mostrar_mensaje(self, mensaje):
        self.estado_texto.delete(1.0, tk.END)
        self.estado_texto.insert(tk.END, mensaje)

    def ventana_agregar_libro(self):
        titulo = simpledialog.askstring("Libro", "Título del Libro:")
        isbn = simpledialog.askstring("Libro", "ISBN:")
        
        if titulo and isbn:
            paginas_data = [f"Contenido de la página {i+1} del libro {titulo}." for i in range(3)] 
            try:
                nuevo_libro = Libro(titulo, isbn, paginas_data)
                resultado = self.biblioteca.agregarLibro(nuevo_libro)
                self.mostrar_mensaje(resultado + "\n\n" + self.biblioteca.mostrarEstado())
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
    def ventana_agregar_autor(self):
        nombre = simpledialog.askstring("Autor", "Nombre del Autor:")
        nacionalidad = simpledialog.askstring("Autor", "Nacionalidad:")
        
        if nombre and nacionalidad:
            try:
                nuevo_autor = Autor(nombre, nacionalidad)
                resultado = self.biblioteca.agregarAutor(nuevo_autor)
                self.mostrar_mensaje(resultado + "\n\n" + self.biblioteca.mostrarEstado())
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def ventana_prestar_libro(self):
        cod_est = simpledialog.askstring("Préstamo", "Código del Estudiante (ej: E123):")
        nom_est = simpledialog.askstring("Préstamo", "Nombre del Estudiante:")
        titulo_libro = simpledialog.askstring("Préstamo", "Título del Libro a prestar:")

        if cod_est and nom_est and titulo_libro:
            libro_encontrado = next((l for l in self.biblioteca.libros if l.titulo == titulo_libro), None)

            estudiante_nuevo = Estudiante(cod_est, nom_est) 

            if libro_encontrado:
                try:
                    resultado = self.biblioteca.prestarLibro(estudiante_nuevo, libro_encontrado)
                    self.mostrar_mensaje(resultado + "\n\n" + self.biblioteca.mostrarEstado())
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", f"Libro '{titulo_libro}' no encontrado en el catálogo.")

    def mostrar_estado(self):
        self.mostrar_mensaje(self.biblioteca.mostrarEstado())

    def cerrar_biblioteca(self):
        resultado = self.biblioteca.cerrarBiblioteca()
        self.mostrar_mensaje(resultado + "\n\n" + self.biblioteca.mostrarEstado())
        messagebox.showinfo("Cierre", resultado)

    def guardar_y_salir(self):
        mensaje = guardar_biblioteca(self.biblioteca)
        messagebox.showinfo("Persistencia", mensaje)
        self.master.destroy()

#3
if __name__ == "__main__":
    
    if not os.path.exists(FILE_NAME):
        b = Biblioteca("Biblioteca Central UMSA")
        
        l1 = Libro("Cien Años de Soledad", "978-0307474728", ["Capítulo 1", "Capítulo 2", "Capítulo 3", "Capítulo 4"])
        l2 = Libro("El Principito", "978-3125971501", ["Intro", "Encuentro con el piloto", "Despedida"])
        a1 = Autor("Gabriel García Márquez", "Colombiana")
        
        b.agregarLibro(l1)
        b.agregarLibro(l2)
        b.agregarAutor(a1)
        
        guardar_biblioteca(b)

    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()