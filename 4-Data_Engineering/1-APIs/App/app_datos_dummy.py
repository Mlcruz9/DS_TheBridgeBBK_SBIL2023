from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/all_books/', methods=['GET'])
def get_all_books():
    return books

# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/book_id/', methods=['GET'])
def get_book_by_id():
    
    if 'id' in request.args:
        id = int(request.args.get('id'))
        result = []
        for book in books:
            if book['id'] == id:
                result.append(book)

        return result
    
    else:
        return 'You must provide an id parameter.'

# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada utilzando al final del endpoint <string:title>
@app.route('/book_title/<string:title>', methods=['GET'])
def get_book_by_title(title):
        
    result = []
    for book in books:
        if book['title'] == title:
            result.append(book)

    return result
    
# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada
@app.route('/book_title_param/', methods=['GET'])
def get_book_by_title_param():
    
    if 'title' in request.args:
        title = request.args.get('title')
        title = title.lower()
        result = []
        # result = [book for book in books if title in book['title'].lower()]
        for book in books:
            if title in book['title']:
                result.append(book)

        if result == []:
            return 'Title not found.'

        else:
            return result
        
    else:
        return 'You must provide an title parameter.'
    
# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/add_book/', methods=['POST'])
def add_book():
    
    new_book = request.get_json()
    books.append(new_book)

    return books


# 6.Ruta para añadir un libro mediante parámetros
@app.route('/add_book_param/', methods=['POST'])
def add_book_param():
    
    book = {}
    book['id'] = int(request.args.get('id'))
    book['title'] = request.args.get('title')
    book['published'] = request.args.get('published')
    book['author'] = request.args.get('author')
    book['first_sentence'] = request.args.get('first_sentence')

    books.append(book)

    return books

# 7.Ruta para modificar un libro
@app.route('/modify_book_title/', methods=['PUT'])
def modify_book_title():
    
    id = int(request.args.get('id'))
    title = request.args.get('title')

    for book in books:
        if book['id'] == id:
            book['title'] = title
    
    return books

# 8.Ruta para eliminar un libro
@app.route('/delete_book_id/', methods=['DELETE'])
def delete_book_id():
    
    id = int(request.args.get('id'))
    
    for book in books:
        if book['id'] == id:
            books.remove(book)
    
    return books


app.run()