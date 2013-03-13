import config
import io
from flask import Flask, jsonify, request, render_template
#from model import PageContent

app = Flask(__name__)

# error handling routing
@app.errorhandler(404)
def page_not_found(error):
    return "This page doesn't exist", 404

@app.route('/')
def index():
    childDir = 'static/img/children_pictures/'
    childPictures = io.loadPictures(childDir)
    return render_template('home.html', title='Home', childDir=childDir, childPictures=childPictures)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact us')

if __name__ == '__main__':
    app.debug = True
    app.run()

