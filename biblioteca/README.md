# 📚 Biblioteca - Sistema de Gestión

![Biblioteca](assets/biblioteca.png)

**Biblioteca** es una aplicación de escritorio desarrollada en **Python**, pensada para la gestión organizada de libros, autores, géneros y estanterías. Con una interfaz construida sobre **CustomTkinter**, permite manejar de forma intuitiva tanto la base de datos como la visualización del inventario de la biblioteca.

---

## 📜 Índice

* [🌟 Características Principales](#-características-principales)  
* [🏗️ Arquitectura del Proyecto](#️-arquitectura-del-proyecto)  
* [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)  
* [🚀 Instalación y Puesta en Marcha](#-instalación-y-puesta-en-marcha)  
* [⚙️ Scripts de Mantenimiento](#️-scripts-de-mantenimiento)  

---

## 🌟 Características Principales

La aplicación está diseñada para gestionar tanto los libros como sus ejemplares y ubicaciones.

#### 📚 **Gestión de Libros y Autores**
- Alta, baja y modificación de libros con sus datos principales (ISBN, título, autor, género, año, edición).  
- Administración de autores y géneros para clasificar mejor el catálogo.  

#### 🗄️ **Organización de Estanterías**
- Creación y edición de estanterías.  
- Visualización de los libros cargados por estantería.  

#### 🔍 **Búsqueda**
- Filtros para localizar libros por título, autor o género.  
- Posibilidad de ver ejemplares asociados a cada libro.  

#### 🛠️ **Base de Datos Integrada**
- El sistema trabaja con **SQLite**, con soporte para claves foráneas y relaciones entre libros, autores y géneros.  

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue un estilo **MVC (Modelo-Vista-Controlador)** para mantener el código ordenado y escalable.

1. **Modelo (Database / Lógica de datos)**  
   - Tablas: `libros`, `autores`, `genero`, `ejemplares`, `estanterias`.  
   - Acceso a datos encapsulado en `base_datos.py`.  

2. **Vista (Interfaz gráfica)**  
   - Construida con **CustomTkinter**.  
   - Cada ventana/pantalla está modularizada en su propio archivo (ej: `mostrar_estanteria.py`, `mostrar_libro.py`).  

3. **Controlador (Gestión de la lógica)**  
   - Archivos que conectan la base de datos con la GUI.  
   - Ejemplo: mover un libro de una estantería a otra, listar autores o ejemplares.  

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3  
- **Base de Datos**: SQLite 3  
- **Interfaz Gráfica**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- **Dependencias**: Pillow (para imágenes en la GUI)  

---

## 🚀 Instalación y Puesta en Marcha

#### 1. Prerrequisitos
- Tener instalado **Python 3.8** o superior.  

#### 2. Clonar el Repositorio
```bash
git clone https://github.com/socarros02/biblioteca.git
cd biblioteca
```
#### 3. Crear un entorno virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
#### 4. Instalar Dependencias
```bash
-pip install -r requirements.txt
```
#### 5.Ejecutar Python
```bash
- python main.py
```
a