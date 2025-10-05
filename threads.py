import db

def add_message(item_id, user_id, message):
    sql = "INSERT INTO thread (item_id, user_id, message, time_sent) VALUES (?, ?, ?, datetime('now'))"
    db.execute(sql, [item_id, user_id, message])

def get_message(item_id):
    sql = """SELECT thread.message, thread.time_sent, users.id user_id, users.username
    FROM thread, users
    WHERE thread.item_id = ? AND thread.user_id = users.id
    ORDER BY thread.id"""
    return db.query(sql, [item_id])