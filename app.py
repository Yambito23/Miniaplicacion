import json
from pathlib import Path
from seguridad import crear_hash, verificar_clave
from datetime import datetime

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "inventario.json"
USUARIOS = RAIZ / "usuarios.json"
LOG = RAIZ / "auditoria.jsonl"



def cargar_inventario():
    try:
        return json.loads(DATOS.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Error: el archivo de inventario no existe.")
        return None
    except json.JSONDecodeError:
        print("Error: el archivo de inventario contiene JSON inválido.")
        return None



def guardar_inventario(productos):
    DATOS.write_text(json.dumps(productos, indent=2), encoding="utf-8")


def registrar_evento(usuario, accion, resultado, **detalles):
    evento = {
        "fecha_hora": datetime.now().astimezone().isoformat(timespec="seconds"),
        "usuario": usuario,
        "accion": accion,
        "resultado": resultado
    }

    evento.update(detalles)

    with LOG.open("a", encoding="utf-8") as archivo:
        archivo.write(json.dumps(evento) + "\n")



def autenticar(nombre, clave):
    usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))

    for usuario in usuarios:
        if usuario["usuario"] == nombre:
            if verificar_clave(usuario["hash"], clave):
                registrar_evento(nombre, "login", "exitoso")
                return {"usuario": nombre, "rol": usuario["rol"]}

    registrar_evento(nombre, "login", "fallido")
    print("Credenciales incorrectas.")
    return None



def consultar_inventario(sesion):
    if not isinstance(sesion, dict) or not sesion.get("usuario") or sesion.get("rol") not in ("user", "admin"):
        print("Acceso denegado.")
        return False

    productos = cargar_inventario()
    if productos is None:
        return False
    
    for producto in productos:
        print(producto["id"], producto["nombre"], producto["cantidad"])

    return True



def modificar_cantidad(sesion, identificador, entrada):
    if not isinstance(sesion, dict) or not sesion.get("usuario") or sesion.get("rol") != "admin":
        usuario = sesion.get("usuario", "sin_sesion") if isinstance(sesion, dict) else "sin_sesion"
        registrar_evento(
            usuario, "modificar", "rechazado",
            producto=identificador,
            motivo="Permisos insuficientes"
        )
        print("Usted no puede modificar el inventario, se requiere el rol de admin.")
        return False

    try:
        cantidad = int(entrada)
    except (ValueError, TypeError):
        print("Cantidad inválida. Ingrese un número entero.")
        return False

    if cantidad < 0 or cantidad > 1000:
        print("Cantidad inválida. Debe estar entre 0 y 1000.")
        return False

    productos = cargar_inventario()
    if productos is None:
        return False

    for producto in productos:
        if producto["id"] == identificador:
            anterior = producto["cantidad"]
            producto["cantidad"] = cantidad
            guardar_inventario(productos)
            registrar_evento(
                sesion["usuario"], "modificar", "exitoso",
                producto=identificador, anterior=anterior, nueva=cantidad
            )
            print("Cantidad actualizada.")
            return True

    print("Producto no encontrado.")
    return False



def main():
    print("Inventario académico — BASE CON DEBILIDADES")
    print("Estudiante:", input("Escriba su nombre: "))
    sesion = None
    while True:
        if sesion is None:
            nombre = input("Usuario (o salir): ")
            if nombre == "salir":
                break
            sesion = autenticar(nombre, input("Contraseña de prueba: "))
            continue
        print("1. Consultar | 2. Modificar | 3. Cerrar sesión | 0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            consultar_inventario(sesion)
        elif opcion == "2":
            identificador = input("ID del producto: ")
            entrada = input("Nueva cantidad: ")
            modificar_cantidad(sesion, identificador, entrada)
        elif opcion == "3":
            sesion = None
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
