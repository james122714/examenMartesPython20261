# ---------------------------------
# MÓDULO: autenticacion.py
# Funciones de registro e inicio de sesión
# ---------------------------------

usuarios_registrados = [
    {"correo": "admin@sistema.com", "password": "1234"}
]


def registrar_usuario():
    """
    Permite registrar un nuevo usuario con correo y contraseña.
    Los datos se guardan en una lista de diccionarios.
    """
    
    correo = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")

    usuario = {
        "correo": correo,
        "password": password
    }

    usuarios_registrados.append(usuario)

    print("Usuario registrado correctamente\n")


def iniciar_sesion():
    """
    Solicita correo y contraseña con máximo 3 intentos.
    Retorna True si el login es correcto.
    Si se agotan los intentos muestra "Cuenta bloqueada temporalmente".
    """

    intentos = 3

    while intentos > 0:

        correo = input("Correo: ")
        password = input("Contraseña: ")

        for usuario in usuarios_registrados:

            if usuario["correo"] == correo and usuario["password"] == password:

                print("Login exitoso\n")
                return True

        intentos -= 1
        if intentos > 0:
            print("Credenciales incorrectas. Intentos restantes:", intentos)

    print("Cuenta bloqueada temporalmente")
    return False
