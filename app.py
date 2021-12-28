#!python3

from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():

    data = pd.read_csv('data.csv').to_json()

    return render_template('index.html', data = data)

if __name__ == '__main__':

    app.run(debug=True)
