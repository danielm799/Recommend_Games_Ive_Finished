class Titles:
    #instance properties/attributes i forgot the names
    def __init__(self, title, genres=None, critic_rating=None):
        self.title = title
        if genres == None:
            self.genres = []
        else:
            self.genres = genres
        if critic_rating == None:
            self.critic_rating = "Nothing yet"
        else:
            self.critic_rating = critic_rating
    
    #for if i want to print out everything about the title
    def get_title_info(self):
        return f""""
        Name: {self.title}
        Genre: {self.genres}
        Metacritic Rating: {self.critic_rating}
        """
    
    #just makes getting the title itself easier.
    def get_title(self):
        return self.title
    def get_genres(self):
        return self.genres
    def get_critic_rating(self):
        return self.critic_rating

class Genres:
    #you know im pretty sure theyre called instance properties
    def __init__(self, genre, titles=None):
        self.genre = genre
        if titles == None:
            self.titles = []
        else:
            self.titles = titles
    
    #iterated through the title objects in self.title and run .get_title_info() on them
    def get_genre_and_titles(self):
        print(f"The titles associated with {self.genre} are/is: ")
        for elem in self.titles:
            print(elem.get_title_info())
    
    #to get titles and genre
    def get_titles(self):
        return [elem.title for elem in self.titles]
    def get_genre(self):
        return self.genre
    
    #lets add in 2 true/false methods to be used with adding a title to a genre
    def title_belongs_under_genre(self, title_object):
        title_genre_list = title_object.get_genres()
        return self.genre in title_genre_list
    def title_already_in_list(self, title_object):
        return title_object in self.titles
    
    #core function that takes a title_object and makes a connects the genre object to the title object if there is a match and if there already is not a
    #connection
    def add_title(self, title_object):
        title_string = title_object.get_title()
        #print(f"{self.genre}'s title list before method starts: {[elem.title for elem in self.titles]}")
        if self.title_belongs_under_genre(title_object) == False:
            print(f"{title_string} does not belong under {self.genre}")
            return
        if self.title_already_in_list(title_object) == True:
            print(f"{title_string} is already under {self.genre}")
            return
        if self.title_belongs_under_genre(title_object) == True and self.title_already_in_list(title_object) == False:
            print(f"Adding {title_string} to {self.genre}")
            self.titles.append(title_object)
            return

    
