import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded (it means when we make any change in templates file then it will be auto reloaded in the screen of any person who was using this route at )
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Adding the user's entry into the database
        name = request.form.get("name")
        day = request.form.get("day")
        month = request.form.get("month")

        db.execute("INSERT INTO birthdays (name, day, month) VALUES(?, ?, ?)", name, day, month)
        return redirect("/")

    else:
        # Displaying the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)


