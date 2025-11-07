# eventos.py

from datos import eventos, id_evento  # Importamos la lista y el contador de IDs
from validaciones import validar_fecha, validar_hora  # Importamos las funciones que revisan fecha y hora

def mostrar_eventos():
    # Si no hay eventos aún, se avisa al usuario
    if not eventos:
        print("No hay eventos registrados.")
    else:
        # Si sí hay, los mostramos uno por uno
        for e in eventos:
            print(f"[{e['id']}] {e['fecha']} - {e['hora']} | {e['titulo']} @ {e['lugar']}")

def agregar_evento():
    # Usamos 'global' para poder modificar el ID que viene de datos.py
    global id_evento

    # Pedimos al usuario la información del evento
    titulo = input("Título del evento: ")
    fecha = input("Fecha (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")
    lugar = input("Lugar: ")

    # Revisamos si la fecha y la hora están bien escritas
    if not validar_fecha(fecha):
        print("La fecha no tiene el formato correcto.")
        return
    if not validar_hora(hora):
        print("La hora no tiene el formato correcto.")
        return

    # Creamos el evento en forma de diccionario
    evento = {"id": id_evento, "titulo": titulo, "fecha": fecha, "hora": hora, "lugar": lugar}

    # Lo guardamos en la lista
    eventos.append(evento)

    # Aumentamos el ID para el siguiente evento
    id_evento += 1

    print("Evento agregado con éxito.\n")

def buscar_por_fecha():
    # Pedimos la fecha que queremos buscar
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")

    # Buscamos los eventos que tengan esa fecha
    encontrados = [e for e in eventos if e["fecha"] == fecha]

    # Si se encuentran eventos, se muestran
    if encontrados:
        for e in encontrados:
            print(f"[{e['id']}] {e['hora']} - {e['titulo']} @ {e['lugar']}")
    else:
        # Si no, avisamos
        print("No hay eventos en esa fecha.\n")

def editar_evento():
    # Primero mostramos todos los eventos para que el usuario vea los IDs
    mostrar_eventos()

    # Pedimos el ID del evento a editar
    try:
        id_editar = int(input("Ingrese el ID del evento a editar: "))
    except ValueError:
        # Si el usuario escribe letras en vez de números
        print("Debe ingresar un número.")
        return

    # Recorremos los eventos para buscar el que tenga ese ID
    for e in eventos:
        if e["id"] == id_editar:
            # Pedimos los nuevos datos
            nuevo_titulo = input("Nuevo título: ")
            nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
            nueva_hora = input("Nueva hora (hh:mm): ")
            nuevo_lugar = input("Nuevo lugar: ")

            # Validamos antes de guardar
            if validar_fecha(nueva_fecha) and validar_hora(nueva_hora):
                e["titulo"] = nuevo_titulo
                e["fecha"] = nueva_fecha
                e["hora"] = nueva_hora
                e["lugar"] = nuevo_lugar
                print("Evento actualizado.\n")
            else:
                print("Los datos ingresados no son válidos.\n")
            return

    # Si no se encontró el ID
    print("El ID ingresado no existe.\n")

def eliminar_evento():
    # Mostramos eventos para que el usuario vea los IDs disponibles
    mostrar_eventos()

    # Pedimos ID
    try:
        id_eliminar = int(input("Ingrese el ID del evento a eliminar: "))
    except ValueError:
        print("Debe ingresar un número.")
        return

    # Buscamos el evento
    for e in eventos:
        if e["id"] == id_eliminar:
            eventos.remove(e)  # Lo borramos
            print("Evento eliminado.\n")
            return

    print("El ID ingresado no existe.\n")

