# 📚 Biblioteca – Sistema de Gestión de Libros

![Biblioteca](assets/biblioteca.png)  
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)  
![SQLite](https://img.shields.io/badge/SQLite-Database-green?logo=sqlite)  
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-orange)

**Biblioteca** es una aplicación de escritorio desarrollada en **Python** con **CustomTkinter** y **SQLite**, diseñada para la gestión completa de libros, ejemplares, estanterías y préstamos. Ofrece una interfaz moderna, intuitiva y adaptable, con soporte para modo claro/oscuro y temas personalizados.

---

## 📜 Índice

* [🌟 Funcionalidades Principales](#-funcionalidades-principales)  
* [🧠 Arquitectura del Proyecto](#-arquitectura-del-proyecto)  
* [🗃️ Base de Datos](#-base-de-datos)  
* [🧩 Ventanas Principales](#-ventanas-principales)  
* [💻 Tecnologías Utilizadas](#-tecnologías-utilizadas)  
* [🔐 Lógica de Funcionamiento Destacada](#-lógica-de-funcionamiento-destacada)  
* [⚙️ Instalación y Ejecución](#-instalación-y-ejecución)  


---

## 🌟 Funcionalidades Principales

- **🧩 Gestión completa de libros y ejemplares**  
  Todos los ejemplares de un libro se almacenan juntos en la misma estantería, manteniendo un orden lógico y físico. Permite agregar nuevos ejemplares, editar información o listar por autor.

- **🔄 Movimientos de estanterías**  
  Los movimientos entre estanterías se realizan con la cantidad completa de ejemplares del libro para conservar la organización del sistema.

- **🧹 Borrado seguro**  
  Un libro solo puede eliminarse si todos sus ejemplares están devueltos. Esto evita la eliminación de registros con préstamos activos.

- **📦 Gestión de préstamos**  
  Préstamo y devolución de ejemplares individuales. Registro de libros más prestados y visualización por estantería.

- **🎨 Interfaz moderna**  
  Basada en **CustomTkinter**, con soporte para modo claro/oscuro y temas personalizados (ej. `coffee.json`). Diseño adaptable y simple para mejorar la experiencia del usuario.


---
## 🧠 Arquitectura del Proyecto

```plaintext
biblioteca/
│
├── main.py
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_base.py             # Conexión SQLite + CRUD completo
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── win_main.py              # Ventana principal
│   │   │
│   │   └── windows/
│   │       ├── libros/              # Gestión de libros y ejemplares
│   │       ├── estanterias/         # CRUD y movimientos
│   │       ├── prestamos/           # Préstamo y devolución
│   │       └── organizador/         # Reportes y organización
│   │
│   └── themes/
│       ├── coffee.json
│       └── biblioteca.jpg
│
└── assets/
    └── biblioteca.png
```
---

## 🗃️ Base de Datos

El sistema utiliza **SQLite** como base de datos local, gestionada mediante funciones en `data_base.py`.

### Relaciones principales:
- **Libro → Ejemplares** (uno a muchos)  
- **Ejemplar → Préstamos** (uno a muchos)  
- **Estantería → Libros** (uno a muchos)  

Cada acción (préstamo, movimiento, eliminación) se registra para garantizar **integridad y trazabilidad** de los datos.

---

## 🧩 Ventanas Principales

| Ventana | Descripción |
|--------|-------------|
| `VentanaPrincipal` | Menú inicial con acceso a todas las funcionalidades. |
| `VentanaEstanterias` | Creación, edición y visualización de estanterías. |
| `VentanaLibros` | Registro, edición y organización de libros y ejemplares. |
| `VentanaPrestarLibro` | Gestión de préstamos de ejemplares individuales. |
| `VentanaDevolverLibro` | Registro de devoluciones con validación automática. |
| `VentanaOrganizar` | Reportes, ordenamiento y estadísticas del sistema. |
| `VentanaBorrarLibro` / `VentanaBorrarEstanteria` | Eliminación segura con validaciones previas. |

---

## 💻 Tecnologías Utilizadas

| Tecnología       | Uso |
|------------------|-----|
| **Python 3.11+** | Lenguaje principal de desarrollo |
| **CustomTkinter** | Interfaz gráfica moderna y personalizable |
| **SQLite3** | Base de datos local ligera y embebida |
| **Pillow (PIL)** | Manejo de imágenes en la interfaz |
| **CTkMessageBox** | Cuadros de diálogo personalizados |

---

## 🔐 Lógica de Funcionamiento Destacada

- **Integridad referencial**: No se permite eliminar libros con ejemplares prestados.  
- **Ubicación unificada**: Todos los ejemplares de un libro permanecen en la misma estantería.  
- **Reportes en tiempo real**: Libros más prestados, préstamos activos y disponibilidad por estantería.  
- **Validaciones automáticas**: Evitan errores humanos y garantizan consistencia de datos.

---

## ⚙️ Instalación y Ejecución

### 1. Prerrequisitos
- **Python 3.11 o superior**

### 2. Clonar el repositorio
```bash
git clone https://github.com/socarros02/biblioteca.git
cd biblioteca
```
### 3. Crear entorno virtual
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 5. Ejecutar aplicacion
```bash
python main.py
```

