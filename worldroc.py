import config
from flask import Flask, jsonify, request, render_template
from model import db, app, PageContent


# error handling routing
@app.errorhandler(404)
def page_not_found(error):
    return "This page doesn't exist", 404

@app.route('/')
def index():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.debug = True
    app.run()

