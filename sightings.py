import db

def add_sighting(bird_species, municipality, location, additional_info, user_id):
    sql = "INSERT INTO items (bird_species, municipality, location, additional_info, user_id, time_added) VALUES (?, ?, ?, ?, ?, datetime('now'))"
    db.execute(sql, [bird_species, municipality, location, additional_info, user_id])

def get_sighting():
    sql = "SELECT id, bird_species, time_added FROM items ORDER BY id DESC"

    return db.query(sql)

def get_sight(sight_id):
    sql = """SELECT 
    items.id, 
    items.bird_species, 
    items.municipality, 
    items.location, 
    items.additional_info, 
    items.time_added, 
    users.username, 
    users.id user_id
    FROM items, users
    WHERE items.user_id = users.id AND items.id = ?"""
    result = db.query(sql,[sight_id])
    return result[0] if result else None

def update_sighting(sight_id, bird_species, municipality, location, additional_info):
    sql = """UPDATE items SET 
    bird_species = ?,
    municipality = ?,
    location = ?,
    additional_info = ?
    WHERE id = ?
    """
    db.execute(sql, [bird_species, municipality, location, additional_info, sight_id])

def remove_sighting(sight_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [sight_id])

def find_sightings(query):
    sql = """SELECT id, bird_species, time_added
    FROM items
    WHERE bird_species LIKE ? OR municipality LIKE ? OR location LIKE ?"""
    like = "%" + query + "%"
    return db.query(sql,[like, like, like])