
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

    show pluto winter flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    pluto "W-well, actually---"

    mc "Maybe we could try sledding!"

    show pluto shy
    
    pluto "Um..."

    mc "Oh! And I checked the website of this resort the other day, guess what else is here?"

    show pluto winter flustered

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
    
    show pluto winter cry

    pluto "{size=-5}... too many people..."

    "Pluto isn't looking too excited aobut this date anymore... Maybe I should try a different approach."

    menu:

        "\"Don't be such a weenie.\"":

            $ pluto_aff -= 1

            show pluto winter flustered

            pluto "A w-weenie?! Like a weenie dog?"

            mc "Well no, not exactly. Like a hotdog with bread---"

            show pluto winter stern

            pluto "A dog that's hot?"

            mc "Not an actual dog, it's an Earth expression--- it means coward or chump, but in a nicer way." 

            show pluto shy

            pluto "O-oh..."

            show pluto winter cry

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

            show pluto winter flustered

            pluto "M-me? I hadn't really thought about it..."

            show pluto shy

            pluto "But if I had to choose, then maybe somewhere more... secluded?"

            pluto "I'm not too sure what else we could do in the snow, I am not really experienced with outside activities..."

            mc "Hmmm..."

            mc "I got it."

    hide pluto with dissolve

    stop music fadeout 2
        
    "Just then, I notice sometihng outside the window that catches my eye."

    label stop_car:

        mc "THEO STOP THE CAR!"

        play music "audio/OST_A_Thawing_Heart.mp3" fadein 0.5 volume 0.1
        
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

        mc "To build a snowman of course!"

        show pluto winter flustered

        show theo neutral

        pluto "A snowman?!"

        mc "That's right! It's basically an activity where we make sculptures made out of snow and ice."

        show pluto winter neutral

        pluto "T-that sounds like fun! I like making things."

        mc  "Then why don't we have a competition and see who can make the best snowman? Theo can even be the judge."

        show theo smile

        theo "I watched all 25 seasons of Judge Judy, so naturally that makes me the most qualified person here."

        show pluto winter joy

        pluto "Okay, I'll do my best!"

        "{i}Pluto looks surprisingly pumped for this. I'm going to have to go all out and impress her with my art skills!"

        scene bg ski resort ext with dissolve:
            zoom 1.2

        $ neo_armstrong = False

        menu snowman_menu:
            "{i}Hmmm... What kind of snowman should I make?"

            "(Choice 1: Make a regular snowman.)":

                mc "A classic snowman should be perfect! With Frosty on my side, there's no way I'll lose!"

                $ snowman_choice = 1

            "(Choice 2: Make a rockin' replica of the Eiffel Tower.)":

                mc "I didn't get voted the \"Most Creative\" in high school for nothing. A replica of one of Earth's finest creations should do the trick!"

                $ snowman_choice = 2

            "(Choice 3: Make a snow dog.)":

                "Since Pluto is into dogs, this might be a good chance to get on her good side."

                mc "Allow me to show you why I was voted \"Most Creative\" in high school. There's nothing I can't do if I set my mind to it!"

                $ snowman_choice = 3

            "(Choice 4: Make the Neo Armstrong Cyclone Jet Armstrong Cannon.)" if not neo_armstrong:

                mc "The what---?"

                $ neo_armstrong = True

                jump snowman_menu

            "(Choice 5: Contemplate what happened to Choice 4.)" if neo_armstrong:

                mc "... Some things are best left unquestioned."

                "{i}I think it might be best to go with Choice 1. I didn't exactly get an A in my art class in college..."

                $ snowman_choice = 1
            
        show pluto shy with dissolve:
            xalign 0.5
            yalign 0.005
            zoom 0.60
        
        pluto "Hmmm..."

        mc "Whoa, are you alright? You haven't moved in the last 3 minutes, your snowman is never going to be built at this rate."

        show pluto winter flustered

        pluto "I got it!"

        show pluto winter joy

        pluto "A bit of this here... some of that there..."

        mc "Um..."

        "She doesn't seem to be listening. She just started but her snowman is looking a lot better than mine already... I have to distrct her somehow if I want to win."

        mc "So Pluto..."

        menu:

            "\"Have you ever heard the tragedy of Darth Plagueis the Wise?\"":

                stop music fadeout 2.0

                show pluto shy

                pluto "No."

                mc "I thought not. It's not a story the Jedi would tell you."
                
                mc "It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and wise he could use the Force to influence the midichlorians to create life..."

                mc "He had such a knowledge of the dark side that he could even keep the ones he cared about from dying."

                mc "The dark side of the Force is a pathway to many abilities some consider to be... unnatural."
                
                mc "He became so powerful, the only thing he was afraid of was losing his power, which eventually, of course, he did."

                show pluto winter cry

                mc "Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep."
                
                mc "Ironic."

                mc "He could save others from death, but not himself."

                show pluto winter stern

                pluto "Is it possible to learn this power?"

                mc "No, at least, not from a Jedi."

            "\"How about I recite a poem I wrote for you?\"":

                show pluto winter flustered

                pluto "Oh, um... Okay, I guess."

                mc "Oh Pluto, my Pluto---"

                show pluto shy

                mc "---Wherefore art thou, Pluto?"

                show pluto winter flustered

                pluto "I'm right here."

                mc "N-no, I wasn't done yet... {i}*ahem*"

                mc "However so divine, yet posture so fine..."

                mc "Be it books or looks, my thoughts betray me with thine hooks."

                show pluto shy

                pluto "{cps=10}{size=-5}... mid..."

                show pluto winter flustered

                pluto "I-I mean, that was... something else. Interesting, but it was sweet... I think..."

                mc "Thank you, thank you. Perhaps an encore will do nicely?"

                show pluto winter stern

                pluto "N-no!"

                show pluto winter neutral

                pluto "I mean, I think that was more than enough for me..."

                mc "Another time then."

            "\"Ya like Jazz?\"":

                stop music

                show pluto shy

                pluto "... Didn't you already ask me this before?"

                mc "Oh shoot--- Wait, that didn't happen, that was another timeline with Ma---"

                hide pluto with dissolve

                show theo neutral with dissolve:
                    xalign 0.5
                    yalign 0.005
                    zoom 0.60
                
                #play sound "audio/SFX_Gun_Click.mp3"

                theo "Sorry boss, but you know too much."

                #play sound "audio/SFX_Gun_Shot.mp3"

                scene bg black

                jump stop_car

            "\"Have you found any interesting hobbies to do in your time here?\"":

                show pluto winter neutral

                pluto "Oh, well there have been a few things I found interesting. There are these little craft activities which I have started to learn a lot about."







