from flask import Flask
from flask_restful import Resource, Api
from PersonDAO import PersonDAO


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return [{'hello': 'world'},{'hello': 'world'},{'hello': 'world'}]


class Persons(Resource):

    def __init__(self):
        self._dao = PersonDAO("persons.db")

    def get(self):
        return list(self._dao.findAllAsJson())

api.add_resource(HelloWorld, '/')
api.add_resource(Persons, '/persons')

if __name__ == '__main__':
    app.run(debug=True)


    