#use the premade list of titles and make all of the genre objects
horror = Genres("Horror")
action = Genres("Action")
adventure = Genres("Adventure")
soulsLike = Genres("Souls-Like")
platformer = Genres("Platformer")
metroidvania = Genres("Metroidvania")
hacknslash = Genres("Hack 'N Slash")
rpg = Genres("RPG")
roguelite = Genres("Rogue-lite")
mystery = Genres("Mystery")
fantasy = Genres("Fantasy")
crpg = Genres("CRPG")
jrpg = Genres("JRPG")
tactical = Genres("Tactical")
postapoc = Genres("Post-Apocalyptic")
shooter = Genres("Shooter")
#in order to allow the user to access the specific objects, it would be easy to place them into a dictionary
genre_object_dict = {
    "Horror": horror,
    "Action": action,
    "Adventure": adventure,
    "Souls-Like": soulsLike,
    "Platformer": platformer,
    "Metroidvania": metroidvania,
    "Hack 'N Slash": hacknslash,
    "RPG": rpg,
    "Rogue-lite": roguelite,
    "Mystery": mystery,
    "Fantasy": fantasy,
    "CRPG": crpg,
    "JRPG": jrpg,
    "Tactical": tactical,
    "Post-Apocalyptic": postapoc,
    "Shooter": shooter
}
#use that same list to make the title objects. The dictionary below has all that is needed to make a title object
#the string title name and a list of strings that will match that title to the genre dictionary.
title_object_dict = {
    "Alien: Isolation": (["Horror"], 81),
    "Amnesia: Rebirth": (["Horror", "Adventure"]),
    "A Plague Tale: Innocence": ["Adventure", "Action"],
    "Ashen": ["Action", "Adventure", "Souls-Like"],
    "Axiom Verge": ["Platformer", "Metroidvania"],
    "Axiom Verge 2": ["Platformer", "Metroidvania"],
    "Bayonetta": ["Action", "Hack 'N Slash"],
    "Bayonetta 2": ["Action", "Hack 'N Slash"],
    "Blasphemous": ["Platformer", "Metroidvania"],
    "Bloodstained: Ritual of the Night": ["Platformer", "Metroidvania"],
    "Celeste": ["Platformer"],
    "Children of Morta": ["Rogue-lite", "Action", "RPG"],
    "CrossCode": ["Action", "RPG", "Adventure"],
    "Danganronpa V3: Killing Harmony": ["Mystery"],
    "Dark Souls III": ["Action", "RPG", "Souls-Like", "Fantasy"],
    "DELTARUNE": ["RPG"],
    "Disco Elysium": ["RPG", "CRPG"],
    "Divinity: Original Sin II": ["RPG", "Adventure", "Fantasy", "Tactical", "CRPG"],
    "ENDER LILIES: Quietus of the Knights": ["Platformer", "Metroidvania"],
    "Final Fantasy VIII Remastered": ["JRPG", "RPG"],
    "GRIS": ["Platformer", "Adventure"],
    "Going Under": ['Rogue-lite', "Action", "Hack 'N Slash"],
    "Hollow Knight": ["Action", "Adventure", "Platformer", "Metroidvania"],
    "Hyper Light Drifter": ["Action", "Adventure", "RPG"],
    "Layers of Fear: Legacy": ["Horror"],
    "Metro Exodus": ["Post-Apocalyptic", "Shooter", "Action"],
    "NieR Replicant ver.1.22474487139…": ["Action", "RPG", "Adventure", "JRPG"],
    "OMORI": ["RPG", "Horror"],
    "Pillars of Eternity": ["RPG", "CRPG", "Fantasy"],
    "Pillars of Eternity II: Deadfire": ["RPG", "CRPG", "Fantasy"],
    "Prey": ["Horror", "Shooter"],
    "Record of Lodoss War-Deedlit in Wonder Labyrinth-":  ["Platformer", "Metroidvania"],
    "Resident Evil Village": ["Action", "Horror"],
    "STAR WARS Jedi: Fallen Order": ["Action", "Adventure", "Souls-Like"],
    "The Outer Worlds": ["Action", "RPG", "Shooter", "Adventure"],
    "UNSIGHTED": ["Action", "Adventure", "RPG", "Metroidvania", "Souls-Like"],
    "Wasteland 2: Director's Cut": ["RPG", "Adventure", "CRPG", "Tactical" , "Post-Apocalyptic"]
}
#the for loop below is meant to turn everything in that title dictionary into a title object.
for key, value in title_object_dict.items():
    title_object = Titles(key, value)
    title_object_dict[key] = title_object

#This function will iterate through the .genres list of title objects, use the returned strings to point to the correct genre object in the 
#genre dictionary, and use Genre.add_title() to make an edge from the genre object to the title object.
def add_titleObj_to_genreObj(title_obj):
    #print(f"Iterating through {title_obj.title}'s genre list...")
    #print("the genres are: ", title_obj.get_genres())
    for elem in title_obj.genres:
        #print(f"Genre is {elem} and the titles under {elem} are {genre_object_dict[elem].get_titles()}")
        genre_object_dict[elem].add_title(title_obj)

#connect all titles to their relevant genre objects
for value in title_object_dict.values():
    add_titleObj_to_genreObj(value)

#greet the user
print('''
Hello!
What I have here is a program that contains some of the video games I have played and completed. You can use inputs
to traverse the genres I have played games from and thus produce the titles that are associated with that genre.
''')
#this function is meant to cross-check a user input across the genre dictionary and produce a list of dictionary keys
#that will be used to access the relevant Genre objects
def match_to_genre(word):
    word_but_lower = word.lower()
    possible_genres = []
    for key in genre_object_dict.keys():
        if word_but_lower in key.lower():
            possible_genres.append(key)
    return possible_genres

#the function will be used as what makes the program persist using recursion to repeat the program in case the 
#user-input does not match.
def find_genre_using_input():
    user_input = input("so tell me, what genre of games would you like to see? (One word please!): ")
    if " " in user_input:
        user_input = "".join(user_input.split())
    possible_genres = match_to_genre(user_input)
    if len(possible_genres) == 0:
        print("Looks like nothing matched. Let's try again.")
        find_genre_using_input()
    print("Here is what matches with your input: ")
    for i in range(len(possible_genres)):
        print(f"{i + 1}: {possible_genres[i]}")
    selection = input("Please enter the number that matches the genre you would like to see: ")
    selected_genre = possible_genres[int(selection) - 1]
    print(genre_object_dict[selected_genre].get_genre_and_titles())

find_genre_using_input()
        
    
    
    
    
