from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello D!o!c!k!e!r!\n"

if __name__== '__main__':
	app.run(debug=True, host='0.0.0.0')