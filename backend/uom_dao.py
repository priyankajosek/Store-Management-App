from mysql.connector import connect, connection, cursor
from sql_connection import get_connection 

def get_uom(connection):
    
    cursor = connection.cursor()
    query = ('SELECT * FROM uom;')
    cursor.execute(query)
    response = []

    for(uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })

    return response


def insert_uom(connection):
    cursor = connection.cursor()
    query = ('SELECT * FROM uom;')
    cursor.execute(query)
    response = []

    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })

    return response



if __name__ == "__main__":

    connection = get_connection()    
    uom = get_uom(connection)
