#app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello World!"

@app.route('/penguins')
def penguins():
    return "Penguins are cute!"

@app.route('/fav-animal')
def fav_animal():
    return "Cats are obviously the best animal."

if __name__ == '__main__':
    app.run(debug=True)