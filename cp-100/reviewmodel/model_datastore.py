# Hannah Galbraith
# Payal Joshi
# CS510 Internet & Cloud Systems Final Project

from .Model import Model

from google.cloud import datastore
from google.cloud import storage
from google.cloud import vision
from google.protobuf import json_format
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import random
import argparse
import io
import re
import os
import six

CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')
PROJECT_ID = os.environ.get('PROJECT_ID')


class model(Model):
    def __init__(self):
        """ Initializes the datastore client using the PROJECT_ID environment variable. """
        self.client = datastore.Client(PROJECT_ID)

    def select(self):
        """ Queries the datastore to fetch all movie reviews. Stores each movie review in a list of dicts. """
        query = self.client.query(kind = 'Movie_Review')
        movie_reviews = []
        for row in list(query.fetch()):
            rev = {}
            rev['movie_name'] = row['title']
            rev['year_released'] = row['year']
            rev['genre'] = row['genre']
            rev['rating'] = row['rating']
            rev['review'] = row['review']
            rev['reviewer'] = row['reviewer']
            rev['sentiment'] = row['sentiment']
            movie_reviews.append(rev)
        return movie_reviews

    def insert(self,movie_name,year_released,genre,rating,review,reviewer):
        """ Creates a new movie review entity in the datastore.
            :param movie_name: String
            :param year_released: String
            :param genre: String
            :param rating: String
            :param review: String
            :param reviewer: String """
        key = self.client.key('Movie_Review')
        rev = datastore.Entity(key)
        #Calculate the sentiment based on the value submitted for the review field of the reviewform
        if review != "":
        	sentiment = self.calculate_sentiment(review)
        rev.update({'title': movie_name, 'year' : year_released, 'genre' : genre, 'rating' : rating, 'review' : review, 'reviewer' : reviewer, 'sentiment': sentiment})
        self.client.put(rev)
        return True

    def detect_labels_get_review(self, filename):
        """ Expects a filename as an argument. Uses the Google Cloud Vision API to detect labels for a given image.
        Returns a tuple ("result") where
        result[0] = a dictionary containing a movie review 
        result[1] = a boolean flag indicating whether a review was selected from a label (T) or randomly selected (F)
        :param filename: String """

        # Initialize a Google Cloud Vision client and give it an image stored in the Google Cloud Storage Bucket
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = "gs://{}/{}".format(CLOUD_STORAGE_BUCKET, filename)

        # Get a response from the API and extract the labels from it
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # Give the labels to the find_review method and return its result to the calling routine
        result = self.find_review(labels)
        return result

    def find_review(self, labels):
        """ Expects a list of labels as an argument. Iterates through the list of movie reviews to find a 
        review that contains one of the labels. If so, it returns a tuple where the first index is the review
        and the second index is a boolean flag set to true. Otherwise, it returns a tuple with a randomly-selected
        review and a boolean flag set to false.
        :param labels: List of Strings """
        movie_reviews = self.select()

        flag = False
        for label in labels:
            for rev in movie_reviews:
                if label.description in rev['review'].lower():
                    flag = True
                    return (rev, flag)

        return (random.choice(movie_reviews), flag)
        
    def calculate_sentiment(self, review):
    
    	"""Expects a value that is passed in the 'Review' field of the reviewform
    	Uses the Google Cloud Language API to detect sentiment in the text.
        :param review: String"""
    	client = language.LanguageServiceClient()
    	
    	if isinstance(review, six.binary_type):
    		review = review.decode('utf-8')
    	
    	#Instantiates a plain text document
    	document  = types.Document(content=review, type=enums.Document.Type.PLAIN_TEXT)
    	
    	#Detects sentiment in the document
    	sentiment = client.analyze_sentiment(document).document_sentiment
    	return sentiment.score
