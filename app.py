from flask import Flask, render_template, url_for, request
import subprocess
import urllib
import csv
app = Flask(__name__)


@app.route('/')
def main():
        
        return render_template("index.html",**locals())