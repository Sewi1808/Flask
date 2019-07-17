from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello_world!"

@app.route('/json')
def json_test():
	someJson = {
		'key1':'value1' 
		'key2':'value2'
	}
	return jsonify(someJson)

if __name__=="__main__":
	app.run(debug=True)