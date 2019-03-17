import sqlite3
from Model import Model
from datetime import date
DB_FILE = 'reviews.db'

"""
A movie review flask app.
Table structure for reviews table:
|-----------|------------------|--------|---------|---------|----------|
|movie_name |   year_released  | genre  | rating  | review  | reviewer |
========================================================================
|  movie1   |       2019       | comic  |   9     |   good! |    PJ    |
"""
class model(Model):

    def __init__(self):
        """
        Queries the reviews table, if the
        table does not exist, creates the 
        table.
        """
        connection = self.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
        except sqlite3.Error:
            cursor.execute("create table reviews(movie_name text, year_released Integer,genre text, rating Integer, review text, reviewer text)")
        cursor.close()

        
    def create_connection(self):
        """
        Creates a database connection
        :returns: Connection
        """
        try:
            connection = sqlite3.connect(DB_FILE)
            return connection
        except sqlite3.DatabaseError as error:
            print(error)
            pass
            
    
    def list_reviews(self):
        """
        Gets all the movie reviews
        from the database.
        :return all the movie reviews
        """
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()

    def insert_reviews(self, submitted_review):
        """
        Inserts the movie review
        into database table
        :param submitted_review:tuple 
        containing movie review
        """
        
        sql = '''INSERT INTO reviews(movie_name, year_released, genre, rating, review, reviewer) values(?,?,?,?,?,?)'''    
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, submitted_review)
        connection.commit()
        cursor.close()
        return True
    
        
        
        
    
