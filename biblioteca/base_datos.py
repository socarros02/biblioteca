libros = [
    {"codigo": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "fecha": 1967},
    {"codigo": 2, "titulo": "1984", "autor": "George Orwell", "fecha": 1949},
    {"codigo": 3, "titulo": "El nombre de la rosa", "autor": "Umberto Eco", "fecha": 1980},
    {"codigo": 4, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "fecha": 1605},
    {"codigo": 5, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "fecha": 1953},
    {"codigo": 6, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "fecha": 1981},
    {"codigo": 7, "titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "fecha": 1813},
    {"codigo": 8, "titulo": "El señor de los anillos", "autor": "J. R. R. Tolkien", "fecha": 1954},
    {"codigo": 9, "titulo": "Rayuela", "autor": "Julio Cortázar", "fecha": 1963},
    {"codigo": 10, "titulo": "La metamorfosis", "autor": "Franz Kafka", "fecha": 1915},
    {"codigo": 11, "titulo": "La meta", "autor": "Franz Kafka", "fecha": 1915}
]
l=libros


biblioteca = [
    {"codigo": 1,
     "estanteria" : [
        [0, {"libro": l[0], "ejemplar": 100, "disponible": True}, 0],
        [{"libro": l[1], "ejemplar": 50, "disponible": True}, 0, {"libro": l[2], "ejemplar": 30, "disponible": False}]],
        "filas":2,
        "columnas":3},
    {"codigo": 2,
     "estanteria": [
         [{"libro": l[0], "ejemplar": 100, "disponible": True},0,0],
         [ {"libro": l[1], "ejemplar": 30, "disponible": False},0, {"libro": l[1], "ejemplar": 31, "disponible": True}]],
     "filas": 2,
     "columnas": 3}
]
