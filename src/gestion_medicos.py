"""
gestion_medicos.py - Gestiona los medicos del hospital usando ARREGLOS.

Responsable: est1
Estructura de datos: list (arreglo dinamico de Python)

PENDIENTE DE IMPLEMENTAR: est1 debe reemplazar los metodos
con la logica real en las Rondas 1 y 2.
"""


class GestionMedicos:
    # __init__ es el constructor: se ejecuta al hacer 'GestionMedicos()'.
    # 'self' es el propio objeto; siempre va como primer parametro de los metodos.
    def __init__(self):
        # En Python una lista crece y se reduce sola: no hay que declarar tamano.
        # El guion bajo inicial (_medicos) es la forma de avisar "esto es interno,
        # no se toca desde fuera". Es el equivalente de 'private' en Java.
        self._medicos = []

    # Stub: metodo para registrar un medico. Recibe nombre y especialidad.
    # En la Ronda 1 se implementara con la logica real usando una clase Medico.
    def registrar(self, nombre, especialidad):
        print("[Pendiente] Registrar medico: " + nombre)

    # Stub: metodo para asignar un medico disponible a un paciente.
    # Devuelve None porque aun no tiene logica real.
    # None es el equivalente de null en Java: "sin valor".
    def asignar_medico(self):
        print("[Pendiente] Asignar medico.")
        return None

    # Stub: mostrar los medicos disponibles.
    # En la Ronda 1 se implementara recorriendo la lista y filtrando por disponible = True.
    def ver_disponibles(self):
        print("[Pendiente] Ver medicos disponibles.")

    # Stub: mostrar los medicos ocupados.
    # En la Ronda 2 se implementara recorriendo la lista y filtrando por disponible = False.
    def ver_ocupados(self):
        print("[Pendiente] Ver medicos ocupados.")

    # Stub: liberar un medico ocupado. Recibe el numero del medico a liberar.
    def liberar(self, numero):
        print("[Pendiente] Liberar medico.")

    # Devuelve 0 como valor temporal; luego contara los medicos disponibles
    def contar_disponibles(self):
        return 0

    # Devuelve 0 como valor temporal; luego contara los medicos ocupados
    def contar_ocupados(self):
        return 0