# ==========================================================
# PROYECTO: AGENDA PERSONAL 
# Desarrollado en Python
#
# ==========================================================

# Importamos la clase datetime para trabajar con fechas y horas.
from datetime import datetime

# Se crea una lista vacía llamada 'eventos' donde se guardarán todos los registros creados.
eventos = []

# Se crea una variable 'id_evento' que servirá para asignar un número único a cada evento.
id_evento = 1


# ----------------------------------------------------------
# FUNCIÓN: validar_fecha
# Verifica que la fecha ingresada tenga el formato correcto (dd/mm/aaaa).
# Si el formato es válido, devuelve True; si no, devuelve False.
# ----------------------------------------------------------
def validar_fecha(fecha):
    try:
        # Se intenta convertir la cadena de texto a una fecha real.
        datetime.strptime(fecha, "%d/%m/%Y")
        return True  # Si funciona, devuelve True (válida)
    except ValueError:
        # Si ocurre un error, la fecha no es válida.
        return False


# ----------------------------------------------------------
# FUNCIÓN: validar_hora
# Comprueba que la hora esté escrita correctamente (hh:mm).
# Devuelve True si es válida o False si está mal escrita.
# ----------------------------------------------------------
def validar_hora(hora):
    try:
        # Se intenta convertir el texto a una hora real.
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        # Si da error, la hora no cumple el formato correcto.
        return False


# ----------------------------------------------------------
# FUNCIÓN: agregar_evento
# Pide al usuario los datos de un nuevo evento y los guarda si todo está correcto.
# ----------------------------------------------------------
def agregar_evento():
    global id_evento  # Permite usar la variable global dentro de la función.

    print("\n=== Agregar nuevo evento ===")  # Muestra título de la sección.

    # Se solicita el título del evento.
    titulo = input("Título del evento: ").strip()  # El método strip() quita espacios innecesarios.

    # Si el usuario deja el campo vacío, se repite hasta que escriba algo.
    while not titulo:
        print("El título no puede estar vacío.")
        titulo = input("Título del evento: ").strip()

    # Se solicita la fecha y se valida el formato.
    fecha = input("Fecha (dd/mm/aaaa): ").strip()
    while not validar_fecha(fecha):
        print("Formato de fecha inválido. Ejemplo correcto: 25/10/2025")
        fecha = input("Fecha (dd/mm/aaaa): ").strip()

    # Se solicita la hora y se valida también.
    hora = input("Hora (hh:mm): ").strip()
    while not validar_hora(hora):
        print("Formato de hora inválido. Ejemplo correcto: 08:30")
        hora = input("Hora (hh:mm): ").strip()

    # Se solicita el lugar del evento (opcional).
    lugar = input("Lugar del evento (opcional): ").strip()

    # Se agrupan todos los datos en un diccionario (como una "ficha").
    evento = {
        "id": id_evento,
        "titulo": titulo,
        "fecha": fecha,
        "hora": hora,
        "lugar": lugar
    }

    # Se agrega la ficha del evento a la lista general.
    eventos.append(evento)

    # Se incrementa el número del ID para el próximo evento.
    id_evento += 1

    print("Evento agregado correctamente.\n")  # Confirmación al usuario.


# ----------------------------------------------------------
# FUNCIÓN: ver_eventos
# Muestra todos los eventos registrados en pantalla.
# ----------------------------------------------------------
def ver_eventos():
    print("\n=== Lista de eventos ===")  # Encabezado de la lista.

    # Si la lista está vacía, se informa al usuario.
    if not eventos:
        print("No hay eventos registrados.\n")
    else:
        # Se recorre cada evento dentro de la lista y se muestran sus datos.
        for e in eventos:
            print(f"[{e['id']}] {e['fecha']} {e['hora']} - {e['titulo']} @ {e['lugar']}")
        print("")  # Salto de línea para separar la información.


# ----------------------------------------------------------
# FUNCIÓN: buscar_por_fecha
# Permite consultar los eventos de una fecha específica.
# ----------------------------------------------------------
def buscar_por_fecha():
    # El usuario escribe una fecha para buscar.
    f = input("\nIngrese la fecha a consultar (dd/mm/aaaa): ").strip()

    # Primero se verifica si la fecha tiene el formato correcto.
    if not validar_fecha(f):
        print("Fecha inválida. Intente nuevamente.\n")
        return  # Se sale de la función si la fecha no es válida.

    # Se crea una nueva lista con todos los eventos que coinciden con esa fecha.
    encontrados = [e for e in eventos if e["fecha"] == f]

    # Si se encontraron resultados, se muestran en pantalla.
    if encontrados:
        print("\n=== Eventos en esa fecha ===")
        for e in encontrados:
            print(f"[{e['id']}] {e['hora']} - {e['titulo']} @ {e['lugar']}")
    else:
        # Si no se encontró nada, se muestra un mensaje.
        print("No hay eventos registrados en esa fecha.\n")


