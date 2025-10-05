import sqlite3, secrets
from flask import Flask
from flask import abort, redirect, render_template, request, session
import config, sightings, users, threads

app = Flask(__name__)
app.secret_key = config.secret_key

#General lengths for data
small_data_length = 50
big_data_length = 1000

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

#Check whether data is within the required limits
def check_requirements(data, length: int, required: bool):
    if required:
        if len(data) > length or not data:
            abort(403)
    else:
        if len(data) > length:
            abort(403)

@app.route("/")
def index():
    all_sightings = sightings.get_sighting()
    return render_template("index.html", sighting=all_sightings)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    sighting = users.get_sighting(user_id)
    return render_template("show_user.html", user=user, sighting = sighting)

@app.route("/sight/<int:sight_id>")
def show_sight(sight_id):
    sight = sightings.get_sight(sight_id)
    if not sight:
        abort(404)
    classes = sightings.get_classes(sight_id)
    messages = threads.get_message(sight_id)
    return render_template("show_sighting.html", sight=sight, classes=classes, messages=messages)

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
    require_login()
    classes = sightings.get_all_classes()
    return render_template("add_sighting.html", classes = classes)

@app.route("/create_sighting", methods=["POST"])
def create_sighting():
    check_csrf()
    bird_species = request.form["bird_species"]
    check_requirements(bird_species, small_data_length, True)

    municipality = request.form["municipality"]
    check_requirements(municipality, small_data_length, True)
    
    location = request.form["location"]
    check_requirements(location, small_data_length, True)
    
    additional_info = request.form["additional_info"]
    check_requirements(additional_info, big_data_length, False)

    user_id = session["user_id"]

    all_classes = sightings.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    sightings.add_sighting(bird_species, municipality, location, additional_info, user_id, classes)

    return redirect("/")

@app.route("/edit_sighting/<int:sight_id>")
def edit_sighting(sight_id):
    require_login()
    sight = sightings.get_sight(sight_id)
    if not sight:
        abort(404)
    all_classes = sightings.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in sightings.get_classes(sight_id):
        classes[entry["title"]] = entry["value"]
    return render_template("edit_sighting.html", sight=sight, classes=classes, all_classes=all_classes)

@app.route("/update_sighting", methods=["POST"])
def update_sighting():
    require_login()
    check_csrf()

    sight_id = request.form["sight_id"]
    sight = sightings.get_sight(sight_id)

    if not sight:
        abort(404)

    bird_species = request.form["bird_species"]
    check_requirements(bird_species, small_data_length, True)

    municipality = request.form["municipality"]
    check_requirements(municipality, small_data_length, True)
    
    location = request.form["location"]
    check_requirements(location, small_data_length, True)
    
    additional_info = request.form["additional_info"]
    check_requirements(additional_info, big_data_length, False)

    all_classes = sightings.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            parts = entry.split(":")
            classes.append((parts[0], parts[1]))

    sightings.update_sighting(sight_id, bird_species, municipality, location, additional_info, classes)

    return redirect("/sight/" + str(sight_id))

@app.route("/remove_sighting/<int:sight_id>", methods=["GET", "POST"])
def remove_sighting(sight_id):
    sight = sightings.get_sight(sight_id)
    require_login()
    if request.method == "GET":
        return render_template("remove_sighting.html", sight=sight)
    
    if request.method == "POST":
        if "remove" in request.form:
            sightings.remove_sighting(sight_id)
            return redirect("/")
        else:
            return redirect("/sight/" + str(sight_id))

@app.route("/new_message", methods=["POST"])
def new_message():
    require_login()
    check_csrf()

    message = request.form["message"]
    sight_id = request.form["sight_id"]

    sight = sightings.get_sight(sight_id)
    if not sight:
        abort(404)

    user_id = session["user_id"]

    threads.add_message(sight_id, user_id, message)

    return redirect("/sight/" + str(sight_id))

@app.route("/register")
def register():
    if not "user_id" in session:
        return render_template("register.html")
    return redirect("/")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    
    try:
        users.create_user(username, password1)
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
        

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["csrf_token"] = secrets.token_hex(16)
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/") 