import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = "SELECT * FROM books"
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return result

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente

# 2.Ruta para obtener los libros de un autor como argumento en la llamada
    
# 3.Ruta para obtener los libros filtrados por título, publicación y autor

app.run()