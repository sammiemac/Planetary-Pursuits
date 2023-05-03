
# Pluto's first date, ice rink
label pluto_date1:

    scene bg black with dissolve

    play sound "audio/SFX_Transition_Scene.mp3" volume 0.2

    pause 2

    centered "{b}{color=#ffffff}A few days later, around noon...{/b}{/color}"

    show bg isaac ext with dissolve

    play music "audio/SFX_Birds_1.mp3" volume 0.1

    "After a few days to give Pluto time to settle in, I got ready for our scheduled date per our agreement. Naturally, Theo as my secretary also acted as the designated escort and driver, as embarrassing as it was to be chauffeured to my date."

    "Theo waited in the car while I went to knock on Pluto’s door. From the other side, muffled panic and rummaging could be heard until finally an out-of-breath Pluto answered the door."

    show pluto neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    menu:
        "Compliment her dress.":

            mc "You look really nice in that dress, Pluto."

            show pluto shy with Dissolve(0.2)

            pluto "You don't need to lie, I know it doesn't suit me..."

            mc "No, it's true! It's something only you could pull off."

            show pluto neutral with Dissolve(0.2)

            $ renpy.notify("Pluto liked your compliment.")
            
            pluto "O-oh, thanks..."

            $ dress_complement = True

            $ pluto_aff += 1

        "Stay quiet.":

            "Deciding not to come off strong and seeing Pluto in a vulnerable state, I choose to let the topic of her choice in dress slide and focus on the task at hand."

            show pluto flustered with Dissolve(0.2)

            "Pluto seems surprised to not be put down for her choice in fashion."

            $ dress_complement = False

        "Make a joke.":

            mc "Wow, we’re going ice skating, not to a ball!"

            show pluto flustered with Dissolve(0.2)

            "Just as I finish, Pluto is visibly devastated. A mixture of sadness and confusion on her face."

            show pluto shy with Dissolve(0.2)

            $ renpy.notify("Pluto looks uncomfortable.")

            pluto "I-I'm sorry, I'm not too familiar with Earth's customs yet, figures I'd mess up already."

            mc "Actually, I was just making a joke... I didn't mean to offend you."

            pluto "No, you're right, this dress doesn't look good on me in the first place. I don't know what I was thinking..."

            "{i}Well that was terrible, way to go me...{/i}"

            $ dress_complement = False

            $ pluto_aff -= 1

    "I escorted Pluto over to Theo's car, and then my trusted secretary began driving us off to our \"date.\""

    scene bg black with dissolve

    play sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    queue sound "audio/SFX_Drive_Away_1.mp3" volume 0.1

    pause 2
    
    scene bg theo sedan with dissolve

    play music "audio/OST_Mr_Secretary_You_Have_A_Call.mp3" fadein 0.5 volume 0.1

    "A normal job usually has people deal with customers, selling and buying, working with computers or machines, and mine... has me going on a date with a celestial body."

    "{i}Sigh...{/i}"

    "Pluto hasn't said anything since we got into the car, and she made sure to keep more than a seat's worth of distance between us. I can't tell whether she's just that engrossed with the scenery outside the window, or if she really doesn't want to talk to me."

    menu:
        "Speak up.":

            mc "Do you, um, like... nature?"

            show pluto shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "Y-yeah."

            hide pluto with dissolve

            "Theo gives me a mocking glance from the rearview mirror at my terrible attempt at conversation."

        "Stay quiet.":
            pass
    
    "Defeated, I likewise resort to staring out the window."

    scene bg black with dissolve

    play sound "audio/SFX_Drive_Away_1_Cut.mp3" volume 0.1

    queue sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    pause 2

    scene bg ice rink ext with fade:
        xalign 0.5
        zoom 0.16

    "As soon as we step out of the car, Pluto immediately hides behind my shoulder, keeping her arms and hands close together in a self-hug, hiding from everyone as they walk past."

    "{i}She probably doesn’t like crowds too much.{/i}"

    show pluto shy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    mc "It’s a weekday, so there shouldn’t be too many people."
    
    show pluto pose think with Dissolve(0.2)

    "Pluto doesn’t respond, but she seems to ease up if only by a little."

    hide pluto with dissolve

    "The lobby is primarily filled with couples, barely any families who are likely on vacation, and what looks to be professionals since they have their own personal pair of skates brandished with sponsorships."
    
    "Despite this, there are hardly any people, most of which are leaving and those who aren’t are still strapping on their skates."

    "Pluto’s eyes dart around the room at every sound with a sense of disillusionment and a hint of curiosity. But at the sight of the affirmed small number of people, she relaxes most of the tension in her body, still maintaining some air of nervousness."

    "I guide us both to the counter, where an employee greets us."

    "Employee" "Hello! Just the two of you I take it? How long would you like to stay?"

    mc "Um..."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "I glance at Pluto to gauge her preference, and she looks at me with a clueless gaze."

    hide pluto with dissolve

    mc "Just an hour."

    "Employee" "Great!"

    "They give us each a ticket which states the time frame that we’re allowed onto the rink, then they hand us our skates."

    "Employee" "Enjoy! Oh, by the way, I really like your dress! It’s very cute."

    if dress_complement:

        show pluto joy with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.60

        $ renpy.notify("Pluto seems happy with the compliment.")
        
        pluto "T-thank you."
    
    else:

        show pluto flustered with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.60
        
        $ renpy.notify("Pluto seems embarassed about the compliment.")

        pluto "O-oh, thanks."
    
    scene bg ice rink int with fade

    "We sit on one of the nearby benches to tie on our skates. Pluto watches me put them on, then tries to replicate the action herself, albeit much slower."
    
    "For a solid three minutes, she struggles to tie a knot with the shoelaces and is clearly getting to the point of being both embarrassed and defeated."

    "Unable to observe her self-torture any longer, I bend over to help her."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "N-no you don’t have to, i-it’s alright."

    show pluto shy with Dissolve(0.2)

    pluto "I know I’m a burden..."

    mc "Don’t say that. I used to tie my best friend’s shoes up until middle school, so don’t worry about it!"

    "I give her a reassuring smile, but I can’t tell if it helps or not."

    mc "It might be a little hard for you to walk in them, so if you want you can hold onto me until you get used to it."

    pluto "N-no it’s okay. I don’t want to slow you down."

    "She keeps her eyes to the floor with a tight lip. Still a bit worried, I make sure to glance at her every now and then as we make our way to the ice rink."

    stop music fadeout 2

    scene bg ice rink with dissolve:
        xalign 0.5
        yalign 1.0
        zoom 1.2

    play music "audio/OST_A_Thawing_Heart.mp3" fadein 0.5 volume 0.1

    $ renpy.sound.play("audio/SFX_ice_skate_ambience.wav", loop=True, fadein=0.5, relative_volume=0.2)

    "An instant gush of frigid air hits us as soon as we enter and I pull my coat closer."

    "{i}I haven't been to an ice rink since I was a kid, were they always this cold?{/i}"

    "Expecting Pluto to be equally freezing and discomforted, I braced myself for her visual pain as a sign that I've messed up once again."

    show pluto joy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "To my surprise, it's actually the opposite. She seems... happy? At least judging by the slight twinkle in her eye."

    "For now though, I decide not to make a comment on it."

    hide pluto with dissolve

    "With wobbled newborn fawn legs, I guide Pluto and myself to the perimeter of the rink for support. The once twinkle she had immediately fades in turn for muffled panic as she struggles to even stand on the ice."

    "On the other hand, I get the hang of at least standing before she can, which evidently disheartens her as her face grows darker as she watches others skate past with ease."

    menu:
        "Offer encouragement.":

            mc "I know you can do it, just try not to overthink it too much. Imagine you’re just wearing heels."

        "Make a light hearted joke.":

            mc "Don’t worry about everyone else, they probably come here every day of the week!"
    
    "Silently heeding my words, Pluto steadily stands straight and manages to keep her balance more adeptly, despite having a slight sway every now and then."

    show pluto neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "T-thank you. N-now what?"

    mc "When you walk, kind of push your feet back on the ice."

    show pluto flustered with Dissolve(0.2)

    "As soon as she attempts to move, she starts to lose balance and thus desperately grabs the railing."

    mc "Just small steps are fine!"

    "After an extended pause to regain her footing, she tries again and has the same result"

    "Once again, her eyes focus on the others around us. The only ones who seem to be struggling are children more than half our age... and us."

    show pluto cry with Dissolve(0.2)

    "Pluto purses her lips and grows visibly more distressed the more she stares, especially at those who are proficient enough to do flips while we can’t even manage to walk."

    hide pluto with dissolve

    "Just as I debate giving her a further boost in confidence, a teenage couple bumps into me and thus Pluto, who falls onto her knees from the impact."

    "The teens, on the other hand, don’t even turn around to apologize. Instead, they whisper and laugh to each other as they go by."

    "I glare in their direction, but then see Pluto in my peripherals struggling to get back up after she fought so hard to figure out how to stand in the first place."

    mc "Crap--!"

    mc "I’m so sorry! They didn’t even try to help us."

    menu:
        "Let her get up on her own.":

            "Pluto surprisingly manages to stand back up without much trouble."

            show pluto neutral with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "It’s alright..."

            $ help_up = False

        "Try to lighten the mood.":

            mc "The ice is slippery huh?"

            show pluto shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            $ renpy.notify("Pluto seems upset.")

            pluto "..."

            "{i}I just made it worse.{/i}"

            "Pluto manages to stand back up without much trouble."

            $ pluto_aff -= 1

            $ help_up = False

        "Help her up.":

            "I try to help her stand but end up slipping myself."

            show pluto joy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "Hehe."

            "{i}Was that a laugh just now?{/i}"

            mc "That’s embarrassing... Now I’m even more sorry for you being stuck with me."

            show pluto neutral with Dissolve(0.2)

            $ renpy.notify("Pluto feels a lot better.")

            pluto "It’s alright, I could say the same about myself."

            mc "Well, now we’re both on the ground so I guess we’re equal now."

            show pluto joy with Dissolve(0.2)

            "Still smiling to ourselves, we slowly get back on our feet."

            $ pluto_aff += 1

            $ help_up = True

        "Help her up and dust her off.":

            "I lift her by her arm in an attempt to help, then try to dust off her dress for her. The moment I reach down, she backs off and makes distance between us."

            show pluto stern with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            $ renpy.notify("Pluto seems uncomfortable.")

            pluto "I-I’m alright..."

            "{i}I just made it worse.{/i}"

            $ pluto_aff -= 1

            $ help_up = False

    hide pluto with dissolve
    
    "I glance at the large digital clock displayed on the wall."

    "{i}Thirty minutes already? Geez. She looks burnt out though, maybe we should leave earlier.{/i}"

    if not help_up:

        "Awkwardly, I try to change the topic."

    else:

        "Feeling a little bit closer with Pluto and with newfound confidence, I come up with an idea."
    
    mc "Why don’t we go outside? There’s some stuff we can check out around the ice rink."

    show pluto neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "O-oh, sure."

    scene bg ice rink int with fade

    $ renpy.sound.stop(fadeout=1)

    "Well, that was an experience. Skating had left both Pluto and I more exhausted than we wanted to admit, a break was more than needed. Suddenly, a familiar noise began to fill the building; its source coming from the outside."

    menu:
        "Take Pluto and investigate the noise.":

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            "Without word or warning, I quickly grab Pluto’s hand and rush her to the exit. Pluto offers little resistance as we approach the doorway, seemingly caught off guard with my sudden actions and unable to process what is going on."

        "Ask Pluto if she wants to investigate the noise.":

            mc "Did you wanna see what's going on outside?"

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            $ renpy.notify("Pluto appreciates you asking.")

            pluto "O-oh! I’m not sure, but I am a bit curious..."

            show pluto neutral with Dissolve(0.2)

            "Pluto seemed a bit taken back by my question, but still eager in her own way."

            $ pluto_aff += 1
    
    stop music fadeout 2
    
    scene bg park bench with fade

    play music "audio/OST_Ice_Cream_Jingle.mp3" fadein 0.5 volume 0.05

    $ renpy.sound.play("audio/SFX_Crowd_Talking_Long.mp3", loop=True, fadein=0.5, relative_volume=0.2)

    "We exit the ice rink, the hot sun and warm air letting us know that the day isn’t over yet."

    mc "As expected, it’s an ice cream truck!"

    "Glancing at Pluto, I notice that she has a slight sparkle in her eyes as she looks around the area."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    pluto "There's so many people... there's kids, parents, and even..."

    pluto "{i}*gasp*{/i}"

    "I look over to see what has caused Pluto to be in a state of disarray, and I find the culprit."

    hide pluto with dissolve

    show dog with dissolve
    
    "A dog sitting near a bench, right across from the ice cream truck, with the owner weaning a pair of sunglasses and eating an ice cream sandwich."

    "The dog was a fluffy golden retriever, medium sized, tongue out as it attempted to cool itself off from the hot sun."

    hide dog with dissolve

    "Pluto's eyes were quickly shifting up from the floor, back to the dog, then back to the floor. She seemed to be interested in the dog, but was unsure of what to do. I give her a gentle tap on the shoulder to get her attention."

    mc "Hey, Pluto--"

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "Eeep!"

    show pluto pose think with Dissolve(0.2)

    pluto "Oh sorry, I was a bit distracted..."

    mc "You really like dogs, huh?"

    show pluto neutral with Dissolve(0.2)

    pluto "Oh, well, they are kind of nice, I guess."

    pluto "They are really friendly, and soft, and fluffy, and playful and people really like them and..."

    show pluto pose think with Dissolve(0.2)

    pluto "{i}sometimeswhenIseeadogIjustthinkitwouldbereallycooltopetthem--{/i}"

    mc "Woah woah, slow down!"

    show pluto flustered with Dissolve(0.2)

    pluto "Ah-- sorry, I did it again didn’t I?"

    show pluto pose think with Dissolve(0.2)

    pluto "Dogs are my favorite animals, sometimes I get carried away when talking about them. It really makes me wish I had my own..."

    mc "Don’t worry about it, everyone has something they are really passionate about, and I bet we could even help get you a dog."

    show pluto flustered with Dissolve(0.2)

    pluto "R-Really?!"

    mc "Sure! But first..."

    menu:
        "Encourage Pluto to go pet the dog.":

            mc "Why don’t you try and ask the owner if you can pet the dog?"

            show pluto shy with Dissolve(0.2)

            pluto "I-I’m not sure I could pull that off."

            mc "Don’t worry! Look, there are a group of kids petting the dog already, I’m sure the owner won’t mind."

            show pluto neutral with Dissolve(0.2)

            pluto "Alright, I’ll do it, if you think I can..."

            hide pluto with dissolve

            "Pluto proceeds to walk up to the owner with sunglasses, getting a bit nervous, but seemingly calming down once the dog looks at her and barks around her."

            show pluto shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            pluto "E-excuse me, w-would it be alright if I could maybe-- if you wouldn't m-mind--"

            "Owner" "Go ahead miss, you can pet him! No need to be shy, he loves the attention."

            show pluto flustered with Dissolve(0.2)

            "Pluto’s eyes light up as she reaches down to pet the excited dog."

            show pluto joy with Dissolve(0.2):
                linear 0.5 xalign 0.875

            show dog with dissolve:
                xalign 0.125
                yalign 1.0

            pluto "Hehe, what a good boy!"

            play sound "audio/SFX_Dog_2.mp3" volume 0.1

            "Dog" "Borf!"

            "The two share a close moment of friendship as Pluto has a big smile on her face, eventually standing back up, satisfied."

            hide dog with dissolve

            show pluto joy with Dissolve(0.2):
                linear 0.5 xalign 0.5
            
            $ renpy.notify("Pluto looks really happy.")

            pluto "That was nice, thank you."

            "Whether she was thanking me or the dog owner, I’m not sure."

            $ pluto_aff += 1

        "Ask the dog owner if Pluto can pet the dog.":

            mc "Why don’t I go and ask the owner if you can pet the dog?"

            show pluto shy with Dissolve(0.2)

            pluto "I-I wouldn’t want to bother you."

            mc "Don’t worry! Look, there are a group of kids petting the dog already, I’m sure the owner wouldn’t mind."

            show pluto neutral with Dissolve(0.2)

            pluto "Well, then, if you wouldn't mind..."

            hide pluto with dissolve

            "I walk up to the owner with sunglasses, who looks at me with a friendly face, the dog looking up at me while running in circles and barking."

            mc "Excuse me, would it be okay for my friend to pet your dog?"

            "Owner" "Sure, she can pet him! No need to be shy, my dog loves the attention."

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            "Pluto’s eyes light up as she hears the owner's response and comes over, reaching down to pet the excited dog."

            show pluto joy with Dissolve(0.2):
                linear 0.5 xalign 0.875

            show dog with dissolve:
                xalign 0.125
                yalign 1.0

            pluto "Hehe, what a good boy!"

            play sound "audio/SFX_Dog_2.mp3" volume 0.1

            "Dog" "Borf!"

            "The two share a close moment of friendship as Pluto has a big smile on her face, eventually standing back up, satisfied."

            hide dog with dissolve

            show pluto joy with Dissolve(0.2):
                linear 0.5 xalign 0.5

            $ renpy.notify("Pluto looks really happy.")

            pluto "That was nice, thank you."

            "Whether she was thanking me or the dog owner, I’m not sure."

            $ pluto_aff += 1
    
    hide pluto with dissolve
    
    "Suddenly, a rowdy group of children catches Pluto’s attention. They’re crowding around an ice cream wagon as they tug on their parents’ shins with desperate pleas."

    "Despite her clear curiosity, she glances around and tries to avoid eye contact with the vendor and myself in an attempt to gain the confidence to speak up."

    show pluto shy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "... How does ice cream taste?"

    mc "Huh?"

    pluto "I’ve never had it before... Is it really worth being that excited over?"

    "In a weird way, Pluto seems almost... jealous of them?"

    mc "For kids, yeah. It’s sort of like candy in the sense of sugary junk food, but more in the form of a cold dairy treat. It comes in all kinds of flavors and shapes."

    show pluto flustered with Dissolve(0.2)

    pluto "Really?"

    mc "Speaking of ice cream, did you want to try some?"

    show pluto joy with Dissolve(0.2)

    pluto "Sure."

    hide pluto with dissolve

    "It’s a hot day, getting some ice cream for the both of us would be nice, but..."

    "Choosing what ice cream to buy can be overwhelming for her with the amount of choices. I should probably..."

    menu:
        "Buy Pluto the dog-shaped ice cream.":

            show ice cream dog with dissolve:
                xalign 0.5
                yalign 0.375
                zoom 0.375

            "Since she seems to like dogs, I decide to buy her the dog shaped ice cream."

            hide ice cream dog with dissolve

            "I talk to the stern looking ice cream man and get two ice cream cones."

            mc "Here you go Pluto, one dog shaped ice cream, chocolate flavored."

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            "Pluto grabs the now melting ice cream and stares intently, at a loss for words."

            show pluto chopper with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 1.0

            pluto "NOOOO!!! I WILL NEVER COMMIT DOGICIDE!!!"

            "Pluto is in shambles and breaks down crying. I forgot that she still isn't used to Earth’s customs."

            "This draws the attention of everyone around us, making matters even worse. I attempt to comfort her and quickly grab the ice cream."

            mc "There there, it’s ok... It’s not actually a dog, see? No dogs were hurt in the making of this ice cream."

            show pluto cry with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "{i}*sniffle*{/i} R-really?"

            mc "Yeah, of course! So there’s no need to cry anymore, okay?"

            show pluto neutral with Dissolve(0.2)

            $ renpy.notify("Pluto is slightly traumatized.")

            pluto "A-alright, but I think I won't be eating any ice cream for a while."

            mc "Me neither..."

            $ pluto_aff -= 1

        "Buy Pluto the blue hedgehog ice cream with a smiley face and the gumball eyes.":

            show ice cream sonic with dissolve:
                xalign 0.5
                yalign 0.25
                zoom 0.25

            "The gumball-face ice cream is a classic, anyone would like this."

            hide ice cream sonic with dissolve

            "I talk to the stern looking ice cream man and get the blue hedgehog on a stick."

            mc "Here you go Pluto, one blueberry hedgehog ice cream with gumball eyes."

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            "Pluto grabs the now melting ice cream and stares intently, seeming a bit confused."

            show pluto neutral with Dissolve(0.2)

            pluto "Thank you... I didn’t know the animals on earth looked so funny."

            mc "What do you mean? It's just a normal-- Oh..."

            "It just dawned upon me that today is a very hot day, and the sun has melted the hedgehog into a funky looking slime with droopy gumball eyes."

            mc "Oh wow, I’m really sorry about that, I didn't realize it would melt so fast. Maybe I can get you a new one..."

            show pluto joy with Dissolve(0.2)

            pluto "Hehe! No, I like it."

            "Pluto licks the melting ice cream."

            show pluto flustered with Dissolve(0.2)

            $ renpy.notify("Pluto really liked the ice cream.")
            
            pluto "Wow, it's really good! I’m glad I got to try it."

            show pluto joy with Dissolve(0.2)

            mc "Hahaha! Ice cream never fails to make any day better."

            $ pluto_aff += 1

        "Buy Pluto a popsicle of her choice.":

            mc "Pluto, What's your favorite flavor?"

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "Oh, that’s an interesting question. There are so many, but if I had to choose... maybe strawberry?"

            mc "You got it!"

            hide pluto with dissolve

            "I talk to the stern looking ice cream man and ask for one strawberry popsicle."

            mc "Here you go Pluto, one strawberry popsicle."

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            "Pluto grabs the popsicle and stares intently, seeming a bit confused."

            pluto "Is ice cream supposed to be frozen solid like this?"

            mc "Actually, it’s a popsicle, so it's not quite an ice cream. But it tastes great all the same. You can think of it as the cousin to ice cream."

            mc "With a bit more confidence in her eyes, Pluto tastes the popsicle."

            show pluto joy with Dissolve(0.2)

            $ renpy.notify("Pluto really liked the popsicle.")

            pluto "Mmm, it's really good and tastes like strawberries! I’m glad I got to try it."

            mc "A good popsicle never fails to make the day better."

            $ pluto_aff += 1

        "Let Pluto order for herself.":

            mc "Hey Pluto, why don’t you try ordering an ice cream from the ice cream truck? They have all kinds of flavors from your basic vanilla to more berry themed ones."

            show pluto flustered with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            pluto "Oh, okay. I've never ordered an ice cream before, but I think I can do it."

            hide pluto with dissolve

            "Pluto goes up to the stern looking ice cream man and seems to tense up with her words being little louder than a whisper."

            show pluto shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "H-hi... I w-w-would like..."

            "Ice Cream Man" "Wha?! I can't hear you, speak  up! I don't got all day."

            show pluto cry

            pluto "A-ah! Sorry, I’ll... just take vanilla..."

            hide pluto with dissolve

            "Defeated, Pluto reluctantly takes the vanilla ice cream cone which was clearly not her first choice, but her default option nevertheless."

            "Pluto proceeds to taste her disappointing ice cream."

            show pluto neutral with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            pluto "Hmm, it's not bad... I would have preferred another flavor like strawberry, but I’ll take what I can get."

            mc "Yeah, ice cream is ice cream, no matter the flavor. I wouldn't worry about the details."

            pluto "Mhm, I think I feel better already. Ice cream really is an Earth specialty."

            show pluto shy with Dissolve(0.2)

            $ renpy.notify("Pluto is slightly embarrassed.")
            
            pluto "I don’t think I will try another one anytime soon, though..."

            mc "Fair enough..."

            $ pluto_aff -= 1
    
    hide pluto with dissolve

    "I notice Theo waiting in the sedan nearby, it looks like it's time to wrap up the date and head home."

    stop music fadeout 2

    $ renpy.sound.stop(fadeout=1)

    scene bg black with dissolve

    play sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    queue sound "audio/SFX_Drive_Away_1.mp3" volume 0.1

    pause 2

    scene bg theo sedan with fade

    play music "audio/OST_Mr_Secretary_You_Have_A_Call.mp3" fadein 0.5 volume 0.1

    "The moment we enter the car, Pluto huddles up next to the car door and locks her eyes on the passing scenery. I glance between her and Theo, who tries to egg me on through the rearview mirror."
    
    "Finally gathering the courage to ask her if she enjoyed herself, I see her eyes shut in the reflection of the window."

    "{i}She must’ve been exhausted, since she hasn’t really explored Earth before.{/i}"

    "I exhale my underlying exhaustion."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Long day?"

    mc "Yep..."

    theo "So? How was it? Since I have to report back and all."

    if pluto_aff > 3:

        $ renpy.notify("You feel like today was successful.")
        
        mc "I think it went alright. As far as I can tell I feel like she had fun, but it’ll be awhile before she gets comfortable with me I think."

        show theo smile with Dissolve(0.2)

        theo "Then I guess either you or me should start arranging another date huh? If you ever need a lady’s man for help, I’m your guy."

        mc "I get it, you’re married."

        theo "And happily too. Maybe that’ll be you someday, but for now you’ll be the astronomy major with your head in the stars."

        mc "Yeah, yeah shove it."

        "Theo and I exchange a smirk all in good fun."

    elif pluto_aff == 3:

        $ renpy.notify("You feel like today could be better.")

        mc "I’ll probably have to talk to her some more, I can’t really tell how she feels right now."

        theo "She seems like a hard nut to crack, I’d probably give it some time."

        mc "I can tell. I’ll still try though. It’s my job after all."

        show theo smile with Dissolve(0.2)

        theo "Don’t sound so defeated, it was just the first date. I’m sure the second one will go better now that you’ve got a better grasp on how to talk to her."

        "The rest of the drive went on in relative silence as I stared out the window."
    
    elif pluto_aff < 3:

        $ renpy.notify("You feel like today was rough.")

        mc "I really messed that up... I don’t know if she’s going to want to help our mission at all, honestly..."

        show theo sweat with Dissolve(0.2)

        theo "Come on man, you were the negotiator! For the sake of both of our jobs I hope that you can pull something together."

        mc "I do too..."

        "The rest of the drive went on with an awkward tension between Theo and I."

    scene bg black with dissolve

    play sound "audio/SFX_Drive_Away_1_Cut.mp3" volume 0.1

    queue sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    pause 3
    
    scene bg isaac ext with fade

    stop music fadeout 2

    "The car ride continued in silence for some time, before finally arriving in front of the ISAAC building."

    "Pluto reluctantly opens her eyes after a gentle nudge on the shoulder from me. Pluto, still half asleep, mumbles some incoherent words before following along with me and Theo into the building."

    "After a long day in each other's company, I feel as if the two of us have come to know each other a little bit better."
    
    "Moments before we part, something comes to mind that I just have to get off my chest."

    mc "P-Pluto!"

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    pluto "Y-yes?"

    mc "I have something I need to tell you. The truth is..."

    menu:
        "I love you!":

            "[[{i}A loud car drives by and completely drowns out what you were trying to say. You feel as if the writing gods did not want you to make this choice yet...{/i}]"

            show pluto shy with Dissolve(0.2)

            pluto "Sorry, I didn't catch that..."

            if pluto_aff > 3:

                show pluto joy with Dissolve(0.2)

                pluto "But today was really fun."
            
            else:

                show pluto neutral with Dissolve(0.2)

                "Pluto gives a small nod and shyly waves her hand."

        "Today was a lot of fun.":

            if pluto_aff > 3:

                show pluto joy with Dissolve(0.2)

                pluto "Y-yeah, it was! Thank you..."
            
            else:

                show pluto neutral with Dissolve(0.2)

                "Pluto gives a small nod and shyly waves her hand."


        "The moon is made of cheese.":

            pluto ". . ."

            pluto "I knew it."

            pluto "That explains so much..."

            if pluto_aff > 3:

                show pluto joy with Dissolve(0.2)

                "Pluto giggles to herself."

                pluto "Thanks for today. It was really fun."
            
            else:

                show pluto neutral with Dissolve(0.2)

                "Pluto gives a small nod and shyly waves her hand."
    
    show pluto neutral with Dissolve(0.2)

    if pluto_aff > 3:

        pluto "See you next time, [first_name]!"
    
    else:

        pluto "Bye-bye, [first_name]."

    "Pluto leaves in a hurry, no doubt tripping on her dress, somewhere out of sight."



