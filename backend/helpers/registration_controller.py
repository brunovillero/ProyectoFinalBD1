import helpers.database

def register_user(data):
    try:
        validate(data)
        return data
    except Exception as error:
        return str(error)

def validate(data):
    if not(data["ci"]) or data["ci"] == "":
        raise Exception("Cedula requerida")

    if not(data["nombre"]) or data["nombre"] == "":
        raise Exception("Nombre requerido")

    if not(data["apellido"]) or data["apellido"] == "":
        raise Exception("Apellido requerido")

    if not(data["fecha_de_nacimiento"]) or data["fecha_de_nacimiento"] == "":
        raise Exception("Fecha de nacimiento requerido")

    if not(data["domicilio"]) or data["domicilio"] == "":
        raise Exception("Domicilio requerido")

    if not(data["email"]) or data["email"] == "":
        raise Exception("Email requerido")

    if not(data["telefono"]) or data["telefono"] == "":
        raise Exception("Telefono requerido")

    if not(data["password"]) or data["password"] == "":
       raise Exception("Password requerido")