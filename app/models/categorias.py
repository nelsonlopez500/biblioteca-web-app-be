from sqlobject import SQLObject, StringCol, BoolCol, DateTimeCol, IntCol

class Categoria(SQLObject):
    # Define la tabla correspondiente
    class sqlmeta:
        table = 'categorias'

    # Define los campos del modelo
    categoria_id = IntCol(alternateID=True)  # `alternateID=True` para establecer como clave primaria
    nombre_categoria = StringCol(unique=True, length=100)  # Campo de nombre, único
    status = BoolCol(default=True)  # Campo de estado
    created_at = DateTimeCol()  # Campo de fecha y hora de creación

    def __repr__(self):
        return f'<Categoria {self.nombre_categoria}>'