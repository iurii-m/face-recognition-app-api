import os

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)

db = SQLAlchemy()


@app.route('/', methods=['GET'])
def index():
    """
    Example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'


@app.route('/add', methods=['POST'])
def hello():
    return "Add endpoint"


@app.route('/get/<string:embeddings>', methods=['GET'])
def search_person(embeddings):
    return "Embeddings endpoint"


@app.route('/all', methods=['GET'])
def hello():
    return "Get all endpoint - Might be useless"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
