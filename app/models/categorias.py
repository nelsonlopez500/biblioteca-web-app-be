from sqlobject import SQLObject, StringCol, BoolCol, DateTimeCol, IntCol
from datetime import datetime

class Categoria(SQLObject):
    class sqlmeta:
        table = 'categorias'  # Nombre de la tabla en la base de datos
        idName = 'categoria_id'  # Este será el nombre del campo id

    # No necesitas definir categoria_id ya que SQLObject lo manejará automáticamente
    # como un campo autoincremental debido a la definición de la tabla.
    
    nombre_categoria = StringCol(unique=True, length=100)  # Nombre de la categoría
    status = BoolCol(default=True)  # Estado de la categoría
    created_at = DateTimeCol(default=datetime.now)  # Fecha de creación

    def __repr__(self):
        return f'<Categoria {self.nombre_categoria}>'
