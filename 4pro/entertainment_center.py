# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!
import media
import fresh_tomatoes

toy_story = media.Movie("TOY STORY",
                        "a story of boy and his toys that come to life",
                        """https://upload.wikimedia.org/wikipedia/commons/8/
8a/Toy_Stoy_3_logo.svg""",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     """https://upload.wikimedia.org/wikipedia/commons/f/f3/
Avatar_bodypainting_%289411449159%29.jpg""",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock", "A story of a rock band",
                             """https://upload.wikimedia.org/wikipedia/commons/9/95/
James_Scholle.jpeg""", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          """unthinkable combination of a rat and a 5-star gourmet
restaurant""",
                          """https://upload.wikimedia.org/wikipedia/commons/0/03/
Anthrocon_2007_KT_con_shirt.jpg""",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight_in_Paris",
                                """This is a romantic comedy set in Paris about a family that goes
there because of business""",   """https://upload.wikimedia.org/wikipedia/
commons/d/df/Midnight_in_Paris%2C_October_2011.jpg""",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger_Games",
                           """dystopian science fiction adventure film directed by Gary Ross and
 based on the novel of the same name""", """https://upload.wikimedia.org/
wikipedia/commons/7/79/The_hunger_games.svg""",
                           """https://www.youtube.com/watch?v=mfmrPu43DF8""")

movies = [toy_story, avatar, school_of_rock,
          ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
