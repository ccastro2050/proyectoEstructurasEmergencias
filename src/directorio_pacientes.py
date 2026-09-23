"""
directorio_pacientes.py - Directorio de pacientes usando ARBOL BINARIO DE BUSQUEDA.

Responsable: est3
Estructura de datos: Arbol BST (menores a la izquierda, mayores a la derecha)

Ronda 1: registrar, buscar, mostrar inorden, contar.
Los metodos eliminar, mostrar_min_max y altura quedan como stubs
y se implementan en la Ronda 2.
"""


class Nodo:
    """Un NODO del arbol: un paciente y sus dos ramas.

    Es la pieza basica del BST: cada nodo apunta a otros dos nodos (o a None).
    """

    def __init__(self, id_paciente, nombre, motivo):
        # ID del paciente: es la CLAVE que ordena el arbol
        self.id = id_paciente
        self.nombre = nombre
        self.motivo = motivo
        # Un nodo nuevo siempre nace como hoja: sin hijos
        self.izquierdo = None   # pacientes con ID MENOR
        self.derecho = None     # pacientes con ID MAYOR


class DirectorioPacientes:
    def __init__(self):
        # Primer nodo del arbol. Si vale None, el directorio esta vacio.
        self._raiz = None

    def registrar(self, id_paciente, nombre, motivo):
        """Registrar un paciente en el arbol.

        La asignacion 'self._raiz =' es imprescindible: cuando el arbol esta
        vacio, la raiz vale None y la unica forma de que apunte al nodo nuevo
        es que la recursion lo devuelva y aqui se guarde.
        """
        self._raiz = self._insertar_recursivo(self._raiz, id_paciente, nombre, motivo)

    def _insertar_recursivo(self, actual, id_paciente, nombre, motivo):
        """Busca el sitio libre donde colgar el nodo nuevo.

        El guion bajo inicial avisa que es un metodo interno de la clase.
        Devuelve el nodo que debe quedar en esta posicion del arbol.
        """
        # CASO BASE: llegamos a un sitio vacio, aqui va el paciente nuevo
        if actual is None:
            return Nodo(id_paciente, nombre, motivo)

        # Si el ID es menor, el sitio esta en la rama izquierda.
        # El resultado se vuelve a enganchar, porque la recursion
        # devuelve la rama ya actualizada.
        if id_paciente < actual.id:
            actual.izquierdo = self._insertar_recursivo(actual.izquierdo, id_paciente, nombre, motivo)
        elif id_paciente > actual.id:
            # Si el ID es mayor, el sitio esta en la rama derecha
            actual.derecho = self._insertar_recursivo(actual.derecho, id_paciente, nombre, motivo)
        else:
            # Si es igual, el paciente ya estaba: no se admiten IDs repetidos
            print("El paciente con ID " + str(id_paciente) + " ya existe en el directorio.")

        # Devolvemos este nodo, ya con su rama actualizada
        return actual

    def buscar(self, id_paciente):
        """Buscar un paciente por su ID y devolver un texto con su informacion."""
        resultado = self._buscar_recursivo(self._raiz, id_paciente)
        if resultado is None:
            return "Paciente con ID " + str(id_paciente) + " no encontrado."
        return ("ID: " + str(resultado.id) + " | Nombre: " + resultado.nombre
                + " | Motivo: " + resultado.motivo)

    def _buscar_recursivo(self, actual, id_paciente):
        """Baja por UNA sola rama comparando en cada nodo.

        Por eso la busqueda es rapida: nunca revisa las dos ramas.
        """
        # CASO BASE: se acabo la rama y no estaba
        if actual is None:
            return None
        # CASO BASE: lo encontramos
        if id_paciente == actual.id:
            return actual
        # Si el ID buscado es menor, seguimos por la izquierda
        if id_paciente < actual.id:
            return self._buscar_recursivo(actual.izquierdo, id_paciente)
        # Si no, por la derecha
        return self._buscar_recursivo(actual.derecho, id_paciente)

    def mostrar_inorden(self):
        """Mostrar todos los pacientes ordenados de menor a mayor ID."""
        if self._raiz is None:
            print("  El directorio esta vacio.")
            return
        self._inorden_recursivo(self._raiz)

    def _inorden_recursivo(self, nodo):
        """Recorrido INORDEN: Izquierda → Raiz → Derecha.

        Este orden es el que hace que los datos salgan ordenados.
        """
        if nodo is not None:
            # 1. Primero toda la rama izquierda (los IDs menores)
            self._inorden_recursivo(nodo.izquierdo)
            # 2. Despues este nodo
            print("  ID: " + str(nodo.id) + " | " + nodo.nombre + " | " + nodo.motivo)
            # 3. Y al final toda la rama derecha (los IDs mayores)
            self._inorden_recursivo(nodo.derecho)

    def eliminar(self, id_paciente):
        """[Ronda 2] Eliminar un paciente — stub pendiente."""
        print("[Pendiente Ronda 2] Eliminar paciente ID: " + str(id_paciente))

    def mostrar_min_max(self):
        """[Ronda 2] Mostrar ID menor y mayor — stub pendiente."""
        print("[Pendiente Ronda 2] Mostrar paciente con ID menor y mayor.")

    def contar(self):
        """Contar cuantos pacientes hay en el directorio."""
        return self._contar_recursivo(self._raiz)

    def _contar_recursivo(self, nodo):
        """Este nodo cuenta 1, mas todo lo que haya en sus dos ramas."""
        # CASO BASE: no hay nodo, no se cuenta nada
        if nodo is None:
            return 0
        return 1 + self._contar_recursivo(nodo.izquierdo) + self._contar_recursivo(nodo.derecho)

    def altura(self):
        """[Ronda 2] Altura del arbol — stub pendiente."""
        return 0