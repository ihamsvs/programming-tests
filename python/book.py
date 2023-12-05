class SQL:
    seq = 0

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")


class Book:
    def __init__(self, sql, title, author):
        # inicializar los atributos
        self.sql = sql
        self.id = None
        self.title = title
        self.author = author

    def save(self):
        try:
            if self.id is None:
                # Validar datos antes de interactuar con la base de datos
                if not self.title or not self.author:
                    raise ValueError(
                        "Título y autor son obligatorios para guardar un libro."
                    )

                self.sql.create(
                    table_name="books", title=self.title, author=self.author
                )
                self.id = self.sql.last_inserted_id()
            else:
                self.sql.update(
                    "books", record_id=self.id, title=self.title, author=self.author
                )
        except Exception as e:
            # Manejar excepciones
            raise Exception(f"Error al guardar el libro: {e}")

    def get(self, book_id):
        try:
            # Verificar la existencia del libro antes de intentar recuperarlo
            book_data = self.sql.retrieve(table_name="books", record_id=book_id)
            if book_data:
                self.id = book_id
                self.title = book_data["title"]
                self.author = book_data["author"]
            else:
                raise ValueError(f"No se encontró un libro con el ID {book_id}")
        except Exception as e:
            raise Exception(f"Error al obtener el libro: {e}")

    def update(self):
        try:
            if self.id is not None:
                # Validar datos antes de interactuar con la base de datos
                if not self.title or not self.author:
                    raise ValueError(
                        "Título y autor son obligatorios para actualizar un libro."
                    )

                self.sql.update(
                    "books", record_id=self.id, title=self.title, author=self.author
                )
            else:
                raise ValueError("El libro no tiene un identificador")
        except Exception as e:
            raise Exception(f"Error al actualizar el libro: {e}")

    def delete(self):
        try:
            if self.id is not None:
                self.sql.delete(table_name="books", record_id=self.id)
            else:
                raise ValueError("El libro no tiene un identificador")
        except Exception as e:
            raise Exception(f"Error al eliminar el libro: {e}")
