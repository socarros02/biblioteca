📚 Biblioteca - Sistema de Gestión

Biblioteca es una aplicación de escritorio desarrollada en Python, pensada para la gestión organizada de libros, autores, géneros y estanterías. Con una interfaz construida sobre CustomTkinter, permite manejar de forma intuitiva tanto la base de datos como la visualización del inventario de la biblioteca.

📜 Índice

🌟 Características Principales

🏗️ Arquitectura del Proyecto

🛠️ Tecnologías Utilizadas

🚀 Instalación y Puesta en Marcha

⚙️ Scripts de Mantenimiento

🌟 Características Principales

La aplicación está diseñada para gestionar tanto los libros como sus ejemplares y ubicaciones.

📚 Gestión de Libros y Autores

Alta, baja y modificación de libros con sus datos principales (ISBN, título, autor, género, año, edición).

Administración de autores y géneros para clasificar mejor el catálogo.

🗄️ Organización de Estanterías

Creación y edición de estanterías.

Visualización de los libros cargados por estantería.

🔍 Búsqueda

Filtros para localizar libros por título, autor o género.

Posibilidad de ver ejemplares asociados a cada libro.

🛠️ Base de Datos Integrada

El sistema trabaja con SQLite, con soporte para claves foráneas y relaciones entre libros, autores y géneros.

🏗️ Arquitectura del Proyecto

El proyecto sigue un estilo MVC (Modelo-Vista-Controlador) para mantener el código ordenado y escalable.

Modelo (Database / Lógica de datos)

Tablas: libros, autores, genero, ejemplares, estanterias.

Acceso a datos encapsulado en base_datos.py.

Vista (Interfaz gráfica)

Construida con CustomTkinter.

Cada ventana/pantalla está modularizada en su propio archivo (ej: mostrar_estanteria.py, mostrar_libro.py).

Controlador (Gestión de la lógica)

Archivos que conectan la base de datos con la GUI.

Ejemplo: mover un libro de una estantería a otra, listar autores o ejemplares.

🛠️ Tecnologías Utilizadas

Lenguaje: Python 3

Base de Datos: SQLite 3

Interfaz Gráfica: CustomTkinter

Dependencias: Pillow (para imágenes en la GUI)

🚀 Instalación y Puesta en Marcha
1. Prerrequisitos

Tener instalado Python 3.8 o superior.

2. Clonar el Repositorio
git clone https://github.com/socarros02/biblioteca.git
cd biblioteca

3. Crear un Entorno Virtual (recomendado)
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

4. Instalar Dependencias
pip install -r requirements.txt

5. Ejecutar la Aplicación
python main.py

⚙️ Scripts de Mantenimiento

init_database.py → Inicializa la base de datos con tablas y datos de prueba.

update_ubicaciones.py → Actualiza y gestiona las ubicaciones de ejemplares.

test_debug.py → Permite probar funciones sin abrir toda la GUI.
