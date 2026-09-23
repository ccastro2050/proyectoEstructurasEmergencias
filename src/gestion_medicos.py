"""
gestion_medicos.py - Gestiona los medicos del hospital usando ARREGLOS.

Responsable: est1
Estructura de datos: list (arreglo dinamico de Python)

Cada medico tiene: nombre, especialidad, y un estado (disponible/ocupado).
Se usa una lista porque la cantidad de medicos es variable pero
no necesitamos busqueda rapida por clave (no es un arbol).

Ronda 1: registrar, ver disponibles, contar.
Los metodos asignar_medico, ver_ocupados y liberar quedan como stubs
y se implementan en la Ronda 2.
"""


class Medico:
    """Representa un medico del hospital.

    En Python pueden convivir varias clases en el mismo archivo; esta se
    declara junto a GestionMedicos porque solo se usa aqui.
    """

    def __init__(self, nombre, especialidad):
        # self.nombre es el atributo del objeto; nombre es el parametro recibido
        self.nombre = nombre
        self.especialidad = especialidad
        # Todo medico nuevo empieza como disponible
        self.disponible = True


class GestionMedicos:
    def __init__(self):
        # Lista que almacena todos los objetos Medico del hospital
        self._medicos = []

    def registrar(self, nombre, especialidad):
        """Registrar un nuevo medico (disponible por defecto)."""
        # append() agrega el elemento al final de la lista
        self._medicos.append(Medico(nombre, especialidad))
        # El signo + une textos
        print("Medico registrado: " + nombre + " (" + especialidad + ")")

    def asignar_medico(self):
        """[Ronda 2] Asignar el primer medico disponible."""
        # Este metodo es un stub: solo imprime un mensaje y devuelve None
        print("[Pendiente Ronda 2] Asignar medico.")
        return None

    def ver_disponibles(self):
        """Mostrar medicos disponibles recorriendo toda la lista."""
        print("\n--- Medicos disponibles ---")
        # Contador para numerar los medicos disponibles que encontramos
        cont = 0
        # 'for m in lista' recorre la lista elemento por elemento.
        # Es mas simple que el for con indice de Java o C#.
        for m in self._medicos:
            if m.disponible:
                # Incrementamos el contador para numerar la lista mostrada
                cont += 1
                print("  " + str(cont) + ". " + m.nombre + " (" + m.especialidad + ")")
        # Si el contador quedo en 0, ningun medico esta disponible
        if cont == 0:
            print("  No hay medicos disponibles.")

    def ver_ocupados(self):
        """[Ronda 2] Mostrar medicos ocupados — stub pendiente."""
        print("[Pendiente Ronda 2] Ver medicos ocupados.")

    def liberar(self, numero):
        """[Ronda 2] Liberar un medico — stub pendiente."""
        print("[Pendiente Ronda 2] Liberar medico.")

    def contar_disponibles(self):
        """Contar cuantos medicos estan disponibles."""
        cont = 0
        for m in self._medicos:
            if m.disponible:
                cont += 1
        return cont

    def contar_ocupados(self):
        """Contar cuantos medicos estan ocupados."""
        cont = 0
        for m in self._medicos:
            # 'not' invierte la condicion: cuenta los que NO estan disponibles
            if not m.disponible:
                cont += 1
        return cont