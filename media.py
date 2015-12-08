import webbrowser
#This class containes the information about a movie
class Movie():
	#lets give the constructor the needed parameter
	def __init__(self, movie_title, move_storyline, poster_image, trailer_youtube):
		#movie title
		self.title = movie_title
		#short describition of the story line
		self.storyline = move_storyline
		#poster image of the movie if avaiable
		self.poster_image_url = poster_image
		#link to the trailer or the movie
		self.trailer_youtube_url = trailer_youtube

	#call this function to open webbrowser with url
	def show_trailer(self):
		webbrowser.open(self.trailer_url)
