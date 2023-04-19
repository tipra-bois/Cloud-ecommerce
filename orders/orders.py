from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.ecommerce
orders = db.orders

@app.route('/orders', methods=['GET'])
def get_orders():
    all_orders = list(orders.find())
    return jsonify({'orders': all_orders})

@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.json
    order_id = orders.insert_one(new_order).inserted_id
    return jsonify({'order_id': str(order_id)})

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.find_one({'_id': ObjectId(order_id)})
    return jsonify({'order': order})

@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    updated_order = request.json
    orders.update_one({'_id': ObjectId(order_id)}, {'$set': updated_order})
    return jsonify({'message': 'Order updated'})

@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders.delete_one({'_id': ObjectId(order_id)})
    return jsonify({'message': 'Order deleted'})



if __name__ == '__main__':
    app.run(port=5010)