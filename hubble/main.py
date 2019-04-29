from django.db.backends.mysql.base import CursorWrapper
import mysql.connector

def get_connection():
    if 'db' not in locals():
        db = mysql.connector.connect(host="heroku_c1eaab334582a09	",user="b0ac306c278038",passwd="cf3ef000",database="hubble41")
    return db

def close_connection():
    if 'db' in locals():
        database.close()

def user_exists(email, password):
    database = get_connection()
    cursor = database.cursor()
    
    sql = "SELECT * FROM user_info WHERE Email=%s AND Password=%s"
    escape = (email, password)

    cursor.execute(sql, escape)

    result = cursor.fetchall()

    return len(result) == 1

print(user_exists("james.kierans99@gmail.com", "james1235"))