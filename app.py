import os
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return ''


@app.route('/post', methods=['POST'])
def post():
    print("Data receive =================================================================")
    print("json {0}".format(request.get_json()))
    print("Data receive =================================================================")


    data = request.get_json();

    # connection = MongoClient('mongodb://user:password@localhost:27017/database')
    connection = MongoClient('mongodb://localhost:27017/database')
    connection.database_names()
    db = connection.database
    posts = db.posts
    post_id = posts.insert(data)

    if post_id:
        return "Inserted " + str(post_id), 200
    else:
        return "Error inserting data.", 202

if __name__ == '__main__':
    host = os.getenv('IP', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)
