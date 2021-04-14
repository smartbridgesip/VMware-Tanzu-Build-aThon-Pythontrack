# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:46:26 2021

@author: prads

"""
from flask import Flask,redirect, url_for
app = Flask(__name__)
@app.route('/admin')
def hello_admin():
    return "hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s guest" %guest

@app.route('/user/<name>')
def hello_user(name):
    if (name == 'admin'):
        return redirect(url_for({}))
    else :
        return redirect(url_for('hello_guest',guest = name))


    
if __name__ == '__main__':
    app.run(debug = True) # local host web browser localhost



