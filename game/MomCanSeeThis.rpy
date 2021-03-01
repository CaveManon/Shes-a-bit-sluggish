label MomCanSeeThis:
play music "audio/ambientinationer_8000.ogg" volume 0.05 loop 
"Friday evening on a college campus."


"Feels like a setup for some kind of movie."


"If only my life could be one of the cool genres."


"She said she found something neat to watch and was pretty excited about it too."


"We plan on watching what she found and maybe ordering some takeout, and it’s not like I can go to my dorm."


"Friggin fumigation, man."


"S’not like the rats caused any serious damage."


"At least the professor loaned me the lecture hall while the dorms are being de-ratted."


"Poor rats."


"Still, got a place to chill, and a cutey to chill with."


"Man, this place looks different at night though. Almost surreal."


"Glancing at my watch, it’s about five minutes before she gets here."

"She’s always punctual with this kind of stuff."

"Even back in elementary school, she had perfect attendance."


"Time for one last check to make sure everything’s ready."


"Projector’s working, seats are properly cushioned, screen is in place."


"I can’t help but feel I’m forgetting something."


"Snacks maybe…?"


"I peek inside my wallet, just to make sure."


"... Just a quarter and a European quid."


"Oh who am I kidding, I’d be lucky to get one of those tiny bags of chips."


"I make a quick trip to the snack machines in the hall…"

"...and load up my bag with nearly all of its contents."


"Gotta love that exchange rate."


"Oh."


"As I make my way back I notice Dori by the door."

show poster:
  yalign 1.0 xalign 0.0
  linear 5.0 yalign 0.0

"It’s a scene I’m used to seeing."

scene 1a with dissolve

"Phone pressed to her head."


"Pacing back and forth."


"Near audible shouting from the phone."


"And her own distressed voice failing."


"Seems like she’s arguing with her roommate again."


D "-I already promised to hang out with someone else!"


D "..."


D "No, I don’t mean… Look, sorry…"


D "No, please don’t-! Ugh…"


D "... Yeah… Yeah…"


D "I’ll think about it."


D "Thanks."


"She pockets her phone and turns to finally see me."

scene 1b with dissolve
D "Oh crap. Sorry, Andrew."


D "You didn’t hear very much of that, right?"


A "Er… No?"


"Her shoulders relax and she lets out a sigh."


A "Was that anything important? Sounded serious."


D "Hah… no. Nothing serious."


menu: 
     "Ask what’s on her mind.":
        jump askMindSfw
     "Ask about the movie she brought.":
        jump askMovieSfw

label askMindSfw:

A "I’ve never seen you this tense… what are you not telling me?"

A "We’re friends, right?"


scene 1b2 with dissolve
D "Ugh, I don’t want to hear that line anymore today…"


D "Please, let’s just… drop the subject."


A "I don’t really appreciate-"


D "Andrew, I’m not talking about this with you."


"She lets out another sigh."

D "Sorry. Let’s just drop it."


A "... Okay."


D "I found this neat movie. Figured you’d like it."

jump firstQuestionConverganceSfw 

label askMovieSfw:

$ score += 1 

A "You said you found a cool movie, right?"

scene 1b1 with dissolve
D "Oh! Well, I was walking around the neighborhood when I saw Vella having a garage sale of some sort." #YIIK is a masterpeice

"Uh oh."

D "And she had this on for sale for only two dollars!"


"She yanks a small CD case from her bag and hands it to me."


"Escawhat-now?"


D "Yeah! I remembered you were really into this sort of thing, so I thought it would be a nice gesture!"


A "Wow, that’s real nice of you."


A "Let’s go ahead and pop it in."

#this should just go to the convergance point

label firstQuestionConverganceSfw:

#Convergance point

scene 2a with fade

"The classroom projector eats the disc and starts humming."


"I turn the lights down, make sure the volume is at a good level, and take my seat next to Dori on the makeshift couch."

D "It’s a bit cold, isn’t it Andrew?"


A "It’s like room temp-"


"Andrew then realized he is profoundly stupid."


