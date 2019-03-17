HOMEWORK#4
The purpose of this homework is to containerize HW3 using Ubuntu 16.04 base image and further making it smaller in size using a different base image.

Description of the application deployed using this container:

This application creates a toy python web application to view and submit movie reviews.

The movie reviews are inserted into sqlite3 table named 'reviews' using HTML form.
The application offers 3 different views:
    1. Default home page
    2. Page to list all the reviews
    3. A form to submit a movie review

The web application can be run on PORT 8000.
The various urls to access the various pages are as follows:
    1. /home or / - Default landing page
    2. /index - To view all the movie reviews
    3. /add - To submit a movie review