# ----------------------------------------------------------
# FUNCIÓN: editar_evento
# Permite modificar los datos de un evento existente utilizando su ID.
# ----------------------------------------------------------
def editar_evento():
    # Si no hay eventos registrados, no se puede editar nada.
    if not eventos:
        print("\nNo hay eventos para editar.\n")
        return

    # Se pide al usuario el ID del evento que quiere editar.
    try:
        id_buscar = int(input("\nIngrese el ID del evento que desea editar: "))
    except ValueError:
        print("Debe ingresar un número válido.")  # Si no es número, muestra error.
        return

    # Se busca dentro de la lista el evento que tenga ese mismo ID.
    for e in eventos:
        if e["id"] == id_buscar:
            print(f"\nEditando evento: {e['titulo']}")  # Muestra el evento que se va a modificar.

            # Se pide un nuevo título; si se deja vacío, mantiene el anterior.
            nuevo_titulo = input("Nuevo título (enter para mantener el actual): ").strip()
            if nuevo_titulo:
                e["titulo"] = nuevo_titulo

            # Se pide una nueva fecha.
            nueva_fecha = input("Nueva fecha (dd/mm/aaaa, enter para mantener): ").strip()
            if nueva_fecha:
                if validar_fecha(nueva_fecha):
                    e["fecha"] = nueva_fecha
                else:
                    print("Fecha inválida. No se cambió la fecha.")

            # Se pide una nueva hora.
            nueva_hora = input("Nueva hora (hh:mm, enter para mantener): ").strip()
            if nueva_hora:
                if validar_hora(nueva_hora):
                    e["hora"] = nueva_hora
                else:
                    print("Hora inválida. No se cambió la hora.")

            # Se pide un nuevo lugar.
            nuevo_lugar = input("Nuevo lugar (enter para mantener): ").strip()
            if nuevo_lugar:
                e["lugar"] = nuevo_lugar

            print("Evento editado correctamente.\n")
            return  # Termina la función después de editar.

    # Si no se encuentra el ID buscado, se informa al usuario.
    print("No se encontró un evento con ese ID.\n")


# ----------------------------------------------------------
# FUNCIÓN: eliminar_evento
# Permite eliminar un evento según su ID.
# ----------------------------------------------------------
def eliminar_evento():
    # Si no hay eventos, no hay nada que eliminar.
    if not eventos:
        print("\nNo hay eventos para eliminar.\n")
        return

    # Se pide el ID del evento a eliminar.
    try:
        id_eliminar = int(input("\nIngrese el ID del evento a eliminar: "))
    except ValueError:
        print("Debe ingresar un número válido.")  # Si no es número, muestra error.
        return

    # Se busca el evento y se elimina si se encuentra.
    for e in eventos:
        if e["id"] == id_eliminar:
            eventos.remove(e)
            print("Evento eliminado correctamente.\n")
            return

    # Si el ID no existe, se muestra un mensaje.
    print("No se encontró un evento con ese ID.\n")


# ----------------------------------------------------------
# FUNCIÓN: menu
# Es la parte principal del programa.
# Muestra las opciones disponibles y llama a la función correspondiente según la elección del usuario.
# ----------------------------------------------------------
def menu():
    while True:  # Bucle infinito hasta que el usuario elija salir.
        print("=== AGENDA PERSONAL ===")
        print("1. Agregar evento")
        print("2. Ver eventos")
        print("3. Buscar por fecha")
        print("4. Editar evento")
        print("5. Eliminar evento")
        print("0. Salir")

        # Se pide al usuario una opción del menú.
        opcion = input("Seleccione una opción: ").strip()

        # Validación: solo acepta números del 0 al 5.
        if opcion not in ["0", "1", "2", "3", "4", "5"]:
            print("Opción inválida. Intente nuevamente.\n")
            continue

        # Dependiendo de la opción, se llama a la función correspondiente.
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
            print("Gracias por usar la Agenda Personal .")
            break  # Sale del bucle y finaliza el programa.


# ----------------------------------------------------------
# INICIO DEL PROGRAMA
# Esta parte hace que el programa empiece automáticamente al ejecutarlo.
# ----------------------------------------------------------
if __name__ == "__main__":
    menu()  # Llama a la función principal del menú.
