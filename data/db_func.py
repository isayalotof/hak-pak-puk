from data.database import c, db

def get_user_query_info(user_id):
    c.execute("""SELECT query_info
                 FROM user_query 
                 WHERE user_id = ?""", (user_id,))
    rows = c.fetchall()
    result = [row[0] for row in rows]
    return result

def get_user_rec_info(user_id, query_info):
    c.execute("""SELECT info
                 FROM user_query 
                 WHERE user_id = ? AND query_info = ?""", (user_id, query_info))
    rows = c.fetchall()
    result = [row[0] for row in rows]
    return result

def add_user_search(user_id, query_info, info):
    c.execute("""INSERT INTO user_query (user_id, query_info, info)
                 VALUES (?, ?, ?);""", (user_id, query_info, info))
    db.commit()
