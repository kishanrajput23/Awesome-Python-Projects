import MySQLdb
u = None

def db(what,username):
    db = MySQLdb.connect("localhost","root","toor","credentials")
    cursor = db.cursor()
    if what == 'get_auth_salt':
        cursor.execute("SELECT AUTH_SALT FROM CLIENT WHERE USER = '" + username + "'")
        data_tmp = cursor.fetchone()
        data = data_tmp[0]
        return data


