__author__ = "Matt Dargen, PHD"
__PHD__ = "Punk Hardcore Drugdealer"

import random

adj = ["Post-","Dream ","Blues ","Electro-",
            "Psych-","Elevator ","Hard ","Harsh ",
            "Progressive ","Acid ","Chill ","Synth ","Space ","Indie ",
            "Horror ","Thrash ","Industrial ","Glam ",
            "Pop-","Death ","Twee ","Math ","Surf ",
            "Gypsy ","Neo-","Melodic ","Stoner ","Jazz-","G-","Political ",
            "Gloom ","Witch ","Nu-","Shred ",
            "Nerd ","Christian ","Freak ","Ambient ","Experimental ","Hardcore ",
            "Urban ","Adult ","Bro ","Alt-","Psycho-"]

noun = ["Noise","LoFi","Blues","Rock","Country","Collage","Doom",
            "Rap","Dub","House","Crunk","IDM","Techno","Bass","Motown"
            "Prog","Disco","Hardcore","Reggae","Punk","Metal","Folk",
            "Garage","Shoegaze","Pop","Grunge","Jazz","Funk","Hip Hop","Grime","Hyphy"]

suffixes = ["core ","tronica ","wave ","abilly ","step ","-wop ","style "]


def main():

    for i in range(20):
        print(genrerate(0))


def genrerate(calls):
    r = random.Random()
    genre = ""

    if(calls == 0):
        type = r.choice([1,2])
    else:
        type = r.choice([1,2,3])
    if type == 1:
        genre += newRandItem(1,r) + genrerate(calls + 1)
    elif type == 2:
        genre += newRandItem(2,r) + newRandItem(3,r)
    else:
        genre += newRandItem(2,r)
    return genre

def newRandItem(state, r):
    if state == 1:
        return r.choice(adj)
    elif state == 2:
        return r.choice(noun)
    elif state == 3:
        return r.choice(suffixes)



main()
