from flask import Flask ,render_template,request,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.secret_key = 'a'
app.config['MYSQL_HOST'] = "remotemysql.com"
app.config['MYSQL_USER'] = "ath06As5XG"
app.config['MYSQL_PASSWORD'] = "0uKsAfnsVT"
app.config['MYSQL_DB'] = "ath06As5XG"

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("apply.html")

@app.route('/uploaddata',methods =["POST"])
def uploaddata():
    if request.method =="POST":
        name = request.form["name"]
        email = request.form["email"]
        stream = request.form["stream"]
        address = request.form["address"]
        session['username']  = name
      
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO newtable VALUES(NULL,% s,% s,% s,% s)',(name,email,stream,address))
        mysql.connection.commit()
        msg = "you have sucessfully got registered"
    return render_template("apply.html",msg = msg)
@app.route('/display')
def display():
    print(session['name'])
    print(type(session['name']))
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM newtable WHERE name = %s', (session['username'],))
    account = cursor.fetchone()
    print(account)
    session.pop('username')
    return render_template("apply.html",account = account)
    


if __name__ == '__main__':
    app.run(debug = True)