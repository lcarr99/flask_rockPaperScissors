from flask import Flask, render_template, request, redirect, url_for
import random
from player import player

app = Flask(__name__)
computer = player()
player = player()
playerAnswers = []
computerAnswers = []
answerNames = {1: "Rock", 2: "Paper", 3: "Scissors"}

@app.route('/')
def index():
    return render_template('index.html', computerScore=computer.score, playerScore=player.score, answerNames=answerNames, playerAnswers=playerAnswers, computerAnswers=computerAnswers)


@app.route('/score', methods=["post"])
def score():
    if request.form.get('answer') != "":
        playerAnswer = int(request.form.get('answer'))
        computerAnswer = random.randint(1, 3)
        if playerAnswer == 1 and computerAnswer == 2:
            computer.increaseScore()
        elif playerAnswer == 2 and computerAnswer == 1:
            player.increaseScore()
        elif playerAnswer == 2 and computerAnswer == 3:
            computer.increaseScore()
        elif playerAnswer == 3 and computerAnswer == 2:
            player.increaseScore()
        elif playerAnswer == 1 and computerAnswer == 3:
            player.increaseScore()
        elif playerAnswer == 3 and computerAnswer == 1:
            computer.increaseScore()
        playerAnswers.append(playerAnswer)
        computerAnswers.append(computerAnswer)
    return redirect(url_for('index'))
