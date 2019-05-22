from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/<int:movie_id>")
def movie(movie_id):
    return render_template("movie.html", id=movie_id)

@app.route("/firstweb")
def firstweb():
    return render_template("first-web.html")

    
if __name__ == "__main__":
    app.run(debug=True)