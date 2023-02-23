from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_method():
    return jsonify({'message': "This is Manya's server"})


@app.route('/', methods=['POST'])
def post_method():
    response_message = request.get_json()
    return jsonify(response_message)


if __name__ == '__main__':
    app.run(debug=True)




