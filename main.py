from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return "Deep learning based lung cancer analyzer Flask API repository"
def index():
    return render_template("index.html")

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)

@app.route('/predict/', methods=['GET','POST'])
#def hell_world():
#    return "Hell World!"
def predict():
    imgData = request.get_data()
    print("debug") 
    return "predict"


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000, debug=True)
