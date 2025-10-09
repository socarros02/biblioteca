import sqlite3 as sql
import os

from carpeta_libros.libros_nuevo_ejemplar import cantidad_ejemplares

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
    SELECT l.titulo,
           count(e.id_ejemplar) as cantidad
    FROM ejemplares e
    JOIN libros l ON e.id_libro = l.isbn
    where e.id_estanteria = ? and e.disponible = 1
    group by l.titulo;
    """, (codigo_estanteria,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {"titulo": r[0],"cantidad":r[1]}
        for r in rows
    ]

def prestar_libro(ejemplar,nombre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
       insert into prestamos(devolucion,id_ejemplar,nombre)
       values (0,?,?)    
        """, (ejemplar,nombre))
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
        SELECT id_estanteria, COUNT(*)
        FROM ejemplares 
        WHERE id_libro = ? and disponible = 1
        GROUP BY id_estanteria
    """, (isbn,))
    row = cursor.fetchall()
    conn.close()

    return [
        {"estanteria": r[0], "cantidad": r[1]}
        for r in row
    ] if row else None

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

def get_id_ejemplar(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id_ejemplar
    FROM ejemplares
    where id_libro = ? and disponible = 1
    LIMIT 1
        """, (isbn,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None



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

def get_ubicacion_ejemplar(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select id_estanteria
    from ejemplares
    where id_libro = ?
    """, (isbn,))
    estanteria = cursor.fetchone()
    conn.close()
    id_estanteria = estanteria[0] if estanteria else None
    return id_estanteria

def carga_nuevo_ejemplar(id_estanteria,isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    insert into ejemplares
        (id_estanteria,id_libro,disponible)
        values (?,?,1)
        """, (id_estanteria,isbn,))
    conn.commit()
    conn.close()
def nuevo_libro(isbn,titulo,autor,publicaion,edicion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    insert into libros
        (isbn,titulo,autor,fecha_publicacion,edicion)
        values (?,?,?,?,?)
        """, (isbn,titulo,autor,publicaion,edicion,))
    conn.commit()
    conn.close()

def editar_libro(isbn_nuevo,titulo,autor,publicaion,edicion,isbn_viejo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    update libros
    set isbn = ?, titulo = ?, autor = ?, fecha_publicacion = ?,edicion = ?
    where isbn = ?
    """,(isbn_nuevo,titulo,autor,publicaion,edicion,isbn_viejo))
    conn.commit()
    conn.close()

def get_prestamos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select p.id_prestamo, p.id_ejemplar, l.titulo, p.nombre
    from prestamos p
    join ejemplares e on e.id_ejemplar = p.id_ejemplar
    join libros l on l.isbn = e.id_libro
    where devolucion = 0
    """)
    prestamos = cursor.fetchall()
    conn.close()
    return [
        {"prestamo": r[0], "ejemplar": r[1],"titulo": r[2],"persona": r[3]}
        for r in prestamos
    ] if prestamos else None

def devolver_prestamos(prestamos):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    update prestamos
    set devolucion = 1
    where id_prestamo = ?
        """, (prestamos,))
    conn.commit()

def mas_prestados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.titulo, COUNT(p.id_prestamo) AS cantidad_prestamos
        FROM prestamos p
        JOIN ejemplares e ON e.id_ejemplar = p.id_ejemplar
        JOIN libros l ON l.isbn = e.id_libro
        GROUP BY l.isbn, l.titulo
        ORDER BY cantidad_prestamos DESC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados[:5]

def cantidad_ejemplares_por_libro(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT COUNT(*) AS canitdad
    FROM ejemplares
    WHERE id_libro = ?;
        """, (isbn,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0]

def capacidad_maxima(estanteria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select capacidad_maxima
    from estanterias
    where id = ?
        """, (estanteria,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0]


def cambiar_de_estanteria(estanteria,isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    update ejemplares
    set id_estanteria = ?
    where id_libro = ?
    """, (estanteria,isbn))
    conn.commit()
    conn.close()

def eliminar_estanteria(estanteria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    delete from estanterias
    where id = ?
    """, (estanteria,))
    conn.commit()
    conn.close()

def borrar_libro_ejemplares(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    delete from ejemplares
    where id_libro = ?
    """, (isbn,))
    conn.commit()
    conn.close()

def borrar_libro(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    delete from libros
    where isbn = ?
    """, (isbn,))
    conn.commit()
    conn.close()

def borrar_libros_prestamos(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM prestamos
        WHERE id_ejemplar IN (
            SELECT id_ejemplar
            FROM ejemplares
            WHERE id_libro = ?
        )
    """, (isbn,))
    conn.commit()
    conn.close()

def buscar_libro_prestados(isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM prestamos
        JOIN ejemplares e ON e.id_ejemplar = prestamos.id_ejemplar
        WHERE e.id_libro = ?
    """, (isbn,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado if resultado else None
    



