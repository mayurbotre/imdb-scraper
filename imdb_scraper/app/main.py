from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_movies():
    with open('movies.json', 'r') as file:
        movies = json.load(file)
    return jsonify(movies)

@app.route('/hello', methods=['GET'])
def get_liveness():
    return jsonify("Hello World!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)