from mysql.connector import connection, cursor
from sql_connection import get_connection
from datetime import datetime

def insert_order(connection, order_details):
   
    cursor = connection.cursor()
    query = ("INSERT INTO orders(customer_name, total,datetime)"
             "Values(%s, %s, %s);")
    data = (order_details['customer_name'], order_details['grand_total'], order_details['datetime'])
    cursor.execute(query, data)
    connection.commit()
    order_id = cursor.lastrowid
    
    order_details_query = ("INSERT INTO order_details(order_id,product_id, quantity, total_price)"
             "VALUES(%s,%s,%s,%s);")
    orders = []
    
    for order_detail in order_details['orders']:
        
        orders.append([
            order_id,
            int(order_detail['product_id']),
            float(order_detail['quantity']),
            float(order_detail['total_price'])
        ]
            
        )
    
    cursor.executemany(order_details_query, orders)
    connection.commit()
    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("select * from orders")
    cursor.execute(query)
    
    response = []
    
    for(order_id, customer_name, total, datetime) in cursor:
        response.append({
            'order_id': order_id,
            'customer': customer_name,
            'total': total,
            'datetime': datetime
        }
            
        )
    return response
    
def get_order_details(connection, order_id):
    cursor = connection.cursor()
    query = ("select orders.customer_name as customer, products.name as product, quantity, total_price "
				"from order_details "
                "inner join orders on order_details.order_id = orders.order_id "
                "inner join products on order_details.product_id = products.product_id "
                "where order_details.order_id = " + str(order_id))
    
    cursor.execute(query)
    
    response = []
    
    for(customer,product,quantity,total_price) in cursor:
        response.append({
            'customer': customer,
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        }
            
        )
    return response
if __name__=="__main__":
    connection = get_connection()
    order_details ={
        'customer_name': 'pravin',
        'grand_total': 921,
        'datetime':  datetime.now(),
        'orders':
            [{
            'product_id': 7,
            'quantity': 2,
            'total_price': 52
            },
            {
            'product_id': 6,
            'quantity': 6,
            'total_price': 208
            }]
    }
    print(insert_order(connection, order_details))
        
    