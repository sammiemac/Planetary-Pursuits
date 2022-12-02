
# Pluto's first date, ice rink
label pluto_date1:

    scene bg black with dissolve

    centered "{b}{color=#ffffff}A few days later, around noon...{/b}{/color}"

    show bg isaac ext with dissolve

    "After a few days to give Pluto time to settle in, I got ready for our scheduled date per our agreement. Naturally, Theo as my secretary also acted as the designated escort and driver, as embarrassing as it was to be chauffeured to my date."

    "Theo waited in the car while I went to knock on Pluto’s door. From the other side, muffled panic and rummaging could be heard until finally an out-of-breath Pluto answered the door."

    show pluto neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    menu:
        "Compliment her dress.":

            mc "You look really nice in that dress, Pluto."

            show pluto shy

            pluto "You don't need to lie, I know it doesn't suit me..."

            mc "No, it's true! It's something only you could pull off."

            show pluto flustered
            
            pluto "O-oh, thanks..."

            $ dress_complement = True

        "Stay quiet.":

            "Deciding not to come off strong and seeing Pluto in a vulnerable state, I choose to let the topic of her choice in dress slide and focus on the task at hand."

            show pluto flustered

            "Pluto seems surprised to not be put down for her choice in fashion."

            $ dress_complement = False

        "Make a joke.":

            mc "Wow, we’re going ice skating, not to a ball!"

            show pluto flustered

            "Just as I finish, Pluto is visibly devastated. A mixture of sadness and confusion on her face."

            show pluto shy

            pluto "I-I'm sorry, I'm not too familiar with Earth's customs yet, figures I'd mess up already."

            mc "Actually, I was just making a joke... I didn't mean to offend you."

            pluto "No, you're right, this dress doesn't look good on me in the first place. I don't know what I was thinking..."

            "{i}Well that was terrible, way to go me...{/i}"

            $ dress_complement = False

    scene bg black with dissolve

    #play sound "<from 0 to 2.5>audio/SFX_car_door.wav" volume 0.02
    
    scene bg theo sedan with dissolve

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

            pluto "Y-yea."

            hide pluto with dissolve

            "Theo gives me a mocking glance from the rearview mirror at my terrible attempt at conversation."

        "Stay quiet.":
            pass
    
    "Defeated, I likewise resort to staring out the window."

    scene bg ice rink ext with fadein

    show pluto shy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "As soon as we step out of the car, Pluto immediately hides behind my shoulder, keeping her arms and hands close together in a self-hug, hiding from everyone as they walk past."

    "{i}She probably doesn’t like crowds too much.{/i}"

    mc "It’s a weekday, so there shouldn’t be too many people."
    
    show pluto neutral

    "Pluto doesn’t respond, but she seems to ease up if only by a little."

    hide pluto with dissolve

    "The lobby is primarily filled with couples, barely any families who are likely on vacation, and what looks to be professionals since they have their own personal pair of skates brandished with sponsorships. Despite this, there are hardly any people, most of which are leaving and those who aren’t are still strapping on their skates."

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
        
        pluto "T-thank you."
    
    else:

        show pluto neutral with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.60

        pluto "O-oh, thanks."
    
    scene bg ice rink int with fadein

    "We sit on one of the nearby benches to tie on our skates. Pluto watches me put them on, then tries to replicate the action herself, albeit much slower. For a solid three minutes, she struggles to tie a knot with the shoelaces and is clearly getting to the point of being both embarrassed and defeated."

    "Unable to observe her self-torture any longer, I bend over to help her."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "N-no you don’t have to, i-it’s alright."

    show pluto cry

    pluto "I know I’m a burden..."

    mc "Don’t say that. I used to tie my best friend’s shoes up until middle school, so don’t worry about it!"

    "I give her a reassuring smile, but I can’t tell if it helps or not."

    mc "It might be a little hard for you to walk in them, so if you want you can hold onto me until you get used to it."

    show pluto shy

    pluto "N-no it’s okay. I don’t want to slow you down."

    "She keeps her eyes to the floor with a tight lip. Still a bit worried, I make sure to glance at her every now and then as we make our way to the ice rink."

    scene bg ice rink with dissolve

    "An instant gush of frigid air hits us as soon as we enter and I pull my coat closer."

    "{i}I haven't been to an ice rink since I was a kid, were they always this cold?{/i}"

    "Expecting Pluto to be equally freezing and discomforted, I braced myself for her visual pain as a sign that I've messed up once again."

    show pluto joy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "To my surprise, it's actually the opposite. She seems... happy? At least judging by the slight twinkle in her eye."

    "For now though, I decide not to make a comment on it."

    #play sound "<from 0 to 2.5>audio/SFX_ice_skate.wav" volume 0.05

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

    show pluto flustered

    "As soon as she attempts to move, she starts to lose balance and thus desperately grabs the railing."

    mc "Just small steps are fine!"

    "After an extended pause to regain her footing, she tries again and has the same result"

    "Once again, her eyes focus on the others around us. The only ones who seem to be struggling are children more than half our age... and us."

    show pluto cry

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

            pluto "..."

            "{i}I just made it worse.{/i}"

            "Pluto manages to stand back up without much trouble."

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

            pluto "It’s alright, I could say the same about myself."

            mc "Well, now we’re both on the ground so I guess we’re equal now."

            "Still smiling to ourselves, we slowly get back on our feet."

            $ help_up = True

        "Help her up and dust her off.":

            "I lift her by her arm in an attempt to help, then try to dust off her dress for her. The moment I reach down, she backs off and makes distance between us."

            show pluto stern with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "I-I’m alright..."

            "{i}I just made it worse.{/i}"

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

    scene bg ice rink int with fadein

    "Well, that was an experience. Skating had left both Pluto and I more exhausted than we wanted to admit, a break was more than needed. Suddenly, a familiar noise began to fill the building; its source coming from the outside."

    play music "audio/OST_Ice_Cream_Jingle.mp3" fadein 0.5 volume 0.01

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

            pluto "O-oh! I’m not sure, but I am a bit curious..."

            show pluto neutral

            "Pluto seemed a bit taken back by my question, but still eager in her own way."
    
    scene bg ice rink ext with fadein

    play music "audio/OST_Ice_Cream_Jingle.mp3" fadein 0.5 volume 0.05

    "We exit the ice rink, the hot sun and warm air letting us know that the day isn’t over yet."

    mc "As expected, it’s an ice cream truck!"

    "Glancing at Pluto, I notice that she has a slight sparkle in her eyes as she looks around the area."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    pluto "There's so many people... there's kids, parents, and even..."

    pluto "{i}*GASP!*{/i}"

    "I look over to see what has caused Pluto to be in a state of disarray, and I find the culprit."

    show dog with dissolve
    
    "A dog sitting near a bench, right across from the ice cream truck, with the owner weaning a pair of sunglasses and eating an ice cream sandwich."

    "The dog was a fluffy golden retriever, medium sized, tongue out as it attempted to cool itself off from the hot sun."

    "Pluto's eyes were quickly shifting up from the floor, back to the dog, then back to the floor. She seemed to be interested in the dog, but was unsure of what to do. I give her a gentle tap on the shoulder to get her attention."

    mc "Hey, Pluto--"

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "Eeep!"

    show pluto shy

    pluto "Oh sorry, I was a bit distracted..."

    mc "You really like dogs, huh?"

    show pluto neutral

    pluto "Oh, well, they are kind of nice, I guess."

    pluto "They are really friendly, and soft, and fluffy, and playful and people really like them and..."

    show pluto shy

    pluto "{i}sometimeswhenIseeadogIjustthinkitwouldbereallycooltopetthem--{/i}"

    mc "Woah woah, slow down!"

    show pluto flustered

    pluto "Ah-- sorry, I did it again didn’t I?"

    show pluto shy

    pluto "Dogs are my favorite animals, sometimes I get carried away when talking about them. It really makes me wish I had my own..."

    mc "Don’t worry about it, everyone has something they are really passionate about, and I bet we could even help get you a dog."

    show pluto flustered

    pluto "R-Really?!"

    mc "Sure! But first..."

    menu:
        "Encourage Pluto to go pet the dog.":

            mc "Why don’t you try and ask the owner if you can pet the dog?"

            show pluto shy

            pluto "I- I’m not sure I could pull that off."

            mc "Don’t worry! Look, there are a group of kids petting the dog already, I’m sure the owner won’t mind."

            show pluto neutral

            pluto "Alright, I’ll do it, if you think I can..."

            hide pluto with dissolve

            "Pluto proceeds to walk up to the owner with sunglasses, getting a bit nervous, but seemingly calming down once the dog looks at her and barks around her."

            show pluto shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            pluto "E-excuse me, w-would it be alright if I could maybe-- if you wouldn't m-mind--"

            "Owner" "Go ahead miss, you can pet him! No need to be shy, he loves the attention."

            show pluto flustered

            "Pluto’s eyes light up as she reaches down to pet the excited dog."

            show pluto joy with dissolve on right

            show dog with dissolve on left

            pluto "Hehe, what a good boy!"

            "Dog" "Borf!"

            "The two share a close moment of friendship as Pluto has a big smile on her face, eventually standing back up, satisfied."

            hide pluto with dissolve

            hide dog with dissolve

            show pluto joy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "That was nice, thank you."

            "Whether she was thanking me or the dog owner, I’m not sure."

        "Ask the dog owner if Pluto can pet the dog.":

            mc "Why don’t I go and ask the owner if you can pet the dog?"

            show pluto shy

            pluto "I-I wouldn’t want to bother you."

            mc "Don’t worry! Look, there are a group of kids petting the dog already, I’m sure the owner wouldn’t mind."

            show pluto neutral

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

            show pluto joy with dissolve on right

            show dog with dissolve on left

            pluto "Hehe, what a good boy!"

            "Dog" "Borf!"

            "The two share a close moment of friendship as Pluto has a big smile on her face, eventually standing back up, satisfied."

            hide pluto with dissolve

            hide dog with dissolve

            show pluto joy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "That was nice, thank you."

            "Whether she was thanking me or the dog owner, I’m not sure."

