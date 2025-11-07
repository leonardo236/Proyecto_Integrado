# main.py

# Importamos todas las funciones que ya hicimos
from eventos import agregar_evento, mostrar_eventos, buscar_por_fecha, editar_evento, eliminar_evento

def main():
    # Este ciclo mantiene el programa corriendo hasta que el usuario elija salir
    while True:
        print("\n===== AGENDA PERSONAL=====")
        print("1. Agregar evento")
        print("2. Ver eventos")
        print("3. Buscar por fecha")
        print("4. Editar evento")
        print("5. Eliminar evento")
        print("0. Salir")

        # Pedimos al usuario qué opción quiere
        opcion = input("Seleccione una opción: ")

        # Dependiendo de la opción se llama la función correspondiente
        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            mostrar_eventos()
        elif opcion == "3":
            buscar_por_fecha()
        elif opcion == "4":
            editar_evento()
        elif opcion == "5":
            eliminar_evento()
        elif opcion == "0":
            # Si desea salir, se rompe el ciclo
            print("Gracias por usar la agenda.")
            break
        else:
            # Si escribe algo inválido
            print("Opción no válida.\n")

# Aquí iniciamos el programa llamando al menú
main()

