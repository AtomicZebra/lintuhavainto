import db

def add_sighting(bird_species, kunta, location, additional_info, user_id):
    sql = "INSERT INTO items (bird_species, kunta, location, additional_info, user_id, time_added) VALUES (?, ?, ?, ?, ?, datetime('now'))"
    db.execute(sql, [bird_species, kunta, location, additional_info, user_id])

def get_sighting():
    sql = "SELECT id, bird_species FROM items ORDER BY id DESC"

    return db.query(sql)

def get_sight(sight_id):
    sql = """SELECT items.bird_species, items.kunta, items.location, items.additional_info, items.time_added, users.username
    FROM items, users
    WHERE items.user_id = users.id AND items.id = ?"""
    return db.query(sql,[sight_id])[0]