# ---------------------------------
# MÓDULO: menu.py
# Menú principal del sistema
# ---------------------------------

from usuarios import mostrar_usuarios, ordenar_por_consumo


def menu_principal():
    """
    Muestra un menú con opciones principales:
    - Mostrar usuarios
    - Ordenar usuarios por consumo
    - Salir
    """

    while True:

        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Mostrar usuarios")
        print("2. Ordenar usuarios por consumo")
        print("3. Salir")
        print("="*50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_usuarios()

        elif opcion == "2":
            ordenar_por_consumo()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")
