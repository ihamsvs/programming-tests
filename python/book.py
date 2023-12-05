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
    """Aquí implementar la clase"""

    def __init__(self, sql, title, author):
        self.sql = sql
        self.id = None
        self.title = title
        self.author = author

    def save(self):
        if self.id is None:
            self.sql.create(table_name="books", title=self.title, author=self.author)
            self.id = self.sql.last_inserted_id()
        else:
            self.sql.update(
                "books", record_id=self.id, title=self.title, author=self.author
            )

    def get(self, book_id):
        return self.sql.retrieve(table_name="books", record_id=book_id)

    def update(self):
        if self.id is not None:
            self.sql.update(
                "books", record_id=self.id, title=self.title, author=self.author
            )
        else:
            raise Exception("El libro no tiene un identificador")

    def delete(self):
        if self.id is not None:
            self.sql.delete(table_name="books", record_id=self.id)
        else:
            raise Exception("El libro no tiene un identificador")
