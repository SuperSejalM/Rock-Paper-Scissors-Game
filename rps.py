from flask import Flask, render_template, request
import random

app = Flask(__name__)

def cpu_choice():
    r = random.randrange(1, 4)
    if r == 1:
        return "Scissors"
    elif r == 2:
        return "Rock"
    elif r == 3:
        return "Paper"
    else:
        return None

def rock_paper_scissors(q,cpu,):

    if q == cpu:
        return "You Tied Try again!"
    elif (q == "Scissors") and (cpu == "Rock"):
        return "The computer wins!"
    elif ((q == "Rock") and (cpu == "Paper")):
        return "The computer wins!"
    elif ((q == "Paper") and (cpu == "Scissors")):
        return "The computer wins!"
    elif ((q == "Scissors") and (cpu == "Paper")):
        return "You win!"
    elif ((q == "Rock") and (cpu == "Scissors")):
        return "You win!"
    elif ((q == "Paper") and (cpu == "Rock")):
        return "You win!"
    else:
        return "Invalid input, please try again."
  
@app.route("/rockps", methods=["GET", "POST"])
def index():
    result = None
    cpumove = None
    if request.method == "POST":
        yourMove = request.form["move"]
        cpumove = cpu_choice()  # Only call once
        result = rock_paper_scissors(yourMove, cpumove)
        result += f" The computer chose {cpumove}."
    return render_template("rockps.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)