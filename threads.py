import db

def add_message(sight_id, user_id, message):
    sql = "INSERT INTO thread (sight_id, user_id, message, time_sent) VALUES (?, ?, ?, datetime('now'))"
    db.execute(sql, [sight_id, user_id, message])

def get_message(sight_id):
    sql = """SELECT thread.id, thread.message, thread.time_sent, users.id user_id, users.username
    FROM thread, users
    WHERE thread.sight_id = ? AND thread.user_id = users.id
    ORDER BY thread.id"""
    return db.query(sql, [sight_id])

def get_single_message(message_id):
    sql = """SELECT 
    thread.id, 
    thread.sight_id,
    thread.user_id,
    thread.message,
    thread.time_sent,
    users.username, 
    users.id user_id
    FROM thread, users
    WHERE thread.user_id = users.id AND thread.id = ?"""
    result = db.query(sql,[message_id])
    return result[0] if result else None    

def remove_message(message_id):
    sql = "DELETE FROM thread WHERE id = ?"
    db.execute(sql, [message_id])