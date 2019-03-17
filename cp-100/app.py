# Hannah Galbraith
# Payal Joshi
# CS510 Internet & Cloud Systems Final Project

from flask import Flask, render_template,redirect, request, url_for,Blueprint
from google.cloud import storage


import reviewmodel
import os

CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')

app = Flask(__name__)
model = reviewmodel.get_model()

@app.route('/list')
def list():
    """ Grabs all the movie reviews from model and renders list of reviews """
    reviews = model.select()
    return render_template('list.html',entries=reviews)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    """
    Returns home page
    for the application.
    """
    return render_template('home.html')


@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
    """ Returns a form to upload a photo. If method == POST, it stores photo in 
    Google Cloud Storage Bucket and then gets movie review result from the model
    based on the photo submitted. Renders template based on whether the review was
    randomly selected or selected via a label. """
    if request.method == 'POST':
        photo = request.files['file']

        # Create a Cloud Storage Client
        storage_client = storage.Client()

        # Get the bucket that the photo will be uploaded to
        bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)

        # Create a new blob and upload the file's content
        blob = bucket.blob(photo.filename)
        blob.upload_from_string(photo.read(), content_type=photo.content_type)

        # Make the blob publicly viewable
        blob.make_public()

        # Detect labels in the photo
        # 'result' is a tuple
        # result[0] = dictionary with review in it
        # result[1] = T/F flag indicating whether or not a review was found
        # that matches a label
        result = model.detect_labels_get_review(photo.filename)
        if result[1] == True:
            return render_template("movie_review.html", entry=result[0])
        else:
            return render_template("random_review.html", entry=result[0])

    return render_template("upload_photo.html", action="upload_photo")




@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Adds the movie review to the datastore
    """
    if request.method == 'POST':
        model.insert(request.form['movie_name'], request.form['year_released'], request.form['genre'],request.form['rating'], request.form['review'],request.form['reviewer'] )
        return redirect('/list')

    return render_template("reviewform.html", action="Add", review={})




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True) 
