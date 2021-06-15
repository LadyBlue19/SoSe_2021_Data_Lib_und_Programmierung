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

@app.route("/") #Decorator
def start_page():
    return "<p>Hello World! <p>"
