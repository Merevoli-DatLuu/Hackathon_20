import flask
from flask import request, render_template, jsonify
import db_connection
import processing

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

@app.route('/api/v1/resource/Score/all', methods=['GET'])
def get_score():
    rr = processing.get_score()
    return jsonify(rr)

@app.route('/api/v1/resource/skillGraph/all', methods=['GET'])
def get_skillgraph():
    rr = processing.processing_skill_value(processing.processing_subject(processing.get_score("ST0003")))
    return jsonify(rr)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        id = request.form['id'] 
        password = request.form['password']
        
        db = db_connection.db_connection()
        data = db.query("SELECT * FROM `user` WHERE user_id = \""+ id + "\" and user_password = \"" + password + "\"")
        if len(data) == 0:
            pass
    
@app.route('/index')
def index():
    return render_template("index_test.html")

if __name__ == "main":
    app.run()
