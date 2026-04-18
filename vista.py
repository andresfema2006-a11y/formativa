from controlador import registrar_usuario, obtener_usuarios, login

def menu():
    while True:
        print("\n1. Registrar")
        print("2. Mostrar usuarios")
        print("3. Login")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")
            password = input("Ingrese contraseña: ")

            mensaje = registrar_usuario(nombre, correo, password)
            print(mensaje)

        elif opcion == "2":
            usuarios = obtener_usuarios()
            if len(usuarios) == 0:
                print("No hay usuarios")
            else:
                for u in usuarios:
                    print(f"Nombre: {u['nombre']} - Correo: {u['correo']}")

        elif opcion == "3":
            correo = input("Correo: ")
            password = input("Contraseña: ")

            mensaje = login(correo, password)
            print(mensaje)

        elif opcion == "4":
            print("Fin del programa")
            break

        else:
            print("Opción inválida")
