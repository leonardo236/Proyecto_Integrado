# validaciones.py

def validar_fecha(fecha):
    # La fecha debe venir como: dd/mm/aaaa
    # Aquí separamos el texto por "/"
    partes = fecha.split("/")
    # Revisamos que tenga 3 partes y que cada parte tenga la longitud correcta
    return len(partes) == 3 and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 4

def validar_hora(hora):
    # La hora debe venir como: hh:mm
    partes = hora.split(":")
    # Revisamos que tenga dos partes y que sean números
    return len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit()

