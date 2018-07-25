import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "Avatar poster link",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock","Storyline",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","SToryline",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games", "storyline",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
print(media.Movie.__module__)
