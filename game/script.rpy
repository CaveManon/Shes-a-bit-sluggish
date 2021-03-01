
define D = Character("Dori")  #tfw slug gf
define A = Character("Andrew") #Robofrengot
define R = Character("Dori's Roommate") #not waifu material

image black = "#000"

# The game starts here.

init python:
      from random import *
      import os

label splashscreen:

  $ splashtype = randint(1,30)
if splashtype == 30:
  $ renpy.movie_cutscene("images/went on the internet and found this.webm")
  play sound "audio/bongos.ogg"
  $ renpy.movie_cutscene("images/CaveManonProductions.webm")
  stop sound
  jump start
elif splashtype == 1:
  if os.path.exists("game/images/commercial.webm"):
    $ renpy.movie_cutscene("commercial.webm")
    $ os.remove("game/images/commercial.webm")
    "no one will believe you"
    $ renpy.quit()
  else:
    play sound "audio/bongos.ogg"
    $ renpy.movie_cutscene("images/CaveManonProductions.webm")
    stop sound
    jump start
else:
  #literally got a writefren to slap some fucking bongos for this one
  play sound "audio/bongos.ogg"
  $ renpy.movie_cutscene("images/CaveManonProductions.webm")
  stop sound
  jump start



label start:
$ score = 0
#some of us are so proud of this that we want to show it to mom and mom doesnt like swear words :))
menu:
   "The script contains swearing and other family unfriendly images, would you be okay with seeing that?"  
   "no thank you":
     "No Swearing Activated..."
     scene black with fade
     jump MomCanSeeThis

   "yeah":
     "Swearing Activated..."
     scene black with fade
     jump Normal


