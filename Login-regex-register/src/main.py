from registrerUser import cargar_usuarios, userExists, createUser, validateInputs, guardar_usuarios

def registrar_usuario():
    usuarios = cargar_usuarios()

    print("=== Registro de Usuario ===")

    name = input("Nombre: ").strip()
    surname = input("Apellido: ").strip()
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    user_exist = userExists(email, password)

    if user_exist[0]:
        print("✘ El usuario ya existe. Intenta con otro email.")
        return 
    
    if not validateInputs(name, surname, email, password):
        print("✘ Datos inválidos. Asegúrate de completar todos los campos correctamente.")
        return 
    
    nuevo_usuario = createUser(name, surname, email, password)

    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    print("✔ Usuario registrado con éxito.")


def main():
    """Menú principal de la terminal."""
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar usuario")
        print("2. Salir")
        
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
