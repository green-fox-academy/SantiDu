from flask import Flask, request, jsonify, make_response
from functools import wraps

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


def post_movie_data(body):
    """
    input: 
    output: none, but write data to database
    """
    pass

 
@app.route("/api/movies")
def api_movies():
    return jsonify(all_movie_data())


@app.route("/api/movies", methods=["POST"])
@require_appkey
def api_movies_post():
    return "Your movie is in the database!"

        

@app.route("/api/movies/<movie_id>", methods=["GET", "PUT", "DELETE"])
def api_movie_id(movie_id):
    if request.method == "GET":
        filename = f"./database/{movie_id}.txt"
        return jsonify(get_movie_data(filename))
    elif request.method == "POST":
        pass



if __name__ == "__main__":
    app.run(debug=True)