"""
Inserts movie reviews in a list as a python dictionary
Fetches the data as a list of dictionary upon retrieval
"""

from Model import Model

class model(Model):

    def __init__(self):
        """
        Initializes the list which
        holds dictionaries containing
        movie reviews
        """
        self.movie_reviews = []
        

    def select(self):
        """
        Creates a list of dictionaries.
        Each dictionary contains movie
        review details such as movie name,
        rating, review, etc.
        Returns the list containing
        movie reviews.
        """
        if not self.movie_reviews:
            movie1 = {'movie_name': 'movie1', 'year_released': 2018,'genre':'horror', 'rating': 5, 'review': "Awesome!", 'reviewer': 'AK'}
            movie2 = {'movie_name': 'movie2', 'year_released': 2012,'genre':'suspense', 'rating': 9, 'review': "Bad!", 'reviewer': 'PK'}
            self.movie_reviews.append(movie1)
            self.movie_reviews.append(movie2)
        return self.movie_reviews


    def insert(self, movie_name, year_released, genre, rating, review, reviewer):
        """
        Inserts dictionary of movie rating related 
        details into movie_review list.
        :param movie_name:String
        :param year_released: int
        :param genre: String
        :param rating: int
        :param review: String
        :param reviewer: String
        """
        params = {'movie_name': movie_name, 'year_released': year_released,'genre':genre, 'rating': rating, 'review': review, 'reviewer': reviewer}
        self.movie_reviews.append(params)
        return True
        
        
        
