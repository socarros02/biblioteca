


drop table autores;
SELECT * FROM libros;
SELECT * FROM ejemplares;
SELECT * FROM prestamos;
SELECT * FROM estanterias;
DELETE FROM estanterias WHERE id IN (3,4);
DELETE FROM sqlite_sequence WHERE name='estanterias';

CREATE TABLE estanterias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
    );

UPDATE estanterias
SET capacidad_maxima = 10
WHERE id = 1 or id =2

SELECT * FROM estanterias



CREATE TABLE ejemplares (
    id_ejemplar INTEGER PRIMARY KEY AUTOINCREMENT,
    id_libro INTEGER,
    id_estanteria INTEGER NULL,
    disponible BOOLEAN,
    FOREIGN KEY (id_estanteria) REFERENCES estanterias(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);



CREATE TABLE prestamos(
id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT ,
devolucion BOOLEAN,
id_ejemplar INTEGER,
nombre varchar(50),
FOREIGN KEY (id_ejemplar) REFERENCES ejemplares(id_ejemplar)
)


INSERT into prestamos(devolucion,id_ejemplar,nombre)VALUES
(0,4,"Juan"),
(0,7,"Marta"),
(0,12,"Esteban"),
(0,15,"Carlos"),
(0,20,"Martin");

CREATE TABLE libros(
    isbn TEXT PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    fecha_publicacion INTEGER,
    edicion TEXT
);

CREATE TABLE ejemplares (
    id_ejemplar INTEGER PRIMARY KEY AUTOINCREMENT,
    id_libro TEXT,
    id_estanteria INTEGER NULL,
    disponible BOOLEAN,
    FOREIGN KEY (id_estanteria) REFERENCES estanterias(id),
    FOREIGN KEY (id_libro) REFERENCES libros(isbn)
);

CREATE TABLE prestamos(
id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT ,
devolucion BOOLEAN,
id_ejemplar INTEGER,
nombre varchar(50),
FOREIGN KEY (id_ejemplar) REFERENCES ejemplares(id_ejemplar)
)


INSERT INTO libros (isbn, titulo, autor, fecha_publicacion, edicion) VALUES
('978-0001', 'Libro 1', 'Autor A', 2001, '1ra'),
('978-0002', 'Libro 2', 'Autor B', 2002, '2da'),
('978-0003', 'Libro 3', 'Autor C', 2003, '1ra'),
('978-0004', 'Libro 4', 'Autor D', 2004, '3ra'),
('978-0005', 'Libro 5', 'Autor E', 2005, '1ra'),
('978-0006', 'Libro 6', 'Autor F', 2006, '2da'),
('978-0007', 'Libro 7', 'Autor G', 2007, '1ra'),
('978-0008', 'Libro 8', 'Autor H', 2008, '1ra'),
('978-0009', 'Libro 9', 'Autor I', 2009, '2da'),
('978-0010', 'Libro 10', 'Autor J', 2010, '1ra'),
('978-0011', 'Libro 11', 'Autor K', 2011, '1ra'),
('978-0012', 'Libro 12', 'Autor L', 2012, '2da'),
('978-0013', 'Libro 13', 'Autor M', 2013, '1ra'),
('978-0014', 'Libro 14', 'Autor N', 2014, '3ra'),
('978-0015', 'Libro 15', 'Autor O', 2015, '1ra'),
('978-0016', 'Libro 16', 'Autor P', 2016, '2da'),
('978-0017', 'Libro 17', 'Autor Q', 2017, '1ra'),
('978-0018', 'Libro 18', 'Autor R', 2018, '1ra'),
('978-0019', 'Libro 19', 'Autor S', 2019, '2da'),
('978-0020', 'Libro 20', 'Autor T', 2020, '1ra');

INSERT INTO ejemplares (id_libro, id_estanteria, disponible) VALUES
('978-0006', 2, 1)
('978-0001', 1, 1),
('978-0002', 2, 1),
('978-0003', 1, 1),
('978-0004', 2, 1),
('978-0005', 1, 1),
('978-0006', 2, 1),
('978-0007', 1, 1),
('978-0008', 2, 1),
('978-0009', 1, 1),
('978-0010', 2, 1),
('978-0011', 1, 1),
('978-0012', 2, 1),
('978-0013', 1, 1),
('978-0014', 2, 1),
('978-0015', 1, 1),
('978-0016', 2, 1),
('978-0017', 1, 1),
('978-0018', 2, 1),
('978-0019', 1, 1),
('978-0020', 2, 1);


INSERT INTO prestamos (devolucion, id_ejemplar, nombre) VALUES
(0, 1, 'Juan Perez'),
(0, 5, 'Maria Gomez'),
(1, 8, 'Carlos Lopez'),
(0, 12, 'Ana Martinez');

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

UPDATE prestamos
set devolucion = 1
where id_prestamo = 2

INSERT INTO prestamos(devolucion,id_ejemplar,nombre)values
(0, 8, 'Maria Gomez')

