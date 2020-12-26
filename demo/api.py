import flask
from flask import request, jsonify
import db_connection

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resource/subject/all', methods=['GET'])
def get_subject():
    db = db_connection.db_connection()
    data = db.query("SELECT * FROM Subject")
    header = ["id", "name"]
    rr = []
    for i in data:
        rt = {}
        for j in range(len(header)):
            rt[header[j]] = i[j]
        rr.append(rt)
    return jsonify(rr)

app.run()