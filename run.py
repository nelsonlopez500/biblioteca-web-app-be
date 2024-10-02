from app import create_app, sqlhub

app = create_app()

with app.app_context():
    try:
        # Probar la conexión
        sqlhub.processConnection.query("SELECT 1")  # Prueba la conexión
        print("Conexión a la base de datos exitosa")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == '__main__':
    app.run(debug=True)