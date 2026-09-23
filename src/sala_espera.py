"""
sala_espera.py - Gestiona la sala de espera usando COLA y PILA.

Responsable: est2
Estructuras de datos: deque (cola FIFO) y list (pila LIFO)

deque viene incluida en Python, en el modulo collections. Se usa para la
cola porque sacar el primer elemento es inmediato; en una lista normal
habria que correr todos los demas una posicion.

PENDIENTE DE IMPLEMENTAR: est2 debe reemplazar los metodos
con la logica real en las Rondas 1 y 2.
"""

# deque es la "cola doblemente terminada" de Python
from collections import deque


class SalaEspera:
    def __init__(self):
        # COLA (FIFO): el primero en llegar es el primero en ser atendido
        self._cola_espera = deque()
        # PILA (LIFO): el ultimo atendido es el primero que se ve.
        # Para la pila basta una lista normal: append() y pop() trabajan
        # por el final, que es justo lo que hace una pila.
        self._historial_atendidos = []

    # Stub: agrega un paciente al final de la cola de espera.
    # En la Ronda 1 se implementara con append().
    def encolar(self, id_paciente, nombre):
        print("[Pendiente] Encolar paciente: " + nombre)

    # Stub: saca al primer paciente de la cola y lo pasa al historial.
    # Devolvera una lista [id, nombre], o None si no habia nadie.
    def atender_siguiente(self):
        print("[Pendiente] Atender siguiente paciente.")
        return None

    # Stub: muestra los pacientes que estan esperando.
    def ver_espera(self):
        print("[Pendiente] Ver sala de espera.")

    # Stub: muestra la pila de pacientes ya atendidos.
    def ver_historial(self):
        print("[Pendiente] Ver historial de atendidos.")

    # Stub: devuelve el ultimo paciente atendido a la cola de espera.
    def deshacer_ultima_atencion(self):
        print("[Pendiente] Deshacer ultima atencion.")

    # Devuelve 0 como valor temporal; luego devolvera el tamano de la cola
    def contar_espera(self):
        return 0

    # Devuelve 0 como valor temporal; luego devolvera el tamano de la pila
    def contar_atendidos(self):
        return 0