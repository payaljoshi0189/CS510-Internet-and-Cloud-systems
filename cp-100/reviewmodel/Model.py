# Hannah Galbraith
# Payal Joshi
# CS510 Internet & Cloud Systems Final Project

class Model():

    def select(self):
        """
        Gets all the movie reviews
        as a list of dictionaries
        :return all the movie reviews
        """
        pass

    def insert(self,movie_name, year_released, genre, rating, review, reviewer):
        """
        Inserts movie reviews into a dictionary
        structure and appends the data to a list
        :param movie_name:String
        :param year_released: String
        :param genre: String
        :param rating: String
        :param review: String
        :param reviewer: String
        """
        pass

    def detect_labels_get_review(self, filename):
        """ Expects a filename as an argument. Uses the Google Cloud Vision API
        to detect labels for a given image.
        :param filename: String """
        pass

    def find_review(self, labels):
        """ Expects a list of labels as an argument. Iterates through the list
        of movie reviews to find a review that contains one of the labels.
        :param labels: List of Strings """
        pass

    def calculate_sentiment(self, review):
        """ Expects a value that is passed in the 'Review' field of the 
        reviewform. Uses the Google Cloud Language API to detect sentiment in 
        the text.
        :param review: String """
        pass
        
