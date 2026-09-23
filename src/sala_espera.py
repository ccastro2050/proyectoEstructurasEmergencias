"""
sala_espera.py - Gestiona la sala de espera usando COLA y PILA.

Responsable: est2
Estructuras de datos: deque (cola FIFO) y list (pila LIFO)

Ronda 1: encolar, atender siguiente, ver espera, contar.
Los metodos ver_historial y deshacer_ultima_atencion quedan como stubs
y se implementan en la Ronda 2.
"""

from collections import deque


class PacienteEspera:
    """Representa a un paciente dentro de la sala de espera.

    Solo guarda lo minimo necesario para la cola: su ID y su nombre.
    """

    def __init__(self, id_paciente, nombre):
        self.id = id_paciente
        self.nombre = nombre


class SalaEspera:
    def __init__(self):
        # COLA (FIFO): el primero en llegar es el primero en ser atendido
        self._cola_espera = deque()
        # PILA (LIFO): el ultimo atendido es el primero que se ve
        self._historial_atendidos = []

    def encolar(self, id_paciente, nombre):
        """Agregar un paciente al FINAL de la cola de espera."""
        # append() mete el elemento por el final: eso es "encolar"
        self._cola_espera.append(PacienteEspera(id_paciente, nombre))

    def atender_siguiente(self):
        """Saca al primer paciente de la cola y lo pasa al historial.

        Devuelve una lista [id, nombre], o None si no habia nadie esperando.
        """
        # Una coleccion vacia se evalua como False en un if
        if not self._cola_espera:
            print("La sala de espera esta vacia. No hay pacientes por atender.")
            # None avisa a main que no habia a quien atender
            return None
        # popleft() saca el PRIMERO de la cola (el que lleva mas tiempo esperando)
        paciente = self._cola_espera.popleft()
        # append() sobre la lista lo pone encima de la pila del historial
        self._historial_atendidos.append(paciente)
        # str() convierte el numero en texto
        return [str(paciente.id), paciente.nombre]

    def ver_espera(self):
        """Mostrar los pacientes que esperan, sin sacarlos de la cola."""
        print("\n--- Sala de espera (FIFO: primero en llegar, primero en ser atendido) ---")
        if not self._cola_espera:
            print("  No hay pacientes en espera.")
            # return sin valor termina el metodo aqui mismo
            return
        # Contador para numerar la posicion en la fila
        pos = 1
        # Recorrer la cola con for no la modifica
        for p in self._cola_espera:
            print("  " + str(pos) + ". ID: " + str(p.id) + " | " + p.nombre)
            pos += 1

    def ver_historial(self):
        """[Ronda 2] Ver historial de atendidos — stub pendiente."""
        print("[Pendiente Ronda 2] Ver historial de atendidos.")

    def deshacer_ultima_atencion(self):
        """[Ronda 2] Deshacer la ultima atencion — stub pendiente."""
        print("[Pendiente Ronda 2] Deshacer ultima atencion.")

    def contar_espera(self):
        """Cuantos pacientes hay esperando. len() da el tamano."""
        return len(self._cola_espera)

    def contar_atendidos(self):
        """Cuantos pacientes fueron atendidos en el turno."""
        return len(self._historial_atendidos)