A "Actually, it is a bit cold."


"I pull out the blanket Dori brought from under me and drape it over us."


"Dori leans into my shoulder."


"Her antennae things brush lightly against the side of my head."


"This setup is the stuff dreams are made of…"


"Hope the movie is good."

scene black with fade

"..."

scene 2a with fade

"Ninety minutes later, the credits emerge from the bottom of the screen."


D "Soo… what’d you think?"


"Her tone carries some sense of expectation."


"The movie, it uh…"


menu:
    "Give an honest review.":
     jump NostalgiaCriticSfw 
    "You watch movies for the experience.":
     jump HeDoesItForFunSfw



label NostalgiaCriticSfw:

scene 2b2

A "Let me find the words…"

scene 4a with dissolve
A "That was quite possibly the worst thing I’ve ever seen!"


A "This went in and out of my mind just like that, it felt like I had just taken a nap on a highway, and a car ran me over once every three seconds and I just woke up."


A "It feels like I drank 50 liters of pure ethanol and am experiencing the godmother of all hangovers."


A "I can’t remember anything from any of this, just the character design from the deepest darks of the deep-darks, and characters that have the same charm as someone crapping on sandpaper and rubbing it on your brand new sports car."  


A "The only thing I can vaguely remember is that a school girl got horny over wings and blood mechas, nothing else." 


A "What were they thinking?!"


A "I am tempted to watch it again, write an entire novel about how bad it is, and then toss myself down a flight of stairs so I can forget about it." 


A "This was the worst thing I’ve ever seen in my entire life."


D "..."


A "..."

"I bite my tongue and wait to see if Dori felt in any way similar about that disgrace of anime."


D "Well jeez. Tell me how you really feel, why don’t you?"


D "Thought it would have been fun, and I thought you were."


D "Why don’t you pick the movie next time, if your taste is so refined."


A "Er…"


A "Come on, you know I don’t mean it like that…"


D "..."


A "..."


D "..."


A "Alright, I’ll make it up to you. I brought some stuff for sandwiches along with all those snacks."


D "Mmmm… fine, I’ll forgive you."

jump FoodTalkSfw

label HeDoesItForFunSfw:

scene 2b1

$ score += 1

A "The art design was certainly unique."


"Left unsaid was the nightmare-inducing character designs."


"what was wrong with their faces. And their eyes."


"I repress the involuntary shudder."

D "I can see why you like this stuff."


A "Er… Yeah…"


D "I liked it!"


"I bite back my scream."


A "So, wanna go another round?"


D "..." #blushing


A "I mean…"


A "How bout some food? I got some snacks from the vending machine."


"I upend my backpack, spilling three-fourths of a vending machine worth of snacks before us."


D "Err… Is it all junk food?"


A "I prefer to call it bachelor meals."


D "*sigh* At least you bought stuff for sandwiches too."


"She reaches into the pile and pulls out some jars and tupperware."

#Convergance

label FoodTalkSfw:

scene 3a with dissolve

D "I saw this one recipe online I wanted to try, think it had mustard and pepperoni and…"


"I nod, hiding the fact that I’m trying to break the disk of god awful anime behind my back."


"This was worse than reddit’s recommended anime list."


"God, Dori’s first exposure to anime and it was that trash fire."


D "... Man, this is looking nice."


D "Today was sandwich day in the cafeteria too, right?"


D "Maaaan, can’t believe I missed sammich day."


A "You didn’t eat lunch today?"


"She hesitates."


D "Just had something to do, didn’t turn out so well."


A "Had to skip to catch up on work?"


D "I wish- no I don’t."


A "Heh."


"She scans the pile and plucks out the pickle jar."

scene 3b with dissolve

D "My roommate wanted me to plant some drugs or something on her ex’s locker."


A "Whoa."


D "Yeahhh… I mean, he probably deserved it? That’s what she told me anyways."


"A pause while she fights the jar."


"I’d place my money on the jar winning."


D "But I got caught by the campus police and we both got in trouble."


A "That’s… Insane, she made you do that?"


