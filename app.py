import os
from flask import Flask, request
import pymongo

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return ''


@app.route('/post', methods=['POST'])
def post():
    print("Data receive =================================================================")
    print("json {0}".format(request.get_json()))
    print("Data receive =================================================================")

    if True:
        return "Yay!", 200
    else:
        return "Nay!", 202

if __name__ == '__main__':
    host = os.getenv('IP', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)
