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
@app.route('/api/v1/resources/books/count_books', methods=['GET'])
def books_by_author():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = '''SELECT author, COUNT(title)
                        FROM books
                        GROUP BY author
                        ORDER BY COUNT(title)
                        DESC'''
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return result


# 2.Ruta para obtener los libros de un autor como argumento en la llamada
@app.route('/api/v1/resources/books/book_author', methods=['GET'])
def books_by_author_param():
    if 'author' in request.args:
        author =  request.args.get('author')
        if author == '':
            return 'Blank space.'
        
        else:
            author = "%" + author + "%"
            connection = sqlite3.connect('books.db')
            cursor = connection.cursor()
            select_books = '''SELECT author, title
                                FROM books
                                WHERE author LIKE ?'''
            result = cursor.execute(select_books, (author,)).fetchall()
            connection.close()

            if result == []:
                connection.close()
                return 'Author not found.'
            
            else:
                connection.close()
                return result
    
    else:
        return 'You must provide an author param.'
    
# 3.Ruta para obtener los libros filtrados por título, publicación y autor

@app.route('/api/v1/resources/books/filters', methods=['GET'])
# def get_filter_new():
#     connection = sqlite3.connect('books.db')
#     cursor = connection.cursor()

#     # Obtener parámetros de la solicitud o usar valores por defecto
#     title = request.args.get('title', '')
#     author = request.args.get('author', '')
#     published = request.args.get('published', '')

#     # Preparar los parámetros para la consulta
#     params = (f'%{title}%', f'%{author}%', f'%{published}%')

#     # Consulta parametrizada
#     info = """
#     SELECT title, author, published
#     FROM books
#     WHERE
#     title LIKE ?
#     AND author LIKE ?
#     AND published LIKE ?;
#     """
#     result = cursor.execute(info, params).fetchall()  # Ejecutar la consulta
#     connection.close()

#     return result

def libros_filtrados():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    autor = "%" + request.args.get('author', '') + "%"
    titulo = "%" +  request.args.get('title', '') + "%"
    publicacion = "%" + request.args.get('published', '')+ "%"

    conditions = []
    parameters = []

    if autor:
        conditions.append("author LIKE ?")
        parameters.append(autor)
    if titulo:
        conditions.append("title LIKE ?")
        parameters.append(titulo)
    if publicacion:
        conditions.append("published LIKE ?")
        parameters.append(publicacion)

    where_clause = " AND ".join(conditions)
    select_books = f"SELECT title, published, author FROM books WHERE {where_clause}"

    result = cursor.execute(select_books, tuple(parameters)).fetchall()

    connection.close()

    return result
app.run()