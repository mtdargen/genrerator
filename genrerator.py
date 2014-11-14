__author__ = "Matt Dargen, PHD"
__PHD__ = "Punk Hardcore Drugdealer"

import random

def main():

    print("____-=/GENRERATOR\=-____")
    while(True):
        try:
            input("press ENTER to Genrerate\n")
        except:
            print(genrerate())


def genrerate():
    r = random.Random()
    message = r.choice(messages)

    if "#" in message:
        message = message.replace("#",r.choice(artists))

    message = message.replace("@", genrerateHelper(0,r))
    message = message.replace("$", genrerateHelper(0,r))

    return message + '\n'

def genrerateHelper(calls, r):
    genre = "\033[4m"

    if(calls == 0):
        type = r.choice([1,2])
    else:
        type = r.choice([1,2,3])

    if type == 1:
        genre += newRandItem(1,r) + genrerateHelper(calls + 1, r)
    elif type == 2:
        genre += newRandItem(2,r) + newRandItem(3,r)
    else:
        genre += newRandItem(2,r)
    return genre + "\033[0m"

def newRandItem(state, r):
    if state == 1:
        return r.choice(adj)
    elif state == 2:
        return r.choice(noun)
    elif state == 3:
        return r.choice(suffixes)

adj = ["Post-","Dream ","Blues ","Electro-",
            "Psyche-","Hard ","Harsh ","Soft ",
            "Progressive ","Acid ","Chill ","Synth ","Space ","Indie ",
            "Horror ","Thrash ","Industrial ","Glam ","Jangle ","Art ",
            "Pop-","Death ","Twee ","Math ","Surf ","Slacker ",
            "Gypsy ","Neo-","Melodic ","Stoner ","Jazz-","G-","Political ",
            "Gloom ","Witch ","Nu-","Shred ","Trill ","Sea ","Afro-",
            "Nerd ","Christian ","Freak ","Ambient ","Experimental ","Hardcore ",
            "Urban ","Adult ","Bro ","Alt-","Psycho-","Vapor "]

noun = ["Noise","LoFi","Blues","Rock","Country","Collage","Doom","Trip",
            "Rap","Dub","House","Crunk","IDM","Techno","Bass","Motown","Crust",
            "Prog","Disco","Hardcore","Reggae","Punk","Metal","Folk","Beats",
            "Garage","Shoegaze","Pop","Grunge","Jazz","Funk","Hip Hop","Grime","Hyphy"]

suffixes = ["core","tronica","wave","abilly","step","style","-bop","-hop"]

messages = ["Pitchfork will not shut up about @",
            "Dude, I've been listening to so much @ lately",
            "I found this rad blog about the @ scene in Atlanta",
            "\m/ @ TIL I DIE \m/",
            "Nothing will help me understand @ music.",
            "God, my brother is one of those @ people now...",
            "@ is the future of music",
            "@ doesn't have a Wikipedia page yet, you know that shit is the real underground.",
            "You haven't lived until you've moshed to some @.",
            "If you don't like @, then you can get the fuck out.",
            "@ music changed my life.",
            "If you like @ then you would LOVE $",
            "@ is the new $.",
            "All I did in college was smoke weed and listen to @",
            "I'm starting a @ band with this guy I met on craigslist",
            "Kids these days with their @ garbage... what happened to good old $?!",
            "I'm so tired of the media labeling everything as @ these days",
            "# just released a @ album out of nowhere!  What?!!",
            "#'s new album kinda sounds like @, but with $ undertones, if that makes any sense.",
            "I can only listen to @ now.  Everything else bores me.",
            "The new # release experiments with @ quite a bit"]

artists = ["Klymaxxx","Huey Lewis & The News","Hall & Oates","George Michael",
            "Tupac","Toto","Yngwie Malmsteen","Aaron Carter","Destiny's Child",
            "David Bowie","James Taylor","Bruce Springsteen","Engelbert Humperdink",
            "Metallica","Oprah","Cheap Trick","The Divinyls","Death Grips"]

main()
