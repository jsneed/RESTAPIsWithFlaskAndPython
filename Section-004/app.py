from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, default = "", location = 'json')
        self.reqparse.add_argument('price', type = float, default = 0.0, location = 'json')

    def find_item(self, name):
        for item in items:
            if(item['name'] == name):
                return item
        return None

    def get(self, name):
        item = self.find_item(name)
        if(not item): return {'item': None}, 404
        return item

    def post(self, name):
        args = self.reqparse.parse_args()
        item = {'name': name, 'price': args['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return items

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:8080/item/bread
api.add_resource(ItemList, '/items') # http://127.0.0.1:8080/items

app.run(port=8080)
