from flask import Blueprint, request, make_response, jsonify

from BLL.movies_bl import MoviesBL
movies_bl = MoviesBL()

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def get_all_movies():
    movies = movies_bl.get_all_movies()
    return jsonify(movies)


@movies.route('/<id>', methods=['GET'])
def get_by_id(id):
    movie = movies_bl.get_by_id(id)
    return jsonify(movie)

@movies.route('/', methods=['POST'])
def create_movie():
    obj = {"name": request.json["name"], "genres": request.json["genres"],
           "image": request.json["image"], "premiered": request.json["premiered"]}
    result = movies_bl.create_movie(obj)
    return make_response({"success": str(result)}, 200)


@movies.route('/<id>', methods=['DELETE'])
def delete_movie(id):
    result = movies_bl.delete_movie(id)
    return result


@movies.route('/<id>', methods=['PUT'])
def update_movie(id):
    obj = {"name": request.json["name"], "genres": request.json["genres"],
           "image": request.json["image"], "premiered": request.json["premiered"]}
    result = movies_bl.update_movie(id, obj)
    return result
