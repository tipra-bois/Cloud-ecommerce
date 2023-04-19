from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)



client = MongoClient()
db = client.ecommerce
products = db.products

@app.route('/products', methods=['GET'])
def get_products():
    all_products = list(products.find())
    return jsonify({'products': all_products})

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    product_id = products.insert_one(new_product).inserted_id
    return jsonify({'product_id': str(product_id)})

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.find_one({'_id': ObjectId(product_id)})
    return jsonify({'product': product})

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    products.update_one({'_id': ObjectId(product_id)}, {'$set': updated_product})
    return jsonify({'message': 'Product updated'})

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    products.delete_one({'_id': ObjectId(product_id)})
    return jsonify({'message': 'Product deleted'})


if __name__ == '__main__':
    app.run(port=5005)