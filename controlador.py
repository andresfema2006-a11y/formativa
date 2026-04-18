from modelo import usuarios

def registrar_usuario(nombre, correo, password):
    if nombre == "":
        return "El nombre está vacío"
    if correo == "":
        return "El correo está vacío"
    if "@" not in correo:
        return "Correo inválido"
    if len(password) < 4:
        return "La contraseña es muy corta"

    for u in usuarios:
        if u["correo"] == correo:
            return "El correo ya existe"

    usuarios.append({
        "nombre": nombre,
        "correo": correo,
        "password": password
    })

    return "Usuario registrado con éxito"


def obtener_usuarios():
    return usuarios


def login(correo, password):
    for u in usuarios:
        if u["correo"] == correo:
            if u["password"] == password:
                return f"Bienvenido {u['nombre']}"
            else:
                return "Contraseña incorrecta"

    return "Usuario no encontrado"