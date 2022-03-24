# I need classes for both titles and graphs. A title object needs to point to
#it's relevant genres and it needs to possess its own name. A genre object
#would need to point to their relevant title objects, add a title object, and print
#out its own name and their relevant titles. I think doing this properly is gonna need a 
#dictionary of titles with their genres as keys, so maybe it isn't necessary to make titles
#point to other titles if theyre going to be on the list
#but whats getting to me is that there must only be one title and one genre. THe only things that
#should be in multiples are the connections e.g. its a graph. But that means that genre objects cannot just
#make a new title if that title maybe exists.
class Titles:
    #instance properties/attributes i forgot the names
    def __init__(self, title, genres=None):
        self.genres = genres
        self.title = title
    #for if i want to print out everything about the title
    def __repr__(self):
        print(f"{self.title}\nGenre: {self.genres}")
    #just makes getting the title itself easier.
    def get_title(self):
        return self.title
    #to be used with Genres.add_title()
    def add_genre(self, genre_string):
        self.genres += [genre_string]

class Genres:
    #you know im pretty sure theyre called instance properties
    def __init__(self, genre, titles=None):
        self.genre = genre
        self.titles = titles
    #easy way to get the titles edge list
    def __repr__(self):
        print(f"The titles associated with the Genre {self.genre}: {self.titles}")
    #oof. Was gonna make a new object but that will make things messy
    def add_title(self, title_object):
        for elem in self.titles:
            if elem == title_object:
                print(f"{title_object.get_title()} is already under {self.genre}")
                return
        self.titles += [title_object]
        title_object.add_genre(self.genre)

#use the premade list of titles and make all of the genre objects
horror = Genres("Horror")
action = Genres("Action")
adventure = Genres("Adventure")
soulslike = Genres("Souls-Like")
platformer = Genres("Platformer")
metroidvania = Genres("Metroidvania")
hacknslash = Genres("Hack N' Slash")
rpg = Genres("RPG")
rougelite = Genres("Rouge-Lite")
mystery = Genres("Mystery")
fantasy = Genres("Fantasy")
crpg = Genres("CRPG")
jrpg = Genres("JRPG")
tactical = Genres("Tactical")
postapoc = Genres("Post-Apocalyptic")
shooter = Genres("Shooter")

#use that same list to make the title objects jesus that was a lot of work
title_genre_dict = {
    "Alien: Isolation": ["Horror"],
    "Amnesia: Rebirth": ["Horror", "Adventure"],
    "A Plague Tale: Innocence": ["Adventure", "Action"],
    "Ashen": ["Action", "Adventure", "Souls-like"],
    "Axiom Verge": ["Platformer", "Metroidvania"],
    "Axiom Verge 2": ["Platformer", "Metroidvania"],
    "Bayonetta": ["Action", "Hack 'N Slash"],
    "Bayonetta 2": ["Action", "Hack 'N Slash"],
    "Blasphemous": ["Platformer", "Metroidvania"],
    "Bloodstained: Ritual of the Night": ["Platformer", "Metroidvania"],
    "Celeste": ["Platformer"],
    "Children of Morta": ["Rouge-lite", "Action", "RPG"],
    "CrossCode": ["Action", "RPG", "Adventure"],
    "Danganronpa V3: Killing Harmony": ["Mystery"],
    "Dark Souls III": ["Action", "RPG", "Souls-like", "Fantasy"],
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
    "STAR WARS Jedi: Fallen Order": ["Action", "Adventure", "Souls-like"],
    "The Outer Worlds": ["Action", "RPG", "Shooter", "Adventure"],
    "UNSIGHTED": ["Action", "Adventure", "RPG", "Metroidvania", "Souls-like"],
    "Wasteland 2: Director's Cut": ["RPG", "Adventure", "CRPG", "Tactical" , "Post-Apocalyptic"]
}
#somehow make a for loop that takes every title's list of relevant genres to make an edge 
#between the title and the relevant genres, or make a function do it

#also set up a linked list that connects titles to each other as to prevent the need of making a list of titles.
#saves memory 

#now ask the user if they want to search through titles or by genre

#if statement for their choice and then ask for a few characters that hopefully match something in this program

#if title, set pointers at the head and tail node to hopefully speed up the search for a relevant title. Relevant 
#titles will be added to a list (the object themselves). The list is produced and I somehow need to proint out the
#string Titles and their Genre lists.

#its easier with Genres. I just use a bunch of if statements and do something similar with Titles like adding 
#relevant genres to a list and printing them out in the end, but I'll be printing out the edges too.

