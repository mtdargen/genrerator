__author__ = "Matt Dargen"

import random

def main():

    print("___-=/GENRERATOR\=-___")
    print("   by matt dargen ;)\n")
    print("Press ENTER to Genrerate!\n")
    while(True):
        raw_input()
        print(genrerate())


def genrerate():
    r = random.Random()
    message = r.choice(messages)


    message = message.replace("@", genrerateHelper(0,r))

    if "$" in message:
        message = message.replace("$", genrerateHelper(0,r))
    if "#" in message:
        message = message.replace("#",r.choice(artists))
    if "*" in message:
        message = message.replace("*",r.choice(places))

    return message

def genrerateHelper(calls, r):
    genre = "\033[4m"

    if(calls == 0):
        type = r.choice([1,2])
    elif(calls == 3):
        type = r.choice([2,3])
    else:
        type = r.choice([1,2,3])

    if type == 1:
        genre += newRandItem(1,r) + genrerateHelper(calls + 1, r)
    elif type == 2:
        genre += newRandItem(1,r) + newRandItem(2,r)
    elif type == 3:
        genre += newRandItem(2,r) + newRandItem(3,r)
    return genre + "\033[0m"

def newRandItem(state, r):
    if state == 1:
        return r.choice(adj)
    elif state == 2:
        return r.choice(noun)
    elif state == 3:
        return r.choice(suffixes)

adj = ["Post-","Dream ","Blues ","Electro-","Bossa ","Pseudo-",
            "Psyche-","Hard ","Harsh ","Soft ","Euro-","New ","Cerebral ",
            "Progressive ","Acid ","Chill ","Synth ","Space ","Indie ",
            "Horror ","Thrash ","Industrial ","Glam ","Jangle ","Art ",
            "Pop-","Death ","Twee ","Math ","Surf ","Slacker ","Wizard ",
            "Gypsy ","Neo-","Melodic ","Stoner ","Jazz-","G-","Political ",
            "Gloom ","Witch ","Nu-","Shred ","Trill ","Sea ","Afro-","Based ",
            "Nerd ","Christian ","Freak ","Ambient ","Hardcore ","Traditional ",
            "Urban ","Adult ","Bro ","Alt-","Psycho-","Vapor ","Digital ","Old-School "]

noun = ["Noise","Blues","Rock","Country","Collage","Doom","Trip","Zydeco",
            "Bongo","Rap","Dub","House","Crunk","IDM","Techno","Bass","Motown",
            "Crust","Bleep-Bloop","Prog","Disco","Hardcore","Reggae","Punk","Metal",
            "Folk","Gospel","Banger","Garage","Shoegaze","Pop","Grunge","Worship",
            "Jazz","Funk","Hip Hop","Grime","Hyphy","Classical"]

suffixes = ["core","tronica","wave","abilly","step","style","-bop","-hop",
            " Beats","-Fi"]

messages = ["Pitchfork will not shut up about @",
            "Dude, I've been listening to so much @ lately",
            "I found this rad blog about the @ scene in *",
            "Have you heard of @?  It's blowing up in * right now.",
            "I wanna move to * so I can be close to all the @ music.",
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
            "The new # release experiments with @ quite a bit",
            "Hipster Runoff keeps talking about @ and I can't tell if it's a joke",
            "My friends are all into @ but personally I'm more of a $ type",
            "My parents say that @ is the will of Satan.",
            "Just found a bunch of @ in my parents' record collection??",
            "Most people think of # as the originator of @ music.",
            "I can't believe you can hear @ in commercials now... it's officially mainstream :(",
            "I like @ music but I HATE the fans.",
            "It's so disrespectful how Miley Cyrus is appropriating @ music.",
            "I like to put a lot of @ in the mix when I do public radio.",
            "We don't have a name yet, but we know we wanna make some @ kinda music.",
            "@ is too challenging for most listeners, I'd suggest starting out with $ and working from there.",
            "Gonna watch this @ band at a house show tonight, wanna come?  It's BYOB.  Also sober.",
            "@ is destroying music and corrupting the youth!",
            "How the fuck did # get booked at a @ festival?",
            "People will remember the 2010's for its @ music.",
            "Keep your #, I wanna listen to some @!",
            "I live in * and there's nowhere to see a good @ show :(",
            "Me and 13 other people like @ on Facebook."]

artists = ["Klymaxxx","Huey Lewis & The News","Hall & Oates","George Michael",
            "Tupac","Toto","Yngwie Malmsteen","Aaron Carter","Destiny's Child",
            "James Taylor","Bruce Springsteen","Engelbert Humperdink",
            "Metallica","Oprah","Cheap Trick","The Divinyls","Death Grips"]

places = ["Spokane","Atlanta","Toronto","New York","LA","Ethiopia","London","Sacto",
            "Ukraine","Athens","Vancouver","Philly","Seattle","Brazil","Appalachia",
            "Montreal","Berlin","Detroit"]

main()
