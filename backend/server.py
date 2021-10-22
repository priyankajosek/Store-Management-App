import products_dao
import uom_dao
import orders_dao
import json
from flask import Flask, request, jsonify
from sql_connection import get_connection


app = Flask(__name__)

connection = get_connection()

#  To see the products details
@app.route('/products', methods = ['GET'])
def products():
    products = products_dao.get_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For deleting a product with a particular product id
@app.route('/delete', methods = ['GET', 'POST'])
def delete_products():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    print(return_id)
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For adding more products
@app.route('/add', methods = ['GET', 'POST'])
def add_products():
    request_payload = json.loads(request.form['data'])
    return_id = products_dao.add_products(connection, request_payload)
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For editing product details
@app.route('/edit_product', methods = ['GET', 'POST'])
def edit_product():
    request_payload = json.loads(request.form(['data']))
    return_id = products_dao.edit_product(connection, request_payload)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
# For retriving Units of Measurement details 
@app.route('/get_uom', methods=['GET'])
def get_uom():
    uom = uom_dao.get_uom(connection)
    response = jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For inserting new Unit of Measurement
@app.route('/insert_uom', methods = ['GET'])
def insert_uom():
    uom = uom_dao.insert_uom(connection)
    response = jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For inserting new order
@app.route('/insert_order', methods = ['GET', 'POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For retrieving all orders
@app.route('/get_all_orders', methods = ['GET'])
def get_all_orders():
    all_orders = orders_dao.get_all_orders(connection)
    response = jsonify(all_orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# For obtaining details of a particular order
@app.route('/get_order_details', methods=['GET'])
def get_order_details():
    
    order_id = request.form['order_id']
    order_details = orders_dao.get_order_details(connection, order_id)
    response = jsonify(order_details)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug= True)