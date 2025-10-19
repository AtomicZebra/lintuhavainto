import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_sighting(bird_species, municipality, location, additional_info, user_id, classes):
    sql = "INSERT INTO sighting (bird_species, municipality, location, additional_info, user_id, time_added) VALUES (?, ?, ?, ?, ?, datetime('now'))"
    db.execute(sql, [bird_species, municipality, location, additional_info, user_id])

    sight_id = db.last_insert_id()

    sql = """INSERT INTO sighting_classes(sight_id, title, value) VALUES (?,?,?)"""
    for title, value in classes:
        db.execute(sql, [sight_id, title, value])

def get_classes(sight_id):
    sql = '''SELECT title, value FROM sighting_classes WHERE sight_id =?'''
    return db.query(sql, [sight_id])

def get_sighting():
    sql = "SELECT id, bird_species, time_added FROM sighting ORDER BY id DESC"
    return db.query(sql)

def get_sight(sight_id):
    sql = """SELECT 
    sighting.id, 
    sighting.bird_species, 
    sighting.municipality, 
    sighting.location, 
    sighting.additional_info, 
    sighting.time_added, 
    users.username, 
    users.id user_id
    FROM sighting, users
    WHERE sighting.user_id = users.id AND sighting.id = ?"""
    result = db.query(sql,[sight_id])
    return result[0] if result else None

def update_sighting(sight_id, bird_species, municipality, location, additional_info, classes):
    sql = """UPDATE sighting SET 
    bird_species = ?,
    municipality = ?,
    location = ?,
    additional_info = ?
    WHERE id = ?
    """
    db.execute(sql, [bird_species, municipality, location, additional_info, sight_id])

    sql = "DELETE FROM sighting_classes WHERE sight_id = ?"
    db.execute(sql, [sight_id])

    sql = "INSERT INTO sighting_classes(sight_id, title, value) VALUES (?,?,?)"
    for title, value in classes:
        db.execute(sql, [sight_id, title, value])

def remove_sighting(sight_id):
    sql = "DELETE FROM sighting_classes WHERE sight_id = ?"
    db.execute(sql, [sight_id])
    sql = "DELETE FROM thread WHERE sight_id = ?"
    db.execute(sql, [sight_id])
    sql = "DELETE FROM sighting WHERE id = ?"
    db.execute(sql, [sight_id])


def find_sightings(query):
    sql = """SELECT id, bird_species, time_added
    FROM sighting
    WHERE bird_species LIKE ? OR municipality LIKE ? OR location LIKE ?"""
    like = "%" + query + "%"
    return db.query(sql,[like, like, like])