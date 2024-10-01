from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Crear una base declarativa
Base = declarative_base()

# Definir la clase Categoria
class Categoria(Base):
    __tablename__ = 'categorias'
    
    categoria_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_categoria = Column(String(100), unique=True, nullable=False)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime)