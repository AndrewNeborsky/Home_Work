from flask import Flask, render_template
from sqlite3 import connect

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!!!'


@app.route('/persons/')
def get_persons():
    db = connect('persons.db')
    cursor = db.execute('SELECT name FROM persons')
    value = [value[0] for value in cursor]
    return '<p>'.join(value)


@app.route('/persons/<name>/')
def get_person(name):
    db = connect('persons.db')
    cursor = db.execute('SELECT name, age, profession FROM persons')
    value = ['<b>Age:</b> %s; <b>profession:</b> %s' % (value[1], value[2]) for value in cursor if value[0] == name]

    if not value:
        return 'Person is not found'
    return '<p>'.join(value)


@app.route('/persons/<name>/<parameter>')
def get_parameter(name, parameter):
    db = connect('persons.db')
    cursor = db.execute('SELECT name, age, profession FROM persons')

    if parameter == 'age':
        value = ['<b>Age:</b> %s' % value[1] for value in cursor if value[0] == name]
    elif parameter == 'profession':
        value = ['<b>Profession:</b> %s' % value[2] for value in cursor if value[0] == name]

    if not value:
        return 'Person is not found'
    return '<p>'.join(value)


if __name__ == "__main__":
    app.run(debug=True, port=80)
