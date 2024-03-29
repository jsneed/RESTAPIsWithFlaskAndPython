from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def __init__(self):
        pass

    def find_item(self, name):
   
        item = next(filter(lambda n: n['name'] == name, items), None)
        return item

    def get(self, name):
        item = self.find_item(name)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        item = self.find_item(name)
        if item:
            return {'message': f'An item with name {name} already exists'}, 400 

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:8080/item/bread
api.add_resource(ItemList, '/items') # http://127.0.0.1:8080/items

app.run(port=8080, debug=True)
