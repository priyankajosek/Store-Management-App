
from sql_connection import get_connection


def get_products(connection):

    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products INNER JOIN uom "
             "ON products.uom_id = uom.uom_id;")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response


def add_products(connection, product):

    cursor = connection.cursor()

    query = ("insert into products "
             "(name, uom_id, price_per_unit) "
             "values (%s, %s, %s)")
    data = (product['name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def edit_product(connection, product):
    
    cursor = connection.cursor()
    query = ("update products SET name = %s, uom_id = %s, price_per_unit=%s"
             "WHERE product_id = %s")
    data = (product['name'], product['uom_id'], product['price_per_unit'], product['product_id'])
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    print(product_id)
    query = ("delete from products "
             "where product_id = " + str(product_id))

    cursor.execute(query)
    connection.commit()

    return product_id


if __name__ == "__main__":

    connection = get_connection()
    
    product = {
        'name': 'carrots',
        'uom_id': '1',
        'price_per_unit': '30'
    }
    