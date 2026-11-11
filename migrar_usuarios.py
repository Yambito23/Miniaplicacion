
import json
from pathlib import Path
from seguridad import crear_hash

USUARIOS = Path(__file__).resolve().parent / "usuarios.json"

usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))

for usuario in usuarios:
    clave = usuario.pop("clave")
    usuario["hash"] = crear_hash(clave)

USUARIOS.write_text(
    json.dumps(usuarios, indent=2),
    encoding="utf-8"
)

print("Contraseñas protegidas correctamente.")
