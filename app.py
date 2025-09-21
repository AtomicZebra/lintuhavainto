import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import db
import config
import sightings

app = Flask(__name__)
app.secret_key = config.secret_key


@app.route("/")
def index():
    all_sightings = sightings.get_sighting()
    return render_template("index.html", sighting=all_sightings)

@app.route("/sight/<int:sight_id>")
def show_sight(sight_id):
    sight = sightings.get_sight(sight_id)
    return render_template("show_sighting.html", sight=sight)

@app.route("/find_sighting")
def find_sighting():
    query = request.args.get("query")
    if query:
        results = sightings.find_sightings(query)
    else:
        query = ""
        results = []
    return render_template("find_sighting.html", query=query, results=results)

@app.route("/new_sighting")
def new_sighting():
    return render_template("add_sighting.html")

@app.route("/create_sighting", methods=["POST"])
def create_sighting():
    bird_species = request.form["bird_species"]
    kunta = request.form["kunta"]
    location = request.form["location"]
    additional_info = request.form["additional_info"]
    user_id = session["user_id"]
    sightings.add_sighting(bird_species, kunta, location, additional_info, user_id)

    return redirect("/")

@app.route("/edit_sighting/<int:sight_id>")
def edit_sighting(sight_id):
    sight = sightings.get_sight(sight_id)
    if sight["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_sighting.html", sight=sight)

@app.route("/update_sighting", methods=["POST"])
def update_sighting():
    sight_id = request.form["sight_id"]
    bird_species = request.form["bird_species"]
    kunta = request.form["kunta"]
    location = request.form["location"]
    additional_info = request.form["additional_info"]
    sightings.update_sighting(sight_id, bird_species, kunta, location, additional_info)

    return redirect("/sight/" + str(sight_id))

@app.route("/remove_sighting/<int:sight_id>", methods=["GET", "POST"])
def remove_sighting(sight_id):
    sight = sightings.get_sight(sight_id)
    if sight["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_sighting.html", sight=sight)
    
    if request.method == "POST":
        if "remove" in request.form:
            sightings.remove_sighting(sight_id)
            return redirect("/")
        else:
            return redirect("/sight/" + str(sight_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/") 