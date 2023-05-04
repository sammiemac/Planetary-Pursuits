
label pluto_date2b:

    scene bg black with dissolve

    pause 1

    scene bg ski resort night with dissolve:
        zoom 1.2

    play music "audio/SFX_Wind_Long.mp3" fadein 0.5 volume 0.1

    "After an eventful day of snowman--- or dog--- making, Pluto and I are about ready to crash for the day. From the corner of my eye, I see Theo wake up and motion me to come speak with him as he exits the car."

    "{i}What could he possibly want? I’m sure he said he can’t interfere with the date or anything."

    mc "Sorry Pluto, could you give me a second? You can wait in the car, I’ll be right back."

    show pluto winter flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "O-oh, no worries."

    hide pluto with dissolve

    play sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    "Theo pulls me aside, no more than a few feet from the silver sedan."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "You want the good news or bad news first?"

    "I sigh, already imagining the disastrous scenarios that could spill out of his mouth, but judging from his still somewhat nonchalant demeanor, it can’t be {i}that{/i} bad."

    mc "Bad news, I suppose."

    theo "Snow’s getting really heavy, so unless you wanna risk her---"

    "Theo glances at the car to make sure the windows are closed but whispers anyways."

    theo "... y'know, getting hurt in a car wreck--- or worse, {i}dying{/i}--- then it’s probably best that we don’t drive more than we have to."
    
    show theo smile with Dissolve(0.2)
    
    theo "This is where the good news comes in."
    
    show theo neutral with Dissolve(0.2)

    theo "We’re not all that far away from a cabin rental spot, so we can just call it for the night and wait out the storm, which should clear by morning."

    mc "And if they’re all taken up? Because I’m sure that there’s plenty of skiers with the same idea."

    show theo smile with Dissolve(0.2)

    theo "Did you forget we work for the government? Not just the government, but {i}the{/i} President. It really wouldn’t take more than waving around an ID or a phone call to get a room."

    mc "... And I'm guessing Pluto doesn't have a say in this?"

    show theo neutral with Dissolve(0.2)

    theo  "Unless your superpowered girlfriend can change the weather, nope."

    "I look back at Pluto, who's peacefully resting against the car door in blissful ignorance."

    "{i}I'd really hate for her to be stuck outdoors, let alone with {/i}me{i} more than she'd have to, but there really aren't any other options, so..."

    mc "Alright... I'll tell her then. I'll at least let her choose what kind of room she wants."

    theo "And if she throws it back at you?"

    mc "Then whatever you come up with."

    show theo smile with Dissolve(0.2)

    "Theo snickers at my comment, but I ignore him altogether. Whatever he has floating around in his mind probably isn’t any good, and it makes me regret my choice nearly instantly."

    scene bg theo sedan night with dissolve

    play sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    "After reentering the car, Pluto greets me with a slight smile while Theo side-eyes me from the rearview mirror."

    mc "Well... It’s gonna snow pretty heavily on our way back, so it’s better if we wait it out for the night in one of the nearby cabins if that’s fine with you."

    show pluto winter flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "I-I don't mind."

    mc "... Do you have a preference for what kind of room you want, ooor...?"

    show pluto winter neutral with Dissolve(0.2)
    
    pluto "Whatever you decide."

    hide pluto with dissolve

    "Judging from her fairly quick and light response, she seems genuine enough which lessens my guilt if only by a bit."

    "Giving a slight nod to Theo from the mirror, he understands to get the car going."

    stop music fadeout 2

    scene bg black with dissolve

    play sound "audio/SFX_Transition_Scene.mp3" volume 0.2

    pause 2

    scene bg cabin lobby with dissolve

    play music "audio/OST_Chill_Theme.mp3" volume 0.1

    "By the time we get there, there’s already a swarm of people in the lobby with all forms of winter themed athletic equipment ranging from snowboards to skis."
    
    "Mostly families and groups of friends are present with only a few couples scattered here and there, but they all share the same traits: covered in snow and completely exhausted--- us no different."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    theo "You two wait here, I'll go ahead and get you guys a room."

    hide theo with dissolve

    "Theo heads off to the receptionist counter. In the meantime, I look to see how Pluto is doing."

    show pluto winter shy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "Her brows are in an uneven knit and she’s watching the people with shaky pupils, gravitating closer and closer to me by the second until she’s full on hugging my arm."

    mc "Sorry, hopefully it won't be all that long."

    "She responds in the form of more unease and a tighter grip on my arm to cope."

    "{i}I hope she’ll be alright..."

    "For someone who dislikes crowds, this is most definitely a nightmare."

    hide pluto with dissolve

    "A majority of the residents seem to be in some form of argument with an employee, which is to be expected with a sudden snow-in."
    
    "Those who aren’t arguing are trying to get by to their already-reserved rooms without setting off a nerve with the agitated masses."

    "After some extensive arguing himself, Theo returns with two sets of key cards and hands me one of them."

    show theo smile with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Told you, government jobs. This one's for you guys."

    mc "And the other?"

    theo "For me. Or did you expect me to sleep in the car?"

    "He boisterously laughs to further mock me, and if the overreaction didn’t help calm Pluto down, I would’ve fought back with a jab at his previous slumber session. Or maybe it’s the fatigue finally getting to me."

    show theo neutral with Dissolve(0.2)

    theo "I got us some good rooms, so there should be a change of clothes for you guys so you don’t have to sleep in all that. They serve breakfast, too, so I’ll see you in the morning."

    hide theo with dissolve

    stop music fadeout 2.0
    
    "With that, we part ways from Theo as I try to get Pluto away from the simmering swarm as quickly as possible."

    scene bg cabin room with dissolve:
        xalign 0.0

    play music "audio/OST_A_Thawing_Heart_CabinVer.mp3" fadein 2.0 volume 0.1

    $ renpy.sound.play("audio/SFX_Fire_Crackle_Long.mp3", loop=True, fadein=2.0, relative_volume=0.2)

    "The moment I open the door, I'm greeted with the homely warth of an electric fireplace already permeating from the room."
    
    "And...?!"

    scene bg cabin room:
        xalign 0.0
        linear 0.5 xalign 0.3

    "{i}ONE BED?!?!?!"

    scene bg cabin room:
        xalign 0.3
        linear 1 xalign 1.0
    
    pause 1.5
    
    "{i}Oh. Phew!"

    "There’s a set of {i}two{/i} queen sized beds parted by an oak nightstand and a rug. In fact, most of the dark wooden floors are covered by soft rugs."

    scene bg cabin room:
        xalign 1.0
        linear 2 xalign 0.0
    
    "By the fireplace is a set of armchairs, while the rest of the room has all forms of cozy country imagery. Furs, plants, candles, you name it."

    show pluto winter flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "From how mesmerized Pluto seems to be, she’s clearly not been in something as extravagant as this, and neither have I quite frankly."

    "{i}Government jobs..."

    "On top of the sheets are what I assume to be our loungewear, so I hand a set over to Pluto."

    mc "You can change here, I’ll change in the bathroom."

    show pluto winter neutral with Dissolve(0.2)

    "Pluto gives an acknowledging nod so I head over to change."

    scene bg black with dissolve

    play sound "audio/SFX_Clothes.wav" volume 0.1

    pause 2.0

    scene bg cabin room with dissolve:
        xalign 0.0
    
    "If I thought the clothes were a little large on me, they were completely oversized on Pluto."
    
    "The sleeves dangled over and concealed her hands, with the hem of her pants dragging across the floor. It seems like she gave up on trying to roll them to her wrists and ankles judging by the loose wrinkles."

    show pluto pj shy with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "I-I'm sorry, it doesn't fit very well..."

    mc "No, no it’s fine! Mine doesn’t really fit either."

    "I flaunt the loose sleeves to help comfort her."

    mc "We can sit by the fire if you want?"

    pluto "S-sure."

    hide pluto with dissolve

    "Rather than sitting on the provided armchairs, Pluto sits on the floor hugging her knees against her face no more than a few feet from the fireplace, so I sit right next to her so she doesn’t feel out of place."

    $ fireplace_1 = True
    $ fireplace_2 = True
    $ fireplace_3 = True
    $ fireplace_4 = True
    $ fireplace_5 = True
    $ fireplace_6 = True
    if pluto_aff > 3:
        $ fireplace_7 = True

    menu fireplace_choice:

        "{i}This feels like a good opportunity to get to know her better."

        "Ask what she thinks about global warming." if fireplace_1:

            show pluto pj shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60
            
            pluto "I-I know some of the other planets aren’t too happy about it, some are even scared of you guys because of it."

            show pluto pj neutral with Dissolve(0.2)

            pluto "But I think everything will work out! I think what’s important is that you’re trying to fix it now right?"

            "{i}Barely, with how little politicians seem to care about the issue..."

            "I nod although a bit hesitant."

            mc "Slowly but surely."

            pluto "Y-yeah! I hope that I can help... I would hate for something to happen to Earth. Or dogs."

            if pluto_aff > 3:

                show pluto pj flustered with Dissolve(0.2)

                pluto "O-or you...!"
            
            show pluto pj shy with Dissolve(0.2)

            pluto "But... it scares me sometimes. I wonder if the other planets are right. That maybe humans are really planning on taking everything or inhabiting us."

            show pluto pj stern with Dissolve(0.2)

            pluto "Especially with Jupiter, they always phrase things in a way that makes me feel dumb for believing in you all..."

            if pluto_aff > 3:

                show pluto pj neutral with Dissolve(0.2)

                pluto "But if humans are like you, then I think it's worth helping you guys out!"

                mc "Now you're making me blush, haha. I'm glad you think I'm a decent person, Theo would probably say otherwise."
            
            else:

                "Pluto mumbles to herself."

                show pluto pj shy with Dissolve(0.2)

                pluto "I'll have to think about it though..."

                "{i}Fuck. Did I mess up somewhere?"

            $ fireplace_1 = False
            
            jump fireplace_choice

        "Ask about the \"Pluto not being a planet\" debate." if fireplace_2:

            show pluto pj shy with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            "Pluto’s eyebrows raise then droop into a tight knit with pursed lips to match. After a few excruciating moments of silence, she finally speaks albeit in a hardly audible jumble."

            pluto "It doesn’t really bother me. Everyone tells me that."

            pluto "Sometimes, I think... maybe they’re right, maybe I’m not a planet... I mean, no one even cared about me until a century ago. And even then, some moons are bigger than me and {i}they’re{/i} not planets... I don’t even know myself..."

            show pluto pj cry with Dissolve(0.2)
            
            pluto "I wish..."

            "Pluto’s voice trails off until it folds back into herself."

            show pluto pj shy with Dissolve(0.2)

            "Ummm... Why don’t we talk about something else? T-this cabin is really c-cozy right...?"

            mc "Yep...!"

            "{i}Man, she looks so stiff. It seems like a sour spot for her, I should avoid saying anything about that..."

        "Ask what she’s been up to since the last date." if fireplace_3:

            show pluto pj stern with dissolve:
                xalign 0.5
                yalign 0.005
                zoom 0.60

            pluto "... Dogs..."

            menu:

                "\"Dogs?\"":

                    show pluto pj flustered with Dissolve(0.2)

                    pluto "Dogs?"
                
                "\"Dogs.\"":

                    show pluto pj neutral with Dissolve(0.2)

                    pluto "Dogs."
                
                "\"Dogs!\"":

                    show pluto pj joy with Dissolve(0.2)

                    pluto "Dogs!"
                
                "\"Woof!\"":

                    show pluto pj joy with Dissolve(0.2)

                    pluto "Woof!"
                
                "\"Cats.\"":

                    show pluto chopper with dissolve:
                        xalign 0.5
                        yalign 0.005
                        zoom 1.0

                    pluto "CATS?!?!?!"



        "Ask about the other planets." if fireplace_4:

        "Ask her opinion on humans." if fireplace_5:

        "Ask why she agreed to meet with us." if fireplace_6:

        "Ask about what she thinks about me." if fireplace_7:

        "Stay silent.":


