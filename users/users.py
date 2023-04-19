from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.ecommerce
users = db.users

@app.route('/users', methods=['GET'])
def get_users():
    all_users = list(users.find())
    return jsonify({'users': all_users})

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    user_id = users.insert_one(new_user).inserted_id
    return jsonify({'user_id': str(user_id)})

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.find_one({'_id': ObjectId(user_id)})
    return jsonify({'user': user})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.json
    users.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})
    return jsonify({'message': 'User updated'})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    users.delete_one({'_id': ObjectId(user_id)})
    return jsonify({'message': 'User deleted'})



if __name__ == '__main__':
    app.run(port=5000)