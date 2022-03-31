# I need classes for both titles and graphs. A title object needs to point to
#it's relevant genres (not necessarily genre objects) and it needs to possess its own name. A genre object
#would need to point to their relevant title objects, add a title object, and print
#out its own name and their relevant titles. I think doing this properly is gonna need a 
#dictionary of titles with their genres as keys, so maybe it isn't necessary to make titles
#point to other titles if theyre going to be on the list
#but whats getting to me is that there must only be one title and one genre. THe only things that
#should be in multiples are the connections e.g. its a graph. But that means that genre objects cannot just
#make a new title if that title maybe exists.
class Titles:
    #instance properties/attributes i forgot the names
    def __init__(self, title, genres):
        self.title = title
        self.genres = genres
    #for if i want to print out everything about the title
    def get_title_and_genres(self):
        return "{0}\nGenre: {1}".format(self.title, self.genres)
    #just makes getting the title itself easier.
    def get_title(self):
        return self.title
    def get_genres(self):
        return self.genres
class Genres:
    #you know im pretty sure theyre called instance properties HOW DOES NOT GIVING TITLES A DEFAULT VALUE MAKE THE PROGRAM ACTUALLY WORK???????
    def __init__(self, genre):
        self.genre = genre
        self.titles = []
    
    #easy way to get the titles edge list
    def get_genre_and_titles(self):
        #for elem in self.titles:
            #if self.title_belongs_under_genre(elem) == False:
                #self.titles.remove(elem)
        readable_title_list = [elem.title for elem in self.titles]
        return f"The title(s) under {self.genre} are/is: {readable_title_list}"
    
    #to get titles and genre
    def get_titles(self):
        return [elem.title for elem in self.titles]
    def get_genre(self):
        return self.genre
    
    #lets add in 2 true/false methods
    def title_belongs_under_genre(self, title_object):
        title_genre_list = title_object.get_genres()
        return self.genre in title_genre_list
    def title_already_in_list(self, title_object):
        return title_object in self.titles
    
    #LMAO A DEFAULT [] FOR TITLES BROKE THE CLASS METHOD AND ANY CHANGES TO THAT INSTANCE PROPERTY WOULD REFLECT ON EVERY OBJECT OF THIS CLASS
    def add_title(self, title_object):
        title_string = title_object.get_title()
        #print(f"{self.genre}'s title list before method starts: {[elem.title for elem in self.titles]}")
        if self.title_belongs_under_genre(title_object) == False:
            #print(f"{title_string} does not belong under {self.genre}")
            return
        if self.title_already_in_list(title_object) == True:
            #print(f"{title_string} is already under {self.genre}")
            return
        if self.title_belongs_under_genre(title_object) == True and self.title_already_in_list(title_object) == False:
            #print(f"Adding {title_string} to {self.genre}")
            self.titles.append(title_object)
            return
#IT TOOK 2 DAYS TO FIND OUT I JUST NEEDED TO DELETE LIKE 8 CHARACTERS
    
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
#use that same list to make the title objects jesus that was a lot of work
title_object_dict = {
    "Alien: Isolation": ["Horror"],
    "Amnesia: Rebirth": ["Horror", "Adventure"],
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
#somehow make a for loop that takes every title's list of relevant genres to make an edge 
#between the title and the relevant genres, or make a function do it
for key, value in title_object_dict.items():
    title_object = Titles(key, value)
    title_object_dict[key] = title_object

#This function will iterate through the .genres list of title objects, use the returned strings to point to the correct genre object in the genre dictionary,
#and use Genre.add_title() to make an edge from the genre object to the title object.
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
Hello! I have here a bunch of games that I have completed. 
This program is nothing more than a way to play around with data structures and graphs; just another project.
Maybe this program will have some extra functionality in the future, but for now, I will allow traversal to find titles based on
user-inputs that are either genres or a few characters that relate to a genre.
''')

possible_match = input("so tell me, what genre of games would you like to see?: ")

#its easier with Genres. I just use a bunch of if statements and do something similar with Titles Like adding 
#relevant genres to a list and printing them out in the end, but I'll be printing out the edges too