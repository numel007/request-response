#app.py
from random import randint
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return "Penguins are cute!"

@app.route('/fav-animal')
def fav_animal():
    return "Cats are obviously the best animal."

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"You are a {adjective} {noun}."

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if (number1.isdigit() == False):
        return f"{number1} is not a digit."
    elif (number2.isdigit() == False):
        return f"{number2} is not a digit."
    elif (number1.isdigit() == True and number2.isdigit() == True):
        num1 = int(number1)
        num2 = int(number2)
        return f"{number1} times {number2} is {num1 * num2}."

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if (n.isdigit() == False):
        return "Invalid input. Please try again by entering a word and a number!"
    elif (n.isdigit() == True):
        number = int(n)
        new_string = ""
        for i in range(number):
            new_string += (word + " ")
        return new_string

@app.route('/reverse/<word>')
def reverse(word):
    reversed_string = ""

    for i in range(len(word), 0, -1):
        reversed_string += word[i-1]
    return reversed_string

@app.route('/strangecaps/<word>')
def strangecaps(word):
    new_string = ""

    for i in range(len(word)):
        if (i%2 == 0):
            new_string += word[i].upper()
        else:
            new_string += word[i].lower()
        i += 1
    return new_string

@app.route('/dicegame')
def dicegame():
    rolled_number = randint(1, 6)

    if (rolled_number == 6):
        return "You rolled a 6. You won!"
    elif (rolled_number != 6):
        return f'You rolled a {rolled_number}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)