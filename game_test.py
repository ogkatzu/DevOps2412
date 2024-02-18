from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


class Game:
    def __init__(self, name):
        self.name = name
        self.difficulty = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def play(self):
        pass


class GuessNumber(Game):
    def __init__(self):
        super().__init__("Guess the Number")

    def play(self):
        target_number = random.randint(1, 100)
        return target_number


class WordGuess(Game):
    def __init__(self):
        super().__init__("Word Guess")

    def play(self):
        words = ['python', 'java', 'ruby', 'javascript', 'swift']
        word = random.choice(words)
        return word


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess-number', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'POST':
        difficulty = int(request.form['difficulty'])
        game = GuessNumber()
        game.set_difficulty(difficulty)
        target_number = game.play()
        return render_template('guess_number.html', target_number=target_number)
    return render_template('guess_number_form.html')
#
#
# @app.route('/word-guess', methods=['GET', 'POST'])
# def word_guess():
#     if request.method == 'POST':
#         difficulty = int(request.form['difficulty'])
#         game = WordGuess()
#         game.set_difficulty(difficulty)
#         word = game.play()
#         return render_template('word_guess.html', word=word)
#     return render_template('word_guess_form.html')


if __name__ == "__main__":
    app.run(debug=True)
