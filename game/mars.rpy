
#Random encounter with Mars, happens after meeting Pluto.
label mars:

    "{i}Who would have thought Pluto could leave such an impression; a shy, pale-skinned girl who could float was something out of a fantasy visual novel.{/i}"

    "{i}I still can’t believe there are 8 more planets like her. I’m not sure I could handle meeting even one more---{/i}"

    "Before I finish my thought, I am interrupted by an upbeat chirpy voice from behind me."

    "???" "Hi Hi! What are you doing brooding around so hard?"

    "I turn around and am quickly surprised to meet a short, orange-skinned, red-haired girl with a smug grin and…. Is that… camo shorts?"

    play music "audio/OST_Retrograding_With_You.mp3" volume 0.1

    show mars smug with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.5
    
    "???" "Hey, that's better! I know I wasn't supposed to come in 'til later, but I got too excited and couldn't wait! The name’s Mars, nice to meetcha!"

    "Camo shorts aside, I struggle to find the words to respond in this unforeseen situation..."

    mc "Oh! Uh, hi...? This is a little unexpected. I haven’t mentally prepared myself for another introduction..."

    show mars neutral

    mars "Not to worry! I {i}maaay{/i} have secretly overheard you talking about Pluto earlier and just knew we would get along fast! Any friend of Pluto is a friend of mine."

    mc "Not sure if friends is the right word, but yeah I guess you could say that. Was there something you wanted that couldn't wait 'til later?"

    show mars smug

    mars "Nope!"

    mc "Oh. Okay then..."

    "What in the world am I supposed to say in this awkward situation...? Think, what would Theo do?"

    $ asked_jazz = False
    $ asked_shorts = False
    $ asked_pluto = False
    $ asked_float = False

    label mars_choices:

        show mars neutral

        menu:

            "\"So... ya like jazz?\"" if not asked_jazz:

                show mars tired

                mars "\'Jazz\'? What's that?"

                show mars excited

                mars "OH! Are they a part of those jacuzzis I've heard so much about? I've really wanted to try one out!"

                show mars tired

                mc "No no, I think you're confusing jacuzzis with jazz, those are two totally separate things. One is a small, hot body of water usually accompanied by bubbles, and the other is a banger type of music."

                show mars excited

                mars "BUBBLES?! BANGER MUSIC?! Now I really want to visit a jazzcuzzi!"

                "{i}Aaand she's not listening anymore..."

                $ asked_jazz = True

                jump mars_choices

            "\"Nice camo shorts.\"" if not asked_shorts:

                show mars excited

                mars "{i}*gasp*{/i} RIGHT?! Finally, someone who gets me! I've been showing it off to all the other planets like Pluto, but she says that the length was \"too short\" for her."

                show mars smug

                mars "But honestly, the color! The style! The pattern!"

                mars "Everything about it was just shouting my name!"

                show mars neutral

                mc "Your shorts were shouting for Mars?"

                mars "And beyond! {i}*ba dum tsss*{/i}"

                $ asked_shorts = True

                jump mars_choices

            "\"Pluto's pretty shy, huh?\"" if not asked_pluto:

                show mars tired

                mars "{i}*sigh*{/i} She is... I've been trying to tell her to be more confident in herself, to speak louder and to stop weaning a coat in the middle of summer!"

                mars "Pluto always says she isn’t like me and can’t do all those things, but I know she can do it if given the right push."

                mc "Huh, I can see you two are really good friends."

                show mars neutral

                "Of course! She’s the only one who doesn’t laugh at my shorts!"

                mc "That's... not the {i}best{/i} way to measure a friendship..."

                show mars excited

                mars "{i}*gasp*{/i} Speaking of my shorts, just the other day, I---"

                "{i}Oh boy, here we go..."

                $ asked_pluto = True

                jump mars_choices

            "\"Can you float, too?\"" if not asked_float:

                show mars smug

                mars "Well, of course I can, dummy!"

                hide mars with dissolve

                "Once again, like magic, the red-head in front of me proceeds to float several feet off the ground and twirl a few times before landing with what looks to be some kind of superhero pose."

                show mars smug with dissolve:
                    xalign 0.5
                    yalign 0.005
                    zoom 0.5

                mars "How was that? Impressed? I know, I know--- I am pretty {i}awesome{/i}."

                mc "I can’t deny that, every time I see one of you planets float, I’m awestruck."
                
                mc "Plus, you're pretty cute."

                show mars blush

                mars "C-C-CUTE?!"

                mc "Yeah, like a puppy---"

                "Mars quickly ran up, hiding her face, and started hitting me before I could even finish, apparently no longer listening."

                show mars baka

                mars "Y-YOU BIG DUMMY!!!"

                $ asked_float = True

                jump mars_choices
    
    hide mars with dissolve

    "After a few more moments of awkward silence, I suddenly remember what my job was in the first place."

    show mars neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.5

    mc "Well, what were you thinking for a date?"

    mars "Isn’t it obvious? There’s only one thing that people should do on dates and that's...!"

    mc "That's...?!"

    show mars smug

    mars "MINESWEEPER BABY!!!"

    "[[... is what Mars would've said.]"

    hide mars with dissolve

    "[[But due to some odd circumstance, the Minesweeper game didn't happen. As if some outside force, like a god or even a programmer, tried their damndest to get it to work, but just couldn't.]"
    
    "[[Maybe they messed up writing the code somewhere. Maybe the tutorial they were following was wrong or outdated. Hell, maybe even the universe could not allow it to happen.]"

    "[[Instead, some outside force will decide the outcome of this \"game.\" Random chance, a name pulled out of a hat. And that result is...]"

    #A 33% chance of getting a Good, Neutral, or Bad outcome.
    $ mars_outcome = renpy.random.randint(1, 3)
    if mars_outcome is 1:
        jump outcome_good
    elif mars_outcome is 2:
        jump outcome_neutral
    elif mars_outcome is 3:
        jump outcome_bad

    label outcome_good:

        $ renpy.notify("Mars is impressed by your Minesweeper skillz.")

        show mars smug with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5

        mars "{i}Exxplosssion!!!{/i} That date was the bomb! Same time next week?"

        mc "Honestly, I think I am a little tired from such intense Minesweeping. I might need to take a rain check on that one. Maybe next semester instead?"

        show mars tired

        mars "Awww, but waiting is boooring... Oh well, I guess I can wait. I know it will be an even better date next time!"

        "The thought of a hard and eventual expert level difficulty of Minesweeper scares me to no end... It looks like I have a lot of training to do."

        show mars neutral

        mc "Haha yeah, I'm looking forward to it, too."
        
        mars "Well then---"

        hide mars with dissolve

        "Mars quickly runs up to me... and gives me a kiss on the cheek."

        show mars neutral with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5
        
        mars "See you next time! Tell Pluto I said hi!"

        hide mars with dissolve

        "And just like that, she's already running off to who knows where."

        mc "That girl really has limitless energy..."

        jump mars_encounter_end

    label outcome_neutral:

        $ renpy.notify("Mars nods approvingly at your Minesweeper game.")

        show mars neutral with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5
        
        mars "Your Minesweeper skills need some work, but they were alright. I give it a solid 7/10!"

        mc "I didn't know this turned into some kind of game show, but I am pretty tired from that intense Minesweeping."

        "{i}I may have to brush up on my skills for any future dates if I don’t want to make fool of myself..."

        mars "Mhm! I can picture the next date already: you, reaching a new highscore under my direct tutelage..."
        
        show mars smug

        mars "From now on, it's nonstop training!"

        "Somehow, the thought of that scares me more than clearing out bombs..."

        show mars neutral

        mc "I’ll be looking forward to next time."

        mars "Well then---"

        hide mars with dissolve

        "Mars quickly runs up to me... and gives me a tight hug."

        show mars neutral with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5
        
        mars "See you next time! Tell Pluto I said hi!"

        hide mars with dissolve

        "And just like that, she's already running off to who knows where."

        mc "That girl really has limitless energy..."
        
        jump mars_encounter_end
    
    label outcome_bad:

        $ renpy.notify("Mars cringes at your lack of Minesweeper rizz.")

        show mars tired with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5
        
        mars "That date really \"blew up\" in your face."

        mc "I'll admit, it was not my best showing of skills."

        mars "Well then---"

        hide mars with dissolve

        "Mars quickly runs up to me... and gives me a pity pat on my back."

        show mars neutral with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.5
        
        mars "I'm sure you'll do better next time! Tell Pluto I said hi!"

        hide mars with dissolve

        "And just like that, she's already running off to who knows where."

        mc "That girl really has limitless energy..."

        jump mars_encounter_end
    
    label mars_encounter_end:

        "And now, I find myself alone in this room. Again."
