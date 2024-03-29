from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
	if (functionName == 'add' or functionName == 'Subtract' or functionName == 'Multiply'):
		if "x" not in postedData or "y" not in postedData:
			return 301
		else:
			return 200
	elif (functionName == 'Division'):
		if "x" not in postedData or "y" not in postedData:
			return 301
		elif int(postedData["y"])==0:
			return 302
		else:
			return 200

class Add(Resource):
	def post(self):
		postedData = request.get_json()

		status_code = checkPostedData(postedData, "add")
		if (status_code!=200):
			retJson = {
				"Message": "An error happened",
				"status": status_code
			}
			return jsonify(retJson)


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
	def post(self):
		postedData = request.get_json()
		status_code = checkPostedData(postedData, "Subtract")		
		if (status_code!=200):
			retJson = {
				"Message": "An error Happened",
				"status": status_code
			}
			return jsonify(retJson)
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)
		ret = x-y
		retMap = {
			'Message': ret,
			'Status Code': 200
		}
		return jsonify(retMap)

class Multiply(Resource):
	def post(self):
		postedData = request.get_json()
		status_code = checkPostedData(postedData, "Multiply")		
		if (status_code!=200):
			retJson = {
				"Message": "An error Happened",
				"status": status_code
			}
			return jsonify(retJson)
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)
		ret = x*y
		retMap = {
			'Message': ret,
			'Status Code': 200
		}
		return jsonify(retMap)

class Divide(Resource):
	def post(self):
		postedData = request.get_json()
		status_code = checkPostedData(postedData, "Division")		
		if (status_code!=200):
			retJson = {
				"Message": "An error Happened",
				"status": status_code
			}
			return jsonify(retJson)
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)
		ret = (x*1.0)/y
		retMap = {
			'Message': ret,
			'Status Code': 200
		}
		return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/Subtract")
api.add_resource(Multiply, "/Multiply")
api.add_resource(Divide, "/Division")

@app.route('/')
def hello_world():
	return "Hello World!"
