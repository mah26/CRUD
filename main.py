from flask import Flask, jsonify, request
from Models.film import Film

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/film/<int:id>', methods=['GET'])
def get_by_id(id):
  film = Film.get_by_id(id)
  if film:
    return jsonify(film.json()), 200
  else:
    return jsonify({'Message': 'Film not found'}), 404


@app.route('/film/', methods=['GET'])
def get():

  films = Film.get_all()
  response = []

  for film in films:
    response.append(film.json())
  
  return jsonify(response), 200


@app.route('/film/', methods=['POST'])

def create(): #Se crea aut.
  json = request.get_json(force=True)
  if(json['title'] != ''):
    return jsonify({'Message': 'Title is empty'}), 400
    
  film = Film(title=json['title'], category=json['category'], length=json['length'])#pilla los datos de json
  film.create()
  
  return jsonify(film), 201

@app.route('/film/<int:id>', methods = ['PUT'] )

def update(id):
  film = Film.get_by_id(id) #el id que queremos
  json= request.get_json(force = True) #del request
  if film:
    film = Film(title=json['title'], category = json['category'], length=json['length'])
    film.update(id)
    return jsonify(film)
      
  else
      return jsonify('Message':'This id does not exist')


@app.route('/film/<int:id>', methods = ['DEL'] )
def delete(id)
  film = Film.get_by_id(id)
  if film:
    film.delete(id)
  else
    return ('Message':"This id does not exist")

app.run(host='0.0.0.0', port=81)
