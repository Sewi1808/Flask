from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
	def post(self):
		postedData = request.get_json()
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)
		ret = x+y
		retMap = {
			'Message': ret,
			'Status Code': 200
		}
		return jsonify(retMap)

class Subtract(Resource):
	pass

class Multiply(Resource):
	pass

class Divide(Resource):
	pass


api=add_resource(Add, "/add")

@app.route('/')
def hello_world():
	return "Hello World!"
