import mysql.connector

__cnx = None


def get_connection():
    global __cnx

    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                    host='127.0.0.1',
                                    database='grocery_store')   
        return __cnx