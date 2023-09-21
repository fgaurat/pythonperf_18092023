from flask import Flask,render_template
from Person import Person
from PersonDAO import PersonDAO

app = Flask(__name__)

@app.route("/")
def index():
    dao = PersonDAO('persons.db')

    return render_template('persons.html',persons=dao.findAll())
