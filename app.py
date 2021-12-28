#!python3

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from data import get_data

app = Flask(__name__)

@app.route('/')
def index():

    data = get_data()

    return jsonify(data)

if __name__ == '__main__':

    app.run(debug=True)
