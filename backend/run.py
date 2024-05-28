from LanavihCV.backend.app import create_app

# Crea una instancia de la aplicación
app = create_app()
    # Ejecuta la aplicación en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)