from flask import Flask, render_template

app = Flask(__name__)

### HTML Workshop
@app.route("/firstweb")
def firstweb():
    return render_template("first-web.html")

### Movies
movies = {
    1: "The Silence of the Lambs",
    2: "Whiplash",
    3: "Good Will Hunting",
    4: "El secreto de sus ojos"
    }

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/<int:movie_id>")
def movie(movie_id):
    with open(f"./movie_database/{movie_id}.txt", "r") as f:
        year = f.readline()
        director = f.readline()
        stars = f.readline()
    return render_template("movie.html", title=movies[movie_id], 
                            year=year, director=director, stars=stars)




if __name__ == "__main__":
    app.run(debug=True)