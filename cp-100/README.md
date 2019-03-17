Final Project
This application creates a toy python web application to view movie reviews, to submit movie reviews.
Additionally, it uses two ML APIs:
	1.Cloud Natural Language API
	2.Cloud Vision API.

Cloud Natural API analysizes the sentiment of the 'Review' that was submitted using the Review form. It calculates the sentiment value based on the 'review' form field. e.g for a movie named 'ABC', the reviewer submits the review as 'an excellent movie' in the review field, sentiment analysis will be calculated on the string 'an excellent movie' and based on the value calculated, it will either render a thumbs up or thumbs down while listing the reviews.

Cloud Vision API detects the labels for the image that was uploaded by the user. If the list of labels that is returned by the API matches any of the movie reviews that are currently in the datastore, a list of movie reviews matching the detected labels is returned. If the program fails to match the label with any of the available movie reviews,it returns a random movie review.

The application offers 4 different views:
    1. Default home page
    2. Page to list all the reviews
    3. A form to submit a movie review
    4. A form to upload an image of a movie character

The web application can be run on PORT 8000.
The various urls to access the various pages are as follows:
    1. /home or / - Default landing page
    2. /list - To view all the movie reviews
    3. /add - To submit a movie review
    4. /upload_photo - To submit an image

