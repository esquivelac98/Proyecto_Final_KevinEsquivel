import os
from modulo1 import ingresar_ventas, guardar_ventas, analizar_ventas


def limpiar_terminal():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPor favor presione Enter para continuar")


# Menú principal
def menu():
    ventas = []  # Lista para almacenar las ventas temporalmente
    while True:
        print("\n*** Menú Principal ***")
        print("1. Ingresar datos de ventas")
        print("2. Guardar datos en archivo CSV")
        print("3. Analizar datos de ventas")
        print("4. Salir")
        opcion = input("Por favor seleccione una opción del menú: ")

        if opcion == "1":
            limpiar_terminal()
            print("\n*** Ingreso de Ventas ***")
            ingresar_ventas(ventas)
            print(ventas)
            pausar()
        elif opcion == "2":
            limpiar_terminal()
            print("\n*** Guardar Ventas ***")
            guardar_ventas(ventas)
            #ventas = []
            pausar()
        elif opcion == "3":
            limpiar_terminal()
            print("\n*** Análisis de Ventas ***")
            analizar_ventas()
            pausar()
        elif opcion == "4":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor intente de nuevamente.")
            pausar()

# Ejecución del sistema solo si el archivo es el main
if __name__ == "__main__":
    limpiar_terminal()
    print("Bienvenido al sistema de gestión de ventas")
    pausar()
    menu()