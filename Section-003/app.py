from flask import Flask, jsonify, request

app = Flask(__name__)
'''
@app.route('/')
def home():
    return 'hello world'
'''

stores = [
    {
        'name': 'ThriftMart',
        'items': [
            {
                'name': 'Tooth Paste',
                'price': 2.25
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    store = {
        'name': data['name'],
        'items': []
    }
    stores.append(store)
    return jsonify(store)

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')
def get_store(name):
    store = find_store(name)
    if not store: return jsonify({'message': 'Store not found'})
    return jsonify(store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    store = find_store(name)
    if not store: return jsonify({'message': 'Store not found'})
    data = request.get_json()
    store['items'].append({'name': data['name'], 'price': data['price']})
    return jsonify(store)

@app.route('/store/<string:name>/item')
def get_store_items(name):
    store = find_store(name)
    if not store: return jsonify({'message': 'Store not found'})
    return jsonify(store['items'])

def find_store(name):
    for store in stores:
        if store['name'] == name: return store
    return None

app.run(port=8080)