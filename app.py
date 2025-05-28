from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return '¡Hola Mundo desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)