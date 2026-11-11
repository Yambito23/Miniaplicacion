# Base educativa — COMP 2700

Nombre: Jose Mujica Melendez
Numero de estudiante: Y00665906

Este proyecto consiste en una aplicación educativa de inventario desarrollada en Python. Su propósito es practicar conceptos de programación y seguridad, incluyendo autenticación, autorización por roles, validación de entradas, almacenamiento de información y registro de auditoría. La aplicación utiliza datos ficticios y está diseñada exclusivamente para usos académicos.

Requiere Python 3.10 o posterior. Desde esta carpeta:

    python -m venv .venv

Windows CMD:

    .venv\Scripts\activate.bat

macOS/Linux:

    source .venv/bin/activate

Luego:

    python -m pip install -r requirements.txt
    python app.py

En algunos sistemas debe utilizar python3 en lugar de python.

Cuentas públicas y exclusivamente ficticias:
- admin / AdminDemo2700!
- user / UserDemo2700!

## Archivos del proyecto: 

    app.py: contiene las funciones principales del inventario, autenticación, autorización, validación y auditoría.

    seguridad.py: contiene las funciones para generar y verificar hashes de contraseñas.

    inventario.json: almacena los productos y sus cantidades.

    usuarios.json: almacena las cuentas de prueba y sus hashes.

    auditoria.jsonl: almacena los eventos de autenticación y modificación.

    README.md: contiene las instrucciones y documentación del proyecto.

## Pruebas hechas:

    Se realizaron pruebas para verificar el funcionamiento de los controles implementados:

    Autenticación: se probaron credenciales correctas, contraseñas incorrectas y usuarios inexistentes.

    Autorización: se comprobó que los usuarios con rol user y las sesiones ausentes no pueden modificar el inventario.

    Validación: se probaron cantidades negativas, valores superiores al límite, texto, decimales y entradas vacías. También se verificaron los límites válidos de 0 y 1000.

    Consulta y modificación: se comprobó que ambos roles pueden consultar, que admin puede modificar cantidades y que un producto inexistente no se crea.

    Persistencia: se verificó que los cambios permanecen después de cerrar y ejecutar nuevamente el programa.

    Auditoría: se verificó el registro de inicios de sesión exitosos y fallidos, modificaciones autorizadas e intentos rechazados.

    Manejo de errores: se probaron archivos ausentes y contenido JSON inválido. Posteriormente se restauró el inventario original y se verificó su funcionamiento.

## Uso de AI:

    Se utilizó ChatGPT como herramienta de apoyo durante el desarrollo del proyecto. Su uso principal fue ayuda con la generación de fragmentos de código, la revisión de posibles errores y la explicación de conceptos o instrucciones que no comprendía completamente en el momento, aunque fueron pocos.

    Aunque se solicitaron sugerencias para implementar diferentes partes del programa, las decisiones finales sobre qué diseño y solución utilizar fueron tomadas por mí. Antes de hacer los cambios, me aseguré comprender el funcionamiento del código y la razón detrás de cada implementación. 

    La IA también se utilizó para aclarar conceptos relacionados con la autenticación, autorización, validación de entradas, auditoría y manejo de excepciones. Finalmente, las implementaciones fueron revisadas y comprobadas mediante pruebas prácticas para verificar que cumplieran con los requisitos del proyecto.

    El IA me ayudo en organizar la estructura del readme.

## Solicitud de mejora

    Una mejora futura sería que, cuando un usuario con rol `user` seleccione la opción de modificar el inventario, el programa lo detenga inmediatamente y muestre un mensaje indicando que no tiene permisos, sin solicitar más información. Esto mejoraría la seguridad ya que no haría que el usario piense que puede llegar hasta el menu de modificar, viendo que esta siendo denegado desde el primer intento.