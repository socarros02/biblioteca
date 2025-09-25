
INSERT INTO ejemplares (libro_id, disponible) VALUES (1, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (1, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (3, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (3, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (2, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (2, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (4, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (4, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (5, 1);
INSERT INTO ejemplares (libro_id, disponible) VALUES (5, 1);



INSERT INTO autores (name) VALUES ('Gabriel García Márquez');
INSERT INTO autores (name) VALUES ('George Orwell');
INSERT INTO autores (name) VALUES ('Jane Austen');
INSERT INTO autores (name) VALUES ('J. R. R. Tolkien');
INSERT INTO autores (name) VALUES ('Franz Kafka');

-- Libros (2 por autor)
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('Cien años de soledad', 1967, 1);
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('Crónica de una muerte anunciada', 1981, 1);

INSERT INTO libros (titulo, fecha, autor_id) VALUES ('1984', 1949, 2);
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('Rebelión en la granja', 1945, 2);

INSERT INTO libros (titulo, fecha, autor_id) VALUES ('Orgullo y prejuicio', 1813, 3);
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('Emma', 1815, 3);

INSERT INTO libros (titulo, fecha, autor_id) VALUES ('El señor de los anillos', 1954, 4);
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('El hobbit', 1937, 4);

INSERT INTO libros (titulo, fecha, autor_id) VALUES ('La metamorfosis', 1915, 5);
INSERT INTO libros (titulo, fecha, autor_id) VALUES ('El proceso', 1925, 5);

SELECT * FROM autores;
SELECT * FROM libros;
SELECT * FROM ejemplares;