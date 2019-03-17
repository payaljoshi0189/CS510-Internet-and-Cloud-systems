from flask import Flask, render_template,redirect, request, url_for
from model_pydict import model

app = Flask(__name__)
model = model()

@app.route('/reviews')
def index():
    """
    This method returns
    a list of dictionary
    containing movie reviews
    """
    entries = model.select()
    return render_template('index.html', entries=entries)

@app.route('/')
@app.route('/home')
def home():
    """
    Returns home page
    for the application.
    """
    return render_template('home.html')

@app.route('/showReviewForm')
def showReviewForm():
    """
    Returns html form 
    to submit  a movie review
    """
    return render_template('reviewform.html')
    

@app.route('/submitRating', methods = ['POST'])
def submitRating():
    """
    Accpets the POST request from the movie
    review form and processes the form data
    by calling insert method of model class
    """
    model.insert(request.form['moviename'], request.form['yearreleased'],request.form['genre'],
                 request.form['rating'], request.form['review'], request.form['reviewer'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True) 
