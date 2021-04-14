# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:32:58 2021

@author: prads
"""

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/') #localhost:500
def home():
    return  render_template('index.html')
@app.route('/login' ,methods = ["POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return render_template("index.html",y = user)
    

if __name__ ==('__main__'):
    app.run(debug = True)

