from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/api/movies", methods=["GET", "POST"])
def api_movies():
    if request.method == "GET":
        return jsonify(all_movie_data())
    elif request.method == "POST":
        pass


def all_movie_data():
    """
    input: None
    output: a set of dictionary containing informations from all movies in the database
    """
    allmovies = []
    for i in range(1,5):
        filename = f"./database/{i}.txt"
        allmovies.append(movie_data(filename))
    return allmovies


def movie_data(filename):
    """
    input: a txt file from movie database
    output: a dictionary with info of the movie
    """
    with open(filename) as f:
        lines = f.readlines()
        return {"id": lines[0].rstrip(),
                "title": lines[1].rstrip(),
                "year": lines[2].rstrip(),
                "genre": lines[5].rstrip(),
                "description": lines[6]}


@app.route("/api/movies/<movie_id>", methods=["GET", "PUT", "DELETE"])
def api_movie_id(movie_id):
    if request.method == "GET":
        filename = f"./database/{movie_id}.txt"
        return jsonify(movie_data(filename))
    elif request.method == "POST":
        pass



if __name__ == "__main__":
    app.run(debug=True)