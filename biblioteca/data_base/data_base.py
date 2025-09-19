import sqlite3 as sql
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "database.db")


import sqlite3 as sql
import os


DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def get_connection():
    return sql.connect(DB_PATH)


def get_libros():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT libros.id, libros.titulo, libros.fecha, autores.name
                   FROM libros
                            JOIN autores ON libros.autor_id = autores.id
                   """)
    rows = cursor.fetchall()
    conn.close()

    return [
        {"codigo": row[0], "titulo": row[1], "fecha": row[2], "autor": row[3]}
        for row in rows
    ]
def get_libro_por_titulo(titulo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT libros.id, libros.titulo, libros.fecha, autores.name
                   FROM libros
                            JOIN autores ON libros.autor_id = autores.id
                   WHERE libros.titulo = ?
                   """, (titulo,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"codigo": row[0], "titulo": row[1], "fecha": row[2], "autor": row[3]}
    return None

def get_libro_por_codigo(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT libros.id, libros.titulo, libros.fecha, autores.name
                   FROM libros
                            JOIN autores ON libros.autor_id = autores.id
                   WHERE libros.id = ?
                   """, (codigo,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"codigo": row[0], "titulo": row[1], "fecha": row[2], "autor": row[3]}
    return None


def get_libros_por_autor(nombre_autor):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name
        FROM autores
        WHERE name = ?
    """, (nombre_autor,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_estanterias():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM estanterias")
    rows = cursor.fetchall()
    conn.close()
    # devolver como lista de diccionarios, igual que antes
    return [{"codigo": r[0], "nombre": r[1]} for r in rows]

def get_estanteria_seleccionada(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT estanterias.id
                   FROM estanterias
                   WHERE estanterias.id = ?
                   """, (codigo,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_estanteria_completa(codigo_estanteria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT e.id_ejemplar,l.titulo
    FROM ejemplares e
    JOIN libros l ON e.id_libro = l.id
    where e.id_estanteria = ?;
    """, (codigo_estanteria,))
    rows = cursor.fetchall()
    conn.close()


    return [
        {
            "ejemplar": r[0],
            "titulo": r[1]
        }
        for r in rows
    ]

def prestar_libro(ejemplar):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ejemplares
        SET disponible = 0,id_estanteria = null
        WHERE id_ejemplar = ?
    """, (ejemplar,))
    conn.commit()
    conn.close()
##create_db()
##create_table()
##create_table_libro()
##create_table_ejemplar()






