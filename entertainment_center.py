import fresh_tomatoes
import media


# initialize the values in the movie class

Avengers = media.Movie("Avengers Infinity War",
                       "superhero film based on the Marvel Comics",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                       "https://youtu.be/6ZfuNTqbHE8")

Doctor = media.Movie("Doctor Strange",
                     "Strange learns the mystic arts after a car accident",
                     "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                     "https://youtu.be/HSzx-zryEgM")

Spider = media.Movie("Spider-Man: Homecoming",
                     "Peter(SpiderMan) tries to balance high school life.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                     "https://youtu.be/U0D3AOldjMU")

Ddlj = media.Movie("Dilwale Dulhania Le Jayenge",
                   "non-resident Indians, who fall in love during a vacation",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg/220px-Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                   "https://youtu.be/UdE_vL9LhfE")

Friends = media.Movie("Friends with Benefits",
                      "they have develop deep mutual feelings for each other.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Friends_with_benefits_poster.jpg/220px-Friends_with_benefits_poster.jpg",
                      "https://youtu.be/wMVO79F9jSk")

whiplash = media.Movie("Whiplash",
                       "Andrew is a 1st year student at Shaffer Conservatory.",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                       "https://youtu.be/7d_jQycdQGo")

# fresh_tomatoes allows to turn this code into a movie website
# The open_movies_page function takes a list or array of movies to show output
# an html webpage or website that shows those movies
movies = [Avengers, Doctor, Spider, Ddlj, Friends, whiplash]
fresh_tomatoes.open_movies_page(movies)
