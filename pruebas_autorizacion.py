from app import (
    autenticar,
    modificar_cantidad,
    consultar_inventario,
    cargar_inventario
)

# Guardar la cantidad original de P001
productos = cargar_inventario()

for producto in productos:
    if producto["id"] == "P001":
        original = producto["cantidad"]

# Obtener una sesión real mediante autenticación
sesion = autenticar(input("Usuario: "), input("Contraseña: "))

# Prueba 1: usuario intenta modificar
print("\nPRUEBA 1: Usuario intenta modificar P001 a 99")
if sesion is not None and sesion["rol"] == "user":
    modificar_cantidad(sesion, "P001", "99")
else:
    print("La cuenta utilizada no tiene el rol user.")

# Prueba 2: modificar con sesión None
print("\nPRUEBA 2: Modificar con sesión None")
modificar_cantidad(None, "P001", "99")

# Prueba 3: consultar con sesión None
print("\nPRUEBA 3: Consultar con sesión None")
consultar_inventario(None)

# Verificar que la cantidad final nunca cambio
productos = cargar_inventario()

for producto in productos:
    if producto["id"] == "P001":
        final = producto["cantidad"]

print("\nCantidad original:", original)
print("Cantidad final:", final)