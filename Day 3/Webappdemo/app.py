# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '4NicIczkIi'
app.config['MYSQL_PASSWORD'] = 'd5EC2NzRDD'
app.config['MYSQL_DB'] = '4NicIczkIi'
mysql = MySQL(app)
app.secret_key = 'a'

@app.route('/')

def homer():
    return render_template('apply.html')

@app.route('/uploaddata',methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' :
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        stream = request.form['stream']
        address = request.form['address']
        session["username"] = name
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO dummy VALUES (NULL, % s, % s, % s, % s)', (name, email,stream,address))
        mysql.connection.commit()
        msg = 'You have successfully registered !'
    return render_template('apply.html', msg = msg)

@app.route('/display')
def display():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM job WHERE userid = % s', (str(session['id'])))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('apply.html',account = account)

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True, port = 9000)