from app import app
from flask import render_template


@app.route ('/')
def home ():
    return render_template('index.html')

@app.route('/about')
def iCANNameThisAnything():
    return render_template('about.html')

@app.route('/signup')
def signMeUp():
    return {'hi' : "there"}


@app.route('home')
def whatever():
    return render_template('home')

@app.route('favorite5')
def yeah():
    return render_template('favorite5')


    



