import webbrowser
# Class
class Movie():
	# lets give the constructor the needed parameter
	def __init__(self, movie_title, move_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = move_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# this method opens the trailer for the movie
	def show_trailer(self):
		webbrowser.open(self.trailer_url)
