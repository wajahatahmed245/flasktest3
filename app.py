import flask
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

v='ww'
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "pucit123", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
cur.execute("SELECT  * from employees ")
rows = cur.fetchall()

@app.route('/')
def hello_world():
    return render_template('root.html')


@app.route('/login')
def login():
    name='isra'
    return render_template('index.html')


@app.route('/showdata')
def showdb():

    return render_template('databasedata.html',row=rows)


@app.route('/submitdata')
def submit():
    return render_template('submiting_data.html')


@app.route('/deleteRows/<int:id>')
def delete(id):
    cur.execute("DELETE from employees where ID= {};".format(id))
    conn.commit()
    return 'deleted {}'.format(id)


if __name__ == '__main__':
    app.run()