D "‘Made’ is a strong word, I figured she’d know better than me about it, but…"


D "That’s uh… what she’s mad at me about right now…"


A "..."


D "..."


D "...Uhh…"


"She hands the jar to me."


"Can you get this for me? Think I got it a bit loose."


A "Huh? Oh, sure."

menu:
    "Open jar.":
     jump openJarSfw
    "Loosen the lid for her.":
     jump loosenJarSfw

label openJarSfw: 

"With a simple twist I remove the lid from the jar of pickles."

scene 3c with dissolve

A "Ta-dah! One order of super vinegar-y pickles."


D "Thanks."


A "Got any more jars that’re stuck?"


D "No, that’s it."


A "You sure?"
scene 3c2 with dissolve

D "Yes Andrew, just that one jar."


A "Absolutely positive?"


D "YES!"

jump postPicklePickleSfw

label loosenJarSfw:

$ score += 1

"I pretend to exert an extreme amount of torque as I slowly twist the lid."


"I sigh in false surrender as I hand Dori back the partially opened jar."


A "Ugh, it’s on way too tight."


D "Really?"

scene 3c with dissolve

"Dori nearly spills all the pickles on her dress when the lid pops off in her hand."


D "Ah! I got it!"


A "Oh yeah. Looks like you didn’t need my help after all."


"She proudly starts forking pickles onto her increasingly chaotic sandwich."


D "Waaiit a second."


D "You could have just opened it."


A "Whaaat? I didn’t do anything, you saw."


A "That was all you."


"She tosses a pickle at my shirt."


D "You dork."


#convergance

label postPicklePickleSfw:

scene 3a with dissolve

"By now our meals are more or less finished and we dig in."


D "What’d you make?"


A "Plain old club sandwich."


A "Uhh… You?"


"We both glance at the glob between two bread pieces she’s made."


D "I dunno!"


D "It’s good though!"


"She holds it over, offering a bite."

A "I’ll take your word for it."


"We share our meal making small talk and sipping soft drinks for a while."


D "And I liked the part where they… Huh… what did happen around then…?"


A "... I don’t remember?"


D "... I don’t either… weird…"

play sound "audio/ringtone.ogg" volume 0.05 

"...?"


"Dori checks her phone, and her face goes a bit paler than usual."


D "I uhh… got to take this…"


A "Yeah, sure."


"She flashes an apologetic smile and steps away, putting the phone to her ear."

scene 1a with fade

"I try not to eavesdrop and focus on finishing my food."


"But I can hear the yelling through the speakers from here."


R "... Right now… make it up to…"


D "I told you, I’m with someone else right now!"


R "... so that’s how you… all this time…"


D "No- come on, I don’t…"


R "... need you… you know that barkeep right?..."


R "... just come along… be fine…"


D "You promised after last time I didn’t have to go anymore…"


R "..."


D "... Okay… Sorry, yeah…"


D "I’ll be there soon…"


"She hangs up and glumly approaches."

scene 1b2 with dissolve

D "Uhh… Hey, I…"


A "I heard."


A "Is it something serious?"


"Dori scoffs and glowers to the side."


D "Hardly…"


D "She wants me to be her ‘wing woman’ at some bar."


A "That doesn’t-"


D "I had to cover the bill last time."


D "And find a ride home by myself."


D "And she ruined one of my favorite dresses."


"Each word is punctuated with her stuffing something roughly into her backpack."


"Even some of the snacks."


A "Then don’t go."


"Dori pauses, her frown marring her pretty face."


A "Your roommate’s a colossal scamp, Dori."


A "She’s clearly put you through this before and probably isn’t going to stop soon."


A "So how about for once you put her through some."


A "Stay here."


A "With me."

#ending is figured here

