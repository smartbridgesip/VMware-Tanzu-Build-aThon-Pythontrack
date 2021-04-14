from flask import Flask

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
session['id']
app.secret_key = 'a'
  
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'studentprofile'
mysql = MySQL(app)
@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        organisation = request.form['organisation']  
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']    
        postalcode = request.form['postalcode'] 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM studentdetails WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO studentdetails VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (username, password, email, organisation, address, city, state, country, postalcode, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM studentdetails WHERE username = % s AND password = % s', (username, password ))
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route("/index")
def index():
    return render_template("index.html")
    

@app.route("/display")
def display():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM studentdetails WHERE id = % s', (session['id'], ))
    account = cursor.fetchone()
    return render_template("display.html", account = account)

@app.route("/update", methods =['GET', 'POST'])
def update():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        organisation = request.form['organisation']  
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']    
        postalcode = request.form['postalcode'] 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM studentdetails WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('UPDATE studentdetails SET  username =% s, password =% s, email =% s, organisation =% s, address =% s, city =% s, state =% s, country =% s, postalcode =% s WHERE id =% s', (username, password, email, organisation, address, city, state, country, postalcode, (session['id'], ), ))
            mysql.connection.commit()
            msg = 'You have successfully updated !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template("update.html", msg = msg)
@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)

   return redirect(url_for('login'))
if __name__ == '__main__':
   app.run(host='0.0.0.0')