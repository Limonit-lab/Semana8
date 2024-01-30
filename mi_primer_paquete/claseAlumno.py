
# Primer módulo
# Hacer una clase fácil, como Alumno, con nombre y nota, con un método imprimir().
# Crear una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Imprimiendo")