if score == 0: #The Bad Ending

    $ file = open("Bad", "w+")
    
    "She pauses a moment, I can see the gears turning in her head."
    
    
    "Her slight scowl tells me none of them are good."
    
    
    D "Stay with you?"
    
    
    A "Uhhh… Yeah?"
    
    
    "She takes a deep breath, collecting her thoughts."
    
    
    D "Andrew. I’ve known you for a long time, but tonight has just been…"
    
    
    D "Ugh."
    
    
    A "..."
    
    
    D "Trying to insert yourself into my private life,"
    
    
    A "..."
    
    
    D "saying to my face you thought the movie I thought we’d have fun watching was terrible,"
    
    
    A "..."
    
    
    D "that ego of yours, you just {i}have{/i} to rub every advantage you have in?"
    
    
    A "..."
    
    
    D "And you seriously think I’d rather hang out here with {i}you{/i}?"
    
    
    A "I mean, look at your alternatives."
    
    
    D "..."
    
    scene b2
    play sound "audio/hubcap.ogg"
    "{i}*SMACK*{/i}"
    
    scene b3
    D "..."
    
    D "You’re no different than the guy my roommate used to go out with."
    
    
    D "Think I get her point of view a bit better now."
    
    
    "Her phone starts buzzing yet again. She picks up halfway into the second buzz."
    
    
    D "Yeah?"
    
    
    "There isn’t yelling coming through the other end this time."
    
    
    D "Yeah, I know… Sorry."
    
    
    D "You were right."
    
    
    D "I’ll be there soon, leaving now."
    
    
    D "... Yeah, I know… you were right, he wasn’t worth it."
    
    
    D "... Okay, I can pay again this time…"
    
    
    D "... Okay…"
    
    
    D "... Bye."
    
    
    "She grimaces at me one more time."
    
    scene b4 with dissolve
    "And with the loud slam of the door, she’s gone."
    stop music fadeout 3.0
    play music "audio/love_theme_simple.ogg" volume 0.08 loop
    scene background with dissolve
    "I touch the mark on my face she left."
    
    
    "Still stings."
    
    "Maybe the sluggish one after all... was me."
    
    "..."

    pause 3
    scene black with fade
    jump playAgainSfw

if score == 1 or score == 2: #The Neutral Ending
    $ file_object  = open("Neutral", "w+")
    
    "She pauses in the middle of packing her bag."
    scene n1 with dissolve
    
    D "... I… I dunno…"
    
    
    D "I… Do want to stay a while longer, but…"
    
    
    D "I promised my roommate to go with her tonight…"
    
    
    D "..."
    
    
    A "I thought you didn’t like doing that stuff with her?"
    
    
    D "I don’t…"
    
    
    A "Why not tell her that?"
    
    
    "She considers it for a moment."
    
    
    D "Never really thought to, I guess."
    
    
    "Maybe now’s the best chance to-"
    
    
    A "Hey, Dori-"
    
    
    "Her phone again."
    
    
    "She hesitantly answers."
    
    
    "There’s no yelling coming through, so I can’t hear the other end."
    
    
    D "Yes?"
    
    
    D "... I already said I was coming."
    
    
    "She glances at me."
    
    
    D "Actually…"
    
    
    D "I wanted to talk about some stuff."
    
    
    D "... Yeah. Okay."
    
    
    D "See you."
    
    scene n2 with dissolve

    "She puts her phone away and starts backing away to the door."
    
    
    A "..."
    
    
    D "Thanks for the advice, Andrew!"
    
    
    D "I’ll go talk with her about it."
    
    
    D "Sorry about having to leave early, maybe next time?"
    
    
    A "Wait, Dori, I wanted to-"
    
    
    D "Next time, Andrew, I promise."
    
    
    D "You should pick the movie too."
    
    
    D "This was fun but I really need to be going."
    
    
    A "Dori I-"
    
    
    D "Later Andrew!"
    
    
    "The door already shut."
    scene background with dissolve
    
    "Looks like I blew it. Me and my big mouth."
    
    
    "Things were looking so well too."
    
    
    "But..."
    
    
    "Dori said next time."
    
    
    "Next time for sure."
    
    
    "I’ll really tell her how I feel."
    
    
    "And also pick something actually worth watching."
    
    
    "But I’ll tell her for sure."
    
    
    "..."
    scene black with fade 
    pause 3
    
    jump playAgainSfw

