import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import random
import requests
import html

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")
db_quiz = SQL("sqlite:///questions.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    print(generate_password_hash("123"))
    rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    if request.method == "POST":
        if 'take' in request.form:
            return redirect("/take")
        elif 'make' in request.form:
            return redirect("/make")
        elif 'random' in request.form:
            return redirect("/random")
    return render_template("index.html", rows=rows)



@app.route("/take", methods=["GET", "POST"])
@login_required
def take():

    questions = db_quiz.execute("SELECT * FROM questions WHERE user = ?", session["user_id"])

    if request.method == "POST":
        time = request.form.get("time")
        score = 0
        total_q = len(questions)
        c_questions = 0
        u_questions = 0

        for q in questions:
            option = request.form.get(f"{q['no']}_option")
            correct = request.form.get(f"{q['no']}_correct")

            if (option == correct):
                score += 1
                c_questions += 1
            elif (option is None):
                u_questions += 1

        return render_template("score.html", score=score, total_q=total_q, c_questions=c_questions, u_questions=u_questions, time=time)

    return render_template("take.html", questions=questions)


@app.route("/random", methods=["GET", "POST"])
@login_required
def random_quiz():

    response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=medium&type=multiple")
    questions = []

    question_bank = response.json()['results']

    if len(question_bank) != 20:
        return apology("Failed to fetch 20 questions from the API. Please try again later.")

    for i, q_data in enumerate(question_bank):
        answers = [
            html.unescape(q_data['correct_answer']),
            html.unescape(q_data['incorrect_answers'][0]),
            html.unescape(q_data['incorrect_answers'][1]),
            html.unescape(q_data['incorrect_answers'][2])
            ]
        random.shuffle(answers)
        question = {
            'no': i + 1,
            'question': html.unescape(q_data['question']),
            'op1': answers[0],
            'op2': answers[1],
            'op3': answers[2],
            'op4': answers[3],
            'correct': q_data['correct_answer']
        }

        questions.append(question)

    if request.method == "POST":
        time = request.form.get("time")
        score = 0
        total_q = len(questions)
        c_questions = 0
        u_questions = 0

        for q in questions:
            option = request.form.get(f"{q['no']}_option")
            correct = request.form.get(f"{q['no']}_correct")

            if (option == correct):
                score += 1
                c_questions += 1
            elif (option is None):
                u_questions += 1

        return render_template("score.html", score=score, total_q=total_q, c_questions=c_questions, u_questions=u_questions, time=time)

    return render_template("random.html", questions=questions)


@app.route("/make", methods=["GET", "POST"])
@login_required
def make():

    if request.method == "POST":
        if 'done' in request.form:
            return redirect("/")
        elif 'add' in request.form:
            if (not request.form.get("question")) or (not request.form.get("option1")) or (not request.form.get("option2")) or (not request.form.get("option3")) or (not request.form.get("option4") or (not request.form.get("correct"))):
                return "Pls fill out all fields"

            question = request.form.get("question")
            op1 = request.form.get("option1")
            op2 = request.form.get("option2")
            op3 = request.form.get("option3")
            op4 = request.form.get("option4")
            correct = request.form.get("correct")

            if correct not in {op1, op2, op3, op4}:
                return "Pls ensure that an option is same as correct answer"

            db_quiz.execute("INSERT INTO questions (user, question, op1, op2, op3, op4, correct) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            session["user_id"], question, op1, op2, op3, op4, correct)
            return render_template("make.html")
        else:
             return render_template("make.html")


    return render_template("make.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        # check if username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # check if password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Validate username and pass
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        c_password = request.form.get("c_password")

        if not username or not password or not c_password:
            return apology("Please fill out all the required fields!")

        if password != c_password:
            return apology("Passwords do not match!")

        # Check if username already exists
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("The username is already taken!")

        hashed_password = generate_password_hash(password)

        # Insert new user into the database
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, hashed_password)

        # Log in the newly registered user
        new_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = new_user[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")
