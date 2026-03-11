# ---------------------------------
# MÓDULO: usuarios.py
# Funciones de gestión de usuarios
# ---------------------------------

import random

usuarios = []


def crear_usuarios():
    """
    Crea una lista de 10 usuarios con datos de ejemplo.
    Cada usuario contiene: id, nombre, documento, estrato, consumos, estado
    """
    
    global usuarios

    for i in range(10):

        consumos = []

        for j in range(30):
            consumo = random.randint(100, 500)
            consumos.append(consumo)

        usuario = {
            "id": i + 1,
            "nombre": "Usuario" + str(i + 1),
            "documento": random.randint(10000000, 99999999),
            "estrato": random.randint(1, 6),
            "consumos": consumos,
            "estado": "ACTIVO"
        }

        usuarios.append(usuario)


def calcular_consumo_total(consumos):
    """
    Calcula el consumo total de energía de una lista de consumos.
    """
    
    total = 0
    for consumo in consumos:
        total = total + consumo
    return total


def mostrar_usuarios():
    """
    Muestra en pantalla los datos de cada usuario y su consumo total.
    """

    print("\n" + "="*80)
    print("INFORMACIÓN DE USUARIOS Y CONSUMO ENERGÉTICO")
    print("="*80)

    for usuario in usuarios:

        total_consumo = calcular_consumo_total(usuario["consumos"])

        print("ID:", usuario["id"])
        print("Nombre:", usuario["nombre"])
        print("Documento:", usuario["documento"])
        print("Estrato:", usuario["estrato"])
        print("Consumo total:", total_consumo)
        print("Consumo promedio diario:", total_consumo / 30)
        print("Estado:", usuario["estado"])
        print("-------------------------")


def ordenar_por_consumo():
    """
    Ordena los usuarios de menor a mayor según el consumo total de energía.
    """

    global usuarios
    cantidad = len(usuarios)

    for i in range(cantidad):
        for j in range(i + 1, cantidad):

            consumo_i = calcular_consumo_total(usuarios[i]["consumos"])
            consumo_j = calcular_consumo_total(usuarios[j]["consumos"])

            if consumo_i > consumo_j:

                temporal = usuarios[i]
                usuarios[i] = usuarios[j]
                usuarios[j] = temporal

    print("\n" + "="*80)
    print("USUARIOS ORDENADOS POR CONSUMO (MENOR A MAYOR)")
    print("="*80 + "\n")
    mostrar_usuarios()
