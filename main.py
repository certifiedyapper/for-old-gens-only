#Hi and welcom to the git-translator
memes = {
    "cringe": "something unfunny and stupid ",
    "lil bro": "mostly used as an offense to call someone younger than you",
    "bro": " short for brother but used for a friend / best friend",
    "alr bud": "used to signify that ur mad",
    "meme":"trendy joke",
    "omg":"short for oh my god used to show madness , sadness and other kind of emotions",   
    "real":"something u agree on",
    "NAHH":"something u didnt expect",
    "pov":"short for point of view",
    "skibidi":"something cool / skibidi toilet"
}
print("list of available wwrods : cringe,lil bro, bro, alr bud, mem , omg")
meme = input ("what word to translate?")
if meme in memes:
    print("translation:",memes[meme])
else:
    print("it aint there bud")