if score == 3: #The Good Ending
    stop music fadeout 2.0
    play music "audio/love_theme_simple.ogg" volume 0.05 loop
    $ file_object  = open("Good", "w+")
    
    scene g1 with dissolve
    
    "It’s fun watching her blush."
    
    "As her cheeks warm they become a soft pinkish purple."
    
    D "S-stay with you?"
    
    "I nod."
    
    scene g2 with dissolve
    
    "My fingers wrap gently around her hand, lowering it and her backpack back onto the floor."
    
    
    A "Yeah."
    
    
    A "Stay with me."
    scene g3 with dissolve
    
    D "Andrew…"
    
    
    "Her fingers intermingle with mine, the feeling of our palms pressing together sending goosebumps up my arms."
    
    
    D "I uh… is this..?"
    
    
    "I simply smile and nod again."
    
    
    "Her face is now near completely pinkish purple."
    
    
    "Magenta?"
    
    
    "Lavender maybe."
    
    
    "Her eyes dart all over the room as she sputters an inconceivable mess."
    
    
    "Even to the phone that’s buzzing loudly on her chair."
    
    D "I uh, that is… I mean… bwah?"
    
    
    "I have to fight back my snickers."
    
    
    "Everything about her is too cute."
    
    
    "Even her overreactions."
    
    
    "I lost against the snickers."
    
    scene g4 with dissolve
    
    "Which gets a new reaction out of Dori."
    
    
    D "Andrew!"
    
    "She has the sweetest pout on her lilac(maybe?) face."
    
    
    "Her free hand starts slapping at my chest."
    
    
    A "*Pfffft* ahahahaha I’m sorry I’m sorry."
    
    
    "Finally her slapping stops."
    
    scene g5 with dissolve
    "She buries her face against my chest, hiding it from view and muffling her voice."
    
    
    D "S’not funneh."
    
    
    A "Was kind of funny."
    
    
    D "S’not."
    
    scene g6 with dissolve
    "Her face is so close when she looks up."
    
    
    A "Dori…"
    
    
    "Her eyes shimmer and her voice is a tiny whimper."
    
    
    D "I’ll stay."
    
    "It feels like the world is muted."
    
    
    "Her head is slowly moving closer."
    
    
    "Her eyes begin to close."
    scene g7 with dissolve
    
    #(Dori struggling to kiss Andrew CG)
    #(Andrew leaning down to meet her halfway CG)
    #(Fanservice-Andrew lifting Dori up by her thigh and kissing CG)
    
    
    "..."
    scene g8 with dissolve
    pause 3
    scene black with fade
    
    if os.path.isfile('Bad') and os.path.isfile('Neutral') and os.path.isfile('Good'): #The Secret Ending
          "We spent the rest of that evening together in that lecture hall."
          
          
          "Dori’s roommate had been furious."
          
          
          "Something about messing up her bar rhythm, I don’t know."
          
          
          "Regardless, Dori and her aren’t roommates anymore."
          
          
          "Good riddance if you ask me."
          
          
          "Looking back, why were they ever roommates in the first place?"
          
          
          "As for me…"
          
          
          D "Andrew? You home?"
          
          
          A "Yep, just finished getting things set up."
          
          
          "Turns out the rats did in fact hurt someone."
          
          
          "Lots of someones."
          
          
          "With the dorm condemned I had to find a place to stay."
          
          
          "And Dori needed help paying her rent."
          
          
          "I’d say things turned out for the best."
          
          
          "The tiny projector starts playing a low quality dvdrip on the white curtain."
          
          
          "Dori takes her favorite seat in our apartment."
          
          scene lyingdown with fade
          
          "My lap."
          
          
          "We cuddle up as we enjoy another movie experience."
          
          "..."
          pause 3
          scene black with fade
          jump playAgainSfw
    else:

          pause 3
          jump playAgainSfw


label playAgainSfw:
menu:
   "would you like to play again?"
   "I do not want to play again":
     "Thank you for your time!"
     $ renpy.quit()

   "I would like to play again":
     jump start

