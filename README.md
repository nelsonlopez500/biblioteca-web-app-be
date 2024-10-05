
## Proyecto Flask - Configuración e Instalación

Este documento explica los pasos para configurar y levantar el proyecto Flask, incluyendo la instalación de todas las dependencias necesarias y la configuración del entorno virtual.

### Requisitos previos

Es necesario tener instalado Python 3.12.3 (o superior) y `pip` en el sistema. Además, se recomienda contar con `virtualenv` para la gestión de entornos virtuales.

### 1. Configuración del entorno virtual

1. **Instalación de virtualenv (si no está instalado):**
   Para instalar `virtualenv`, se debe ejecutar el siguiente comando en la terminal:
   ```bash
   pip install virtualenv
   ```

2. **Creación del entorno virtual:**
   Una vez instalado `virtualenv`, se crea un entorno virtual en la raíz del proyecto:
   ```bash
   virtualenv -p python3.12.3 venv
   ```

3. **Activación del entorno virtual:**
   - En Windows:
     ```bash
     .env\Scriptsctivate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

Este paso asegura que todas las librerías y dependencias se instalen en un entorno aislado.

### 2. Instalación de dependencias

Con el entorno virtual activo, se procede a instalar las librerías necesarias para el proyecto:

#### a) Instalación de Flask

Flask es el framework web utilizado en este proyecto. Para instalarlo, se debe ejecutar el siguiente comando:
```bash
pip install flask
```

#### b) Instalación de Flask-CORS

Flask-CORS permite gestionar las solicitudes de recursos cruzados (CORS), necesarias cuando el frontend y backend están en dominios diferentes. Para instalarlo:
```bash
pip install flask-cors
```

#### c) Instalación de Flaskr

Flaskr es una extensión para estructurar el proyecto Flask. Para instalarla, se debe ejecutar:
```bash
pip install flaskr
```

#### d) Instalación de SQLObject

SQLObject es la herramienta de mapeo objeto-relacional (ORM) utilizada en el proyecto para gestionar la base de datos. Para instalarla:
```bash
pip install SQLObject
```

#### e) Instalación de python-dotenv

`python-dotenv` permite cargar variables de entorno desde un archivo `.env`, lo que facilita la configuración de credenciales y otros parámetros sensibles. Para instalarla:
```bash
pip install python-dotenv
```

### 3. Conexión a la base de datos

#### Instalación de pymssql

Para establecer la conexión con la base de datos SQL Server en el proyecto Flask, es necesario instalar `pymssql`. Esta librería permite interactuar con bases de datos SQL Server directamente desde Python. Se puede instalar usando el siguiente comando:

```bash
pip install pymssql
```

Una vez instalada, puedes configurar la conexión a tu base de datos en el proyecto, utilizando las variables de entorno cargadas con `python-dotenv`.

### 4. Ejecución del proyecto

Una vez instaladas todas las dependencias, se puede ejecutar el proyecto Flask utilizando el siguiente comando en la terminal:
```bash
flask run
```

Esto iniciará el servidor de desarrollo y la aplicación estará disponible en `http://localhost:5000`.
