"""
directorio_pacientes.py - Directorio de pacientes usando ARBOL BINARIO DE BUSQUEDA.

Responsable: est3
Estructura de datos: Arbol BST (menores a la izquierda, mayores a la derecha)

PENDIENTE DE IMPLEMENTAR: est3 debe reemplazar los metodos
con la logica real en las Rondas 1 y 2.
"""


class DirectorioPacientes:
    # Constructor: por ahora no hace nada. En la Ronda 1, est3 agregara
    # aqui la raiz del arbol y la clase Nodo que representa cada paciente.
    # 'pass' es la forma de decir "aqui no hay nada todavia": Python exige
    # que un bloque tenga al menos una instruccion.
    def __init__(self):
        pass

    # Stub: inserta un paciente en el arbol ordenado por ID.
    # En la Ronda 1 se implementara con un metodo recursivo.
    def registrar(self, id_paciente, nombre, motivo):
        print("[Pendiente] Registrar paciente ID: " + str(id_paciente))

    # Stub: busca un paciente por su ID y devuelve un texto con su informacion.
    # str() convierte el numero en texto para poder unirlo con +.
    def buscar(self, id_paciente):
        return "[Pendiente] Buscar paciente ID: " + str(id_paciente)

    # Stub: muestra todos los pacientes ordenados por ID (recorrido inorden).
    def mostrar_inorden(self):
        print("[Pendiente] Mostrar pacientes en orden.")

    # Stub: elimina un paciente del arbol.
    def eliminar(self, id_paciente):
        print("[Pendiente] Eliminar paciente ID: " + str(id_paciente))

    # Stub: muestra el paciente con el ID mas pequeno y el mas grande.
    def mostrar_min_max(self):
        print("[Pendiente] Mostrar paciente con ID menor y mayor.")

    # Devuelve 0 como valor temporal; luego contara los nodos del arbol
    def contar(self):
        return 0

    # Devuelve 0 como valor temporal; luego calculara la altura del arbol
    def altura(self):
        return 0