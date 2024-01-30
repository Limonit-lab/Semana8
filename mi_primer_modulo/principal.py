# Crear una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo.

from claseAlumno import Alumno

alumno1 = Alumno("Guadi", 9)

print(alumno1.nombre)
print(alumno1.nota)
print(alumno1.imprimir())