# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:51:27 2021

@author: AFB
"""
#nach jeder Veränderung -> speichern und in gitBash
# python -m flask run eingeben??? wenn development ausgeschaltet
from flask import Flask

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

@app.route("/isbn")
def isbn_display():
    return"<p>ISBN given: </p>"
    