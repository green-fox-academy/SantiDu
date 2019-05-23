from flask import Flask, request, jsonify, make_response
from functools import wraps
from os import listdir, remove
from re import match

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
            return make_response("Unauthorized", 401)    
    return decorated_function


def postdata_into_database(movie_json):
    """
    input: json data in the request
    output: none, but write data to database
    """
    files = listdir("database")
    id = int(match(r"\d+", files[-1]).group()) + 1
    newfpath = f"./database/{id}.txt"
    try:    
        with open(newfpath, "w") as f:
            f.write(str(id) + "\n")
            f.write(str(movie_json["title"]) + "\n")
            f.write(str(movie_json["year"]) + "\n")
            f.write(str(movie_json["genre"]) + "\n")
            f.write(str(movie_json["description"]) + "\n")
    except KeyError:
        remove(newfpath)
        return "Mal-formatted json"
    

@app.route("/api/movies")
def api_movies():
    return jsonify(all_movie_data())


@app.route("/api/movies", methods=["POST"])
@require_appkey
def api_movies_post():
    malJsonMessage = postdata_into_database(request.get_json())
    if malJsonMessage == "Mal-formatted json":
        return "You should have title, year, genre and description as fields in json."
    return "Your movie has been added to the database successfully."

        

@app.route("/api/movies/<movie_id>", methods=["GET", "PUT", "DELETE"])
def api_movie_id(movie_id):
    if request.method == "GET":
        filename = f"./database/{movie_id}.txt"
        return jsonify(get_movie_data(filename))
    elif request.method == "POST":
        pass



if __name__ == "__main__":
    app.run(debug=True)