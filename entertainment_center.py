#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

Avengers_Endgame = media.Movie("Avengers: Endgame",
                        "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
                        "https://upload.wikimedia.org/wikipedia/th/thumb/0/0d/Avengers_Endgame_poster.jpg/220px-Avengers_Endgame_poster.jpg",
                        "https://youtu.be/TcMBFSGVi1c")

print(Avengers_Endgame.storyline)

Avengers_Infinity_War = media.Movie("Avengers: Infinity War",
                     "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                     "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                     "https://youtu.be/6ZfuNTqbHE8")

#print(Avengers_Infinity_War.storyline)
#Avengers_Infinity_War.show_trailer()

Eternals = media.Movie("Eternals", 
                             "The saga of the Eternals, a race of immortal beings who lived on Earth and shaped its history and civilizations.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Eternals_%28film%29_poster.jpeg/220px-Eternals_%28film%29_poster.jpeg",
                             "https://youtu.be/x_me3xsvDgk")

Shang_Chi = media.Movie("Shang Chi and the Legend of the Ten Rings",
                             "Shang-Chi, the master of weaponry-based Kung Fu, is forced to confront his past after being drawn into the Ten Rings organization.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Shang-Chi_and_the_Legend_of_the_Ten_Rings_poster.jpeg/220px-Shang-Chi_and_the_Legend_of_the_Ten_Rings_poster.jpeg",
                             "https://youtu.be/8YjFbMbfXaQ")

Black_Panther = media.Movie("Black Panther",
                                "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.",
                                "https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg",
                                "https://youtu.be/xjDjIWPwcPU")

Thor_Ragnarok = media.Movie("Thor : Ragnarok",
                           "Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.",
                           "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                           "https://youtu.be/ue80QwXMRHg")   

movies = [Avengers_Endgame, Avengers_Infinity_War, Eternals,Shang_Chi, Black_Panther, Thor_Ragnarok]
fresh_tomatoes.open_movies_page(movies)
