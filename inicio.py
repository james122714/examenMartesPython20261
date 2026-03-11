# ---------------------------------
# ARCHIVO PRINCIPAL: inicio.py
# Punto de entrada del sistema
# ---------------------------------

from autenticacion import registrar_usuario, iniciar_sesion
from usuarios import crear_usuarios
from menu import menu_principal


def main():
    """
    Controla el flujo principal del programa.
    """

    print("\n" + "="*50)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN ENERGÉTICA")
    print("="*50)
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("="*50)
    print("Usuario de prueba: admin@sistema.com / 1234")
    print("="*50)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
        print("Ahora intente iniciar sesión con sus credenciales.\n")

    acceso = iniciar_sesion()

    if acceso == True:
        crear_usuarios()
        menu_principal()
    else:
        print("No se pudo acceder al sistema. El programa se cerrará.")


# ---------------------------------
# PUNTO DE ENTRADA
# ---------------------------------
if __name__ == "__main__":
    main()

    #
    #PROMT CON EL CUAL HICE UNA PARTE Necesito generar un programa en Python para un taller académico.

#El programa debe usar únicamente programación estructurada con funciones definidas usando "def". No debe usar programación orientada a objetos ni funciones lambda.

#El sistema debe tener las siguientes funciones:

#main()

#Controla el flujo principal del programa.

#registrar_usuario()

#Permite registrar un usuario con correo y contraseña.

#Los datos se guardan en una lista de diccionarios.

#iniciar_sesion()

#Solicita correo y contraseña.

#Permite máximo 3 intentos de acceso.

#Si el login es correcto retorna True.

#Si se agotan los intentos muestra "Cuenta bloqueada temporalmente".

#crear_usuarios()

#Crea una lista llamada usuarios con 10 diccionarios.

#Cada diccionario debe contener:
id
#nombre
#documento
#estrato
#consumos (lista de 30 valores numéricos de consumo energético)
#estado

#mostrar_usuarios()

#Muestra en pantalla los datos de cada usuario y su consumo total.

#ordenar_por_consumo()

#Ordena los usuarios de menor a mayor según el consumo total de energía.

#menu_principal()

#Debe mostrar un menú con opciones:

#Mostrar usuarios

#Ordenar usuarios por consumo

#Salir

#El programa debe usar listas, diccionarios y estructuras de control básicas (for, while, if).

#El archivo principal debe llamarse "inicio.py".
    #