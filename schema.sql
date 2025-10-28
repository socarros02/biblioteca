

SELECT * FROM libros;
SELECT * FROM ejemplares;
SELECT * FROM prestamos;
SELECT * FROM estanterias;

CREATE TABLE IF NOT EXISTS libros (
    isbn VARCHAR(13) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    fecha_publicacion INT
    edicion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS estanterias (
    id_estanteria INT PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    capacidad_maxima int NOT NULL
);

CREATE TABLE IF NOT EXISTS ejemplares (
    id_ejemplar INT PRIMARY KEY AUTOINCREMENT,
    id_libro VARCHAR(13),
    disponible BOOLEAN DEFAULT 1,
    id_estanteria INT,
    FOREIGN KEY (id_libro) REFERENCES libros(isbn),
    FOREIGN KEY (id_estanteria) REFERENCES estanterias(id_estanteria)
);

CREATE TABLE IF NOT EXISTS prestamos (
    id_prestamo INT PRIMARY KEY AUTOINCREMENT,
    id_ejemplar INT,
    devolucion BOOLEAN DEFAULT 0,
    nombre VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_ejemplar) REFERENCES ejemplares(id_ejemplar)
);

CREATE TRIGGER trg_prestamo_insert
AFTER INSERT ON prestamos
FOR EACH ROW
BEGIN
    UPDATE ejemplares
    SET disponible = 0, id_estanteria = NULL
    WHERE id_ejemplar = NEW.id_ejemplar;
END;


CREATE TRIGGER trg_prestamo_update
AFTER UPDATE OF devolucion ON prestamos
FOR EACH ROW
WHEN NEW.devolucion = 1
BEGIN
    UPDATE ejemplares
    SET disponible = 1
    WHERE id_ejemplar = NEW.id_ejemplar;
END;


