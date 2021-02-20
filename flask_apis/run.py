# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name is mandatory")


class Plants(Resource):

    def __init__(self):
        self.name = parser.parse_args().get('name', None)

    def get(self):
        response = {}
        response[self.name] = self.name
        return response



api.add_resource(Plants, '/get_details')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True
