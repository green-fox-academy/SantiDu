from flask import Flask, request, jsonify, make_response
from functools import wraps
from os import listdir, remove
from re import match
import fileinput

app = Flask(__name__)
API_KEY = "soyunllave"


def get_movie_data(filename):
    """
    input: a txt file from movie database
    output: a dictionary with info of the movie
    """
    with open(filename) as f:
        lines = f.readlines()
        return {"id": lines[0].rstrip(),
                "title": lines[1].rstrip(),
                "year": lines[2].rstrip(),
                "genre": lines[3].rstrip(),
                "description": lines[4]}


def all_movie_data():
    """
    input: None
    output: a set of dictionary containing informations from all movies in the database
    """
    allmovies = []
    for i in range(1,5):
        filename = f"./database/{i}.txt"
        allmovies.append(get_movie_data(filename))
    return allmovies


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('API_KEY') == API_KEY:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify({"error": "Invalid API_KEY"}), 403)    
    return decorated_function


def data_into_database(movie_json, fpath, id, method="POST"):
    """
    input: json data in the request
    output: none, but write data to database
    """
    try:
        if method == "PUT":
            with open(fpath) as f:
                content = f.read()
        with open(fpath, "w+") as f:    
            f.write(str(id) + "\n")
            f.write(str(movie_json["title"]) + "\n")
            f.write(str(movie_json["year"]) + "\n")
            f.write(str(movie_json["genre"]) + "\n")
            f.write(str(movie_json["description"]) + "\n")
    except KeyError:
        if method == "POST":
            remove(fpath)
        elif method == "PUT":
            with open(fpath, "w") as f:
                f.write(content)
        return "Mal-formatted json"


@app.route("/api/movies")
def api_movies():
    return jsonify(all_movie_data())


@app.route("/api/movies", methods=["POST"])
@require_appkey
def api_movies_post():
    files = listdir("database")
    id = int(match(r"\d+", files[-1]).group()) + 1
    fpath = f"./database/{id}.txt"
    malJsonMessage = data_into_database(request.get_json(), fpath, id=id)
    if malJsonMessage == "Mal-formatted json":
        return "You should have title, year, genre and description as fields in json."
    return jsonify(request.get_json())

        
@app.route("/api/movies/<movie_id>")
def api_movie_id(movie_id):
    filename = f"./database/{movie_id}.txt"
    return jsonify(get_movie_data(filename))
    

@app.route("/api/movies/<movie_id>", methods=["PUT"])
@require_appkey
def api_movie_id_put(movie_id):
    flist = listdir("database")
    fname = f"{movie_id}.txt"
    if fname in flist:
        fname = f"./database/{movie_id}.txt"
        malJsonMessage = data_into_database(request.get_json(), fname, id=movie_id, method="PUT")
        if malJsonMessage == "Mal-formatted json":
            return "You should have title, year, genre and description as fields in json."
        return jsonify(request.get_json())
    return make_response(jsonify({"error": f"No movie found with {movie_id} ID"}), 404)        


@app.route("/api/movies/<movie_id>", methods=["DELETE"])
@require_appkey
def api_movie_id_delete(movie_id):
    try:
        remove(f"./database/{movie_id}.txt")
    except FileNotFoundError:
        return make_response(jsonify({"error": f"No movie found with {movie_id} ID"}), 404)
    



if __name__ == "__main__":
    app.run(debug=True)