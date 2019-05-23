from requests import put

movie_json = { "title": "the legend of 1900 test",
                "year": 1998,
                "genre": "Drama, Music, Romance",
                "description": "A baby boy, discovered in 1900 on an ocean liner, grows into a musical prodigy, never setting foot on land." 
                }
headers = {"API_KEY": "soyunllave"}
response = put(url="http://127.0.0.1:5000/api/movies/5", json=movie_json, headers=headers)
print(response)