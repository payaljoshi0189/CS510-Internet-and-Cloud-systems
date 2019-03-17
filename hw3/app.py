from flask import Flask, render_template,redirect, request, url_for
from model_sqlite3 import model

app = Flask(__name__)
model = model()

@app.route('/index')
def index():
    """
    This method returns
    a list containing movie 
    reviews retrieved from database
    """
    reviews = [dict(movie_name = row[0],year_released = row[1], genre = row[2],rating = row[3], review = row[4], reviewer = row[5] )\
               for row in model.list_reviews()]
    return render_template('index.html', reviews=reviews)

@app.route('/')
@app.route('/home')
def home():
    """
    Returns home page
    for the application.
    """
    return render_template('home.html')

@app.route('/add')
def add():
    """
    Returns html form 
    to submit  a movie review
    """
    return render_template('reviewForm.html')
    

@app.route('/submitRating', methods = ['POST'])
def submitRating():
    """
    Accpets the POST request from the movie
    review form and inserts the form data
    into database by calling insert method of 
    model class
    """
    submitted_review = ()
    submitted_review = (request.form['movie_name'], request.form['year_released'],request.form['genre'],
                 request.form['rating'], request.form['review'], request.form['reviewer'])
    model.insert_reviews(submitted_review)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
