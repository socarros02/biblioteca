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
                   SELECT isbn,titulo,fecha_publicacion,autor
                   FROM libros
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
                   SELECT isbn,titulo,fecha_publicacion,autor
                   FROM libros
                   WHERE titulo = ?
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
                   SELECT isbn,titulo,fecha_publicacion,autor
                   FROM libros
                   WHERE isbn = ?
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
        SELECT autor
        FROM libros
        WHERE autor like ?
    """, (f"{nombre_autor}%",))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_estanterias():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre,capacidad_maxima FROM estanterias")
    rows = cursor.fetchall()
    conn.close()
    # devolver como lista de diccionarios, igual que antes
    return [{"codigo": r[0], "nombre": r[1], "capacidad":r[2]} for r in rows]

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
    JOIN libros l ON e.id_libro = l.isbn
    where e.id_estanteria = ?;
    """, (codigo_estanteria,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {"ejemplar": r[0],"titulo": r[1]}
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

def nueva_estanteria(nombre,capacidad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    INSERT INTO estanterias(nombre,capacidad_maxima)values 
                    (?,?)
                   
                   """, (nombre, capacidad,))
    conn.commit()
    conn.close()



def get_ejemplares_especificos(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT ej.id_ejemplar,es.nombre,ej.disponible
    from ejemplares ej
    join estanterias es on es.id = ej.id_estanteria
    where id_libro = ?
        """, (isbn,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {"ejemplar": r[0], "estanteria": r[1],"disponible":r[2]}
        for r in rows
    ]

def get_ejemplar_por_estanteria(estanteria,isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select count(*)
    from ejemplares
    where id_estanteria = ? and id_libro = ?
    """, (estanteria,isbn,))
    cantidad = cursor.fetchall()[0]
    conn.close()
    return [cantidad]


def contar_ejemplares_por_estanteria(id_estanteria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM ejemplares
        WHERE id_estanteria = ?
    """, (id_estanteria,))
    cantidad = cursor.fetchone()
    conn.close()
    return cantidad[0] if cantidad else 0
def editar_estaneria(id_estanteria,nombre,capacidad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        update estanterias
        set nombre = ?,capacidad_maxima = ?
        where id = ?
    """, (nombre,capacidad,id_estanteria,))
    conn.commit()
    conn.close()

