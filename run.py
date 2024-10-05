from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        # Probar la conexión
        db.session.execute(text("SELECT 1"))  # Prueba la conexión
        print("Conexión a la base de datos exitosa")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == '__main__':
    app.run(debug=True)