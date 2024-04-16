from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:user_number>")
def guess_number(user_number):
    if random_number > user_number:
        return "<b><h1 style='color: red'>Too low!</h1><br></b>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_number < user_number:
        return "<b><h1 style='color: blue'>Too high!</h1><br></b>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<b><h1 style='color: green'>Correct you won!</b></h1><br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
