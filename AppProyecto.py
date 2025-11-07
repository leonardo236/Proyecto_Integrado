# ============================================================
# PROYECTO: Agenda Personal 
# NOMBRE : Agenda Fast
#  
#
# 
#   
#   
#
# 
# 
# ============================================================

import sys
from datetime import datetime

# Lista global para almacenar los eventos en memoria
eventos = []

# Contador incremental que asigna un ID único a cada evento
id_evento = 1


# ------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# ------------------------------------------------------------

def validar_fecha(fecha):
    """
    Valida que una fecha tenga el formato correcto (dd/mm/aaaa)
    y que sea una fecha real.
    Retorna True si la fecha es válida, False en caso contrario.
    """
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_hora(hora):
    """
    Valida que la hora tenga el formato correcto (hh:mm)
    en formato de 24 horas.
    Retorna True si la hora es válida, False en caso contrario.
    """
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


# ------------------------------------------------------------
# FUNCIONES PRINCIPALES
# ------------------------------------------------------------

def agregar_evento():
    """
    Permite al usuario registrar un nuevo evento en la agenda.
    Solicita título, fecha, hora y lugar (opcional).
    Todos los datos se validan antes de guardar.
    """
    global id_evento

    print("\n--- Agregar nuevo evento ---")

    titulo = input("Título del evento: ").strip()
    if not titulo:
        print("Error: el título no puede estar vacío.")
        return

    fecha = input("Fecha (dd/mm/aaaa): ").strip()
    if not validar_fecha(fecha):
        print("Error: formato de fecha incorrecto. Use dd/mm/aaaa.")
        return

    hora = input("Hora (hh:mm): ").strip()
    if not validar_hora(hora):
        print("Error: formato de hora incorrecto. Use hh:mm en formato 24h.")
        return

    lugar = input("Lugar (opcional): ").strip() or "No especificado"

    evento = {
        "id": id_evento,
        "titulo": titulo,
        "fecha": fecha,
        "hora": hora,
        "lugar": lugar
    }

    eventos.append(evento)
    id_evento += 1
    print("Evento agregado correctamente.")


def ver_eventos():
    """
    Muestra todos los eventos registrados en la agenda.
    Si la lista está vacía, se informa al usuario.
    """
    print("\n--- Lista de eventos ---")
    if not eventos:
        print("No hay eventos registrados.")
        return

    for e in eventos:
        print(f"[{e['id']}] {e['fecha']} {e['hora']} - {e['titulo']} @ {e['lugar']}")


def buscar_por_fecha():
    """
    Permite buscar eventos que coincidan con una fecha específica.
    La fecha ingresada debe estar en formato dd/mm/aaaa.
    """
    fecha = input("Ingrese una fecha (dd/mm/aaaa): ").strip()

    if not validar_fecha(fecha):
        print("Error: formato de fecha incorrecto.")
        return

    encontrados = [e for e in eventos if e["fecha"] == fecha]

    if encontrados:
        print("\nEventos encontrados:")
        for e in encontrados:
            print(f"[{e['id']}] {e['hora']} - {e['titulo']} @ {e['lugar']}")
    else:
        print("No hay eventos registrados para esa fecha.")


def editar_evento():
    """
    Permite modificar los datos de un evento existente.
    El usuario debe ingresar el ID del evento a editar.
    Si el ID no existe o el valor ingresado no es válido,
    se informa el error sin interrumpir el programa.
    """
    try:
        eid = int(input("Ingrese el ID del evento a editar: "))
        evento = next(e for e in eventos if e["id"] == eid)
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return
    except StopIteration:
        print("Error: no se encontró ningún evento con ese ID.")
        return

    print("\n--- Editar evento ---")
    nuevo_titulo = input(f"Título ({evento['titulo']}): ").strip() or evento['titulo']
    nueva_fecha = input(f"Fecha ({evento['fecha']}): ").strip() or evento['fecha']
    nueva_hora = input(f"Hora ({evento['hora']}): ").strip() or evento['hora']
    nuevo_lugar = input(f"Lugar ({evento['lugar']}): ").strip() or evento['lugar']

    if not validar_fecha(nueva_fecha):
        print("Error: la fecha ingresada no es válida.")
        return
    if not validar_hora(nueva_hora):
        print("Error: la hora ingresada no es válida.")
        return

    evento.update({
        "titulo": nuevo_titulo,
        "fecha": nueva_fecha,
        "hora": nueva_hora,
        "lugar": nuevo_lugar
    })

    print("El evento ha sido actualizado correctamente.")


def eliminar_evento():
    """
    Permite eliminar un evento existente según su ID.
    Si el ID no existe o no es válido, se muestra un mensaje de error.
    """
    try:
        eid = int(input("Ingrese el ID del evento a eliminar: "))
        global eventos
        eventos = [e for e in eventos if e["id"] != eid]
        print("El evento ha sido eliminado.")
    except ValueError:
        print("Error: el ID debe ser un número entero.")


# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL (MENÚ)
# ------------------------------------------------------------

def main():
    """
    Muestra el menú principal del programa y gestiona
    la interacción con el usuario.
    Cada opción llama a la función correspondiente.
    """
    while True:
        print("\n===== AGENDA PERSONAL =====")
        print("1. Agregar evento")
        print("2. Ver eventos")
        print("3. Buscar por fecha")
        print("4. Editar evento")
        print("5. Eliminar evento")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            ver_eventos()
        elif opcion == "3":
            buscar_por_fecha()
        elif opcion == "4":
            editar_evento()
        elif opcion == "5":
            eliminar_evento()
        elif opcion == "0":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.")


# ------------------------------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
