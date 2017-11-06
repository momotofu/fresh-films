import webbrowser

class Movie():
    """
    A Python data structure to store movie related information
    """

    # class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        """
        Movie object constructor that takes a title,
        a storyline, a poster image url, and trailer youtube url,
        as arguments in order to populate instance variables.
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """
        Open and view movie\'s the trailer in a webbrowser
        """
        webbrowser.open(self.trailer_url)
