import fresh_tomatoes
import media

# create the movise that will be shown on the page
the_godfather = media.Movie("The Godfather",
	"The aging patriarch of an organized crime dynasty transfers "
	"control of his clandestine empire to his reluctant son.",
	"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg?download",
	"https://www.youtube.com/watch?v=sY1S34973zA")

avatar = media.Movie("Avatar",
	"A paraplegic marine dispatched to the moon Pandora on unique "
	"mission becomes torn between following his orders and protecting "
	"the world he feels is his home.",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_matrix = media.Movie("The Matrix",
	"A computer hacker learns from mysterious rebels about the true nature "
	"of his reality and his role in the war against its controllers.",
	"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
	"https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
	"Two imprisoned men bond over a number of years "
	"finding solace and eventual redemption through acts of common decency.",
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	"https://www.youtube.com/watch?v=6hB3S9bIaco")

#add to an array
movies = [the_godfather, avatar, the_matrix, the_shawshank_redemption]

#open webbrowser with preloaded page
fresh_tomatoes.open_movies_page(movies)
