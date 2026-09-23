"""
main.py - Punto de entrada del Sistema de Emergencias.

Este archivo orquesta las 3 estructuras de datos:
- DirectorioPacientes (Arbol BST) → est3
- SalaEspera (Cola + Pila) → est2
- GestionMedicos (Arreglo) → est1

IMPORTANTE: Este archivo se crea una sola vez y NO se vuelve a modificar.
Cada estudiante solo trabaja en su propio archivo.
"""

# 'from X import Y' trae la clase Y que vive en el archivo X.py.
# Es el equivalente de los 'import' de Java: sin estas tres lineas,
# este archivo no conoceria las clases de los companeros.
from directorio_pacientes import DirectorioPacientes
from sala_espera import SalaEspera
from gestion_medicos import GestionMedicos


def main():
    # Creamos el objeto que gestiona el directorio de pacientes (arbol BST)
    directorio = DirectorioPacientes()
    # Creamos el objeto que gestiona la sala de espera (cola) y el historial (pila)
    sala = SalaEspera()
    # Creamos el objeto que gestiona los medicos del hospital (arreglo)
    medicos = GestionMedicos()
    # Guarda la opcion elegida. Empieza en -1 para que entre al ciclo while.
    opcion = -1

    # Ciclo while: el menu se repite mientras el usuario no elija 0 (Salir)
    while opcion != 0:
        # print() escribe en pantalla y salta de linea. \n es un salto extra.
        print("\n==========================================")
        print("    SISTEMA DE EMERGENCIAS HOSPITALARIAS")
        print("==========================================")
        print("--- Pacientes (Arbol BST - est3) ---")
        print("  1. Llegada de paciente")
        print("  2. Buscar paciente por ID")
        print("  3. Ver todos los pacientes (ordenados)")
        print("  4. Eliminar paciente del directorio")
        print("  5. Paciente con ID menor / mayor")
        print("--- Atencion (Cola + Pila - est2) ---")
        print("  6. Atender siguiente paciente")
        print("  7. Ver sala de espera")
        print("  8. Ver historial de atendidos")
        print("  9. Deshacer ultima atencion")
        print("--- Medicos (Arreglo - est1) ---")
        print(" 10. Registrar medico")
        print(" 11. Ver medicos disponibles")
        print(" 12. Liberar medico")
        print("--- Estadisticas ---")
        print(" 13. Resumen general")
        print("  0. Salir")
        print("==========================================")

        # input() muestra el mensaje, espera a que el usuario escriba y
        # devuelve lo escrito como texto. end="" evita el salto de linea
        # para que el cursor quede junto al mensaje.
        entrada = input("Seleccione una opcion: ")

        # try-except: intenta convertir el texto a numero entero.
        # Si el usuario escribio letras, int() lanza un ValueError y
        # entramos en el except en vez de que el programa se caiga.
        try:
            opcion = int(entrada)
        except ValueError:
            print("Error: ingrese un numero valido.")
            # Ponemos -1 para que no ejecute ninguna opcion
            opcion = -1
            # continue salta al inicio del while, mostrando el menu de nuevo
            continue

        # === PACIENTES (est3: DirectorioPacientes) ===
        # Python no tiene switch: se usa una cadena de if / elif / else.
        if opcion == 1:
            # Pedimos al usuario el ID del paciente
            id_paciente = int(input("ID del paciente: "))
            # Pedimos el nombre del paciente
            nombre = input("Nombre del paciente: ")
            # Pedimos el motivo de la consulta
            motivo = input("Motivo de consulta: ")
            # Registrar en el directorio (arbol BST) — inserta ordenado por ID
            directorio.registrar(id_paciente, nombre, motivo)
            # Encolar en sala de espera — lo agrega al final de la cola FIFO
            sala.encolar(id_paciente, nombre)
            print("Paciente registrado y en sala de espera.")

        elif opcion == 2:
            # Pedimos el ID del paciente a buscar
            id_buscar = int(input("ID a buscar: "))
            # buscar() recorre el arbol BST y devuelve un texto con la informacion
            print(directorio.buscar(id_buscar))

        elif opcion == 3:
            print("\nPacientes registrados (ordenados por ID):")
            # mostrar_inorden() recorre el arbol en orden (izquierda, raiz, derecha)
            directorio.mostrar_inorden()

        elif opcion == 4:
            # Pedimos el ID del paciente a eliminar del arbol BST
            id_eliminar = int(input("ID del paciente a eliminar: "))
            # eliminar() busca y quita el nodo del arbol BST
            directorio.eliminar(id_eliminar)

        elif opcion == 5:
            # mostrar_min_max() muestra el paciente con el ID mas pequeno y el mas grande
            directorio.mostrar_min_max()

        # === ATENCION (est2: SalaEspera) ===
        elif opcion == 6:
            # atender_siguiente() saca al primero de la cola y lo apila en el historial.
            # Devuelve una lista [id, nombre] o None si la cola esta vacia.
            atendido = sala.atender_siguiente()
            # Verificamos si habia un paciente en la cola (si no es None)
            if atendido is not None:
                # atendido[0] es el ID y atendido[1] es el nombre
                print("Atendiendo a: " + atendido[1] + " (ID: " + atendido[0] + ")")
                # Asignar medico disponible — busca en el arreglo el primero libre
                medico_asignado = medicos.asignar_medico()
                # Si encontro un medico disponible (no es None)
                if medico_asignado is not None:
                    print("Medico asignado: " + medico_asignado)
                else:
                    # No habia ningun medico disponible en el arreglo
                    print("No hay medicos disponibles. Atencion sin medico asignado.")

        elif opcion == 7:
            # ver_espera() muestra todos los pacientes en la cola sin sacarlos
            sala.ver_espera()

        elif opcion == 8:
            # ver_historial() muestra la pila de atendidos (ultimo primero)
            sala.ver_historial()

        elif opcion == 9:
            # deshacer_ultima_atencion() saca el ultimo de la pila y lo regresa a la cola
            sala.deshacer_ultima_atencion()

        # === MEDICOS (est1: GestionMedicos) ===
        elif opcion == 10:
            # Pedimos el nombre del medico a registrar
            nombre_med = input("Nombre del medico: ")
            # Pedimos la especialidad del medico
            especialidad = input("Especialidad: ")
            # registrar() crea un nuevo medico y lo agrega a la lista
            medicos.registrar(nombre_med, especialidad)

        elif opcion == 11:
            # ver_disponibles() recorre la lista y muestra los medicos con disponible = True
            medicos.ver_disponibles()

        elif opcion == 12:
            # ver_ocupados() muestra los ocupados con un numero para seleccionarlos
            medicos.ver_ocupados()
            # Pedimos al usuario que elija cual medico liberar
            num_med = int(input("Numero del medico a liberar (0 para cancelar): "))
            # Si el usuario escribio un numero mayor a 0, liberamos ese medico
            if num_med > 0:
                # liberar() busca el medico ocupado en esa posicion y lo marca disponible
                medicos.liberar(num_med)

        # === ESTADISTICAS ===
        elif opcion == 13:
            # Resumen con los contadores de las 3 estructuras de datos
            print("\n--- RESUMEN GENERAL ---")
            # contar() cuenta recursivamente los nodos del arbol BST
            print("Pacientes registrados: " + str(directorio.contar()))
            # altura() calcula recursivamente la altura maxima del arbol
            print("Altura del directorio: " + str(directorio.altura()))
            # contar_espera() devuelve el tamano de la cola (cuantos esperan)
            print("En sala de espera: " + str(sala.contar_espera()))
            # contar_atendidos() devuelve el tamano de la pila (cuantos atendidos)
            print("Atendidos en el turno: " + str(sala.contar_atendidos()))
            # contar_disponibles() cuenta los medicos con disponible = True
            print("Medicos disponibles: " + str(medicos.contar_disponibles()))
            # contar_ocupados() cuenta los medicos con disponible = False
            print("Medicos ocupados: " + str(medicos.contar_ocupados()))

        elif opcion == 0:
            # El usuario eligio salir; mostramos mensaje de despedida
            print("Cerrando sistema de emergencias...")

        else:
            # Si el numero no corresponde a ninguna opcion valida del menu
            print("Opcion no valida.")


# Esta linea hace que main() se ejecute solo cuando el archivo se corre
# directamente (python src/main.py), y no cuando otro archivo lo importa.
if __name__ == "__main__":
    main()