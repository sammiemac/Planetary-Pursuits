
label pluto_date2a:

    scene bg black with dissolve

    play sound "audio/SFX_Transition_Scene.mp3" volume 0.2

    pause 2

    centered "{b}{color=#ffffff}A few days after the first \"date\"...{/b}{/color}"

    centered "{color=#ffffff}After the ice rink date didn't go as planned, I felt like I needed to make it up to Pluto somehow, so I decided to take her to a ski resort."

    centered "{color=#ffffff}She didn't seem to know much about skiing or resorts, but she loved the idea of being surrounded by snow and large open spaces."

    centered "{color=#ffffff}Once again we set a date and let Theo know so that he could come along and chauffeur. On the day of the trip, we picked her up and set off on a long ride to the resort..."

    centered "{color=#ffffff}When we arrived at the resort, the snow-covered landscape took her breath away. She had never seen anything like it before, and her eyes lit up with wonder and amazement."

    play music "audio/OST_Mr_Secretary_You_Have_A_Call.mp3" fadein 0.5 volume 0.1

    scene bg theo sedan winter with dissolve:

    "I can’t help but feel a sense of excitement and nervousness at the same time as we get closer to the resort."

    "This time, everything will go perfectly and she will be sure to enjoy the outing more than our previous one."

    mc "When we get to the ski resort, we’re going to have to make the tough choice between extreme skiing or survival snowboarding."

    show pluto pose think with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    pluto "W-well, actually---"

    mc "Maybe we could try sledding!"

    show pluto shy
    
    pluto "Um..."

    mc "Oh! And I checked the website of this resort the other day, guess what else is here?"

    show pluto flustered

    pluto "Huh?"

    mc "An ice skating ri---"

    theo "{i}Ahem."

    show pluto shy:
        linear 0.5 xalign 0.125
    
    show theo neutral with dissolve:
        xalign 0.875
        yalign 0.005
        zoom 0.60
    
    "Theo glares at me from the rear-view mirror."

    "{i}Looks like I was totally talking over Pluto..."

    mc "Sorry Pluto, was there something you wanted to say?"

    show pluto shy:
        linear 0.5 xalign 0.5
    
    hide theo with dissolve

    pluto "N-no not really... it's just that those activities sound kind of intense and I’m starting to think that there might be a lot of people when we get there..."
    
    show pluto cry

    pluto "{size=-5}... too many people..."

    "Pluto isn't looking too excited aobut this date anymore... Maybe I should try a different approach."

    menu:

        "\"Don't be such a weenie.\"":

            $ pluto_aff -= 1

            show pluto flustered

            pluto "A w-weenie?! Like a weenie dog?"

            mc "Well no, not exactly. Like a hotdog with bread---"

            show pluto stern

            pluto "A dog that's hot?"

            mc "Not an actual dog, it's an Earth expression--- it means coward or chump, but in a nicer way." 

            show pluto shy

            pluto "O-oh..."

            show pluto cry

            pluto "{size=-5}... I guess I am a weenie."

            mc "Yeah, you're kind of killing the vibe, but I suppose we could do something else instead then."

            $ renpy.notify("Pluto looks to be on the verge of tears.")
        
        "\"I'm not too sure what you're getting at.\"":

            show pluto shy:
                linear 0.5 xalign 0.125
    
            show theo sweat with dissolve:
                xalign 0.875
                yalign 0.005
                zoom 0.60

            theo "Maybe she'd prefer a different activity around here?"

            mc "O-oh yeah...! I know that... How about we do something else then?"

        "\"What would you like to do, Pluto?\"":

            $ pluto_aff += 1

            $ renpy.notify("Pluto appreciates you asking.")

            show pluto flustered

            pluto "M-me? I hadn't really thought about it..."

            show pluto pose think

            pluto "But if I had to choose, then maybe somewhere more... secluded?"

            pluto "I'm not too sure what else we could do in the snow, I am not really experienced with outside activities..."

            mc "Hmmm..."

            mc "I got it."

    hide pluto with dissolve
        
    "Just then, I notice sometihng outside the window that catches my eye."

    label stop_car:

        mc "THEO STOP THE CAR!"
        
        scene bg ski resort ext with dissolve:
            zoom 1.2
        
        mc "This is perfect!"

        show theo sweat with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.60

        theo "Uh boss, we are kind of in the middle of nowhere..."

        mc "Let's get out here Pluto, we can keep heading to the cabin later."

        show theo sweat:
            linear 0.5 xalign 0.125
        
        show pluto shy with dissolve:
            xalign 0.875
            yalign 0.005
            zoom 0.60
        
        pluto "O-okay, um... Why did we stop here though?"


