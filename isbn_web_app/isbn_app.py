# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:51:27 2021

@author: AFB
"""
#nach jeder Veränderung -> speichern und in gitBash
# python -m flask run eingeben??? 
# wenn development ausgeschaltet ist, dann nicht, nur site erneuern
from flask import Flask, render_template


print (__name__)
app = Flask (__name__)
"""
Website... http://127.0.0.1:5000/
"""
@app.route("/") #Startseite
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info") #Informationsseite
def show_info():
    return "<p>Some Information</p>"

@app.route("/isbn/<isbn>")#<..> ist ein Platzhalter. Dh. dahinter muss noch was kommen. in dem Fall eine Zahl
def isbn_display(isbn):
    return render_template("isbn_display.html")
    