from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello_world!"

@app.route('/json')
def json_test():
	someJson = {
		'key1':'value1',
		'key2':'value2'
	}
	return jsonify(someJson)

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
	# get x y from post
	dataDict = request.get_json()
	x = dataDict["x"]
	y = dataDict["y"]
	#add x + y =z
	z = x + y
	retJSON = {
		"z" : z
	}
	#return jsonify(map_prepared)
	return jsonify(retJSON), 200

if __name__=="__main__":
	app.run(debug=True)