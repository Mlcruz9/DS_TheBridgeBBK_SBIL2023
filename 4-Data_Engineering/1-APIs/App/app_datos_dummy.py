from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros

# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada

# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada utilzando al final del endpoint <string:title>

# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada

# 5.Ruta para añadir un libro mediante un json en la llamada

# 6.Ruta para añadir un libro mediante parámetros

# 7.Ruta para modificar un libro

# 8.Ruta para eliminar un libro

app.run()