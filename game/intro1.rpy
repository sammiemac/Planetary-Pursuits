
# Intro scene
label intro1:

    scene bg black

    play music "audio/OST_Spaced_Out.mp3" volume 0.3

    "My body feels light, like a feather in the air. I try to observe my surroundings, but… there are none to observe. Everything is dark. Fear is the first thing that rises in my throat, but it quickly dissipates, leaving me empty, at peace."

    "I close my eyes, and I let the wind carry me. Then, I feel something warm, the sun’s heat, followed by a slight chill passing by, like a cool autumn breeze that tousles my hair. And then, I feel like I've landed, like the wind has placed me gingerly on the ground."

    "I open my eyes."

    scene bg space with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5

    "I look around me, my surroundings suddenly lit up by a vast universe. I'm standing on a comet as it flies through space, as if it's giving me a tour of the galaxy." 
    
    "I can see all the planets of our solar system; from Mars, to Jupiter, even Pluto. And of course, our Earth."
    
    "It's beautiful." 
    
    "A satellite passes by me, slowly beeping away."

    image satellite far:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 0.25
    show satellite far with dissolve

    play sound "audio/SFX_Satelite_Beep_Slow.mp3" volume 0.02

    "Satellite" "{i}*Beep. Beep. Beep.*{/i}"

    "{i}Why does that sound familiar?{/i}"

    image satellite close:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 0.5
    show satellite close with dissolve

    play sound "audio/SFX_Satelite_Beep_Med.mp3" volume 0.02

    "Satellite" "{i}*Beep! Beep! Beep!*{/i}"

    "{i}Now that I mention it, it isn’t passing by - at least, it isn’t anymore.{/i}"

    image satellite closer:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 1.5
    show satellite closer with dissolve

    play sound "audio/SFX_Satelite_Beep_Fast.mp3" volume 0.05

    "Satellite" "{i}*BEEP. BEEP. BEEP.*{/i}"

    "{i}Okay, that’s a little too close for comfo-!{/i}"

    image satellite closest:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 3.5
    show satellite closest with dissolve

    play sound "audio/SFX_Satelite_Beep_Fast.mp3" volume 0.1

    "Satellite" "{i}*BEEP! BEEP! BEEP!*{/i}"

    scene bg black

    stop music

    #play sound "SFX_crash.wav"

    mc "AHHHHHHHH--!!!"

    scene bg bedroom with fade

    "I sit up straight, a rush of cold hitting me immediately thanks to the sweat on the collar of my pajama shirt. I look to the source of beeping: it’s coming from my cell phone, laying there idly as it charges on my nightstand."

    play sound "audio/SFX_Alarm.mp3" volume 0.02

    #show phone

    mc "6:16… 16 minutes past the alarm…"

    menu:
        "\"Oh, well that’s better than usual.\"":
            "{i}Well, there’s no point in continuing to lay down here. Not like I can go back to bed with this sweat on my back.{/i}"

        "\"Huh? 16 minutes?!\"":
            "{i}I shouldn’t be late for work if I start getting ready now…{/i}"
    
    scene bg black with fade

    #play sound "SFX_change_clothes.wav"

    "After a quick shower to wash off that cold sweat, I put on the clothes I had set aside last night: the uniform for the new place I'm working at. I gathered up the rest of my belongings and checked myself out in the mirror."

    scene bg bedroom with fade

    play music "audio/OST_Retrograding_With_You.mp3" volume 0.1

    "{i}Alright, I'm as ready as I'll ever be. Uniform and everything...{/i}"

    "{i}Oh! Almost forgot my nametag.{/i}"

    "I pick up my nametag. It reads: "

    python:
        first_name = renpy.input("Please enter your first name.")
        first_name = first_name.strip() or "Taylor"

    python:
        last_name = renpy.input("Please enter your last name.")
        last_name = last_name.strip() or "Nova"

    menu:
        "Please select your pronouns."
        "He/Him/His":
            $ pronounChoice = 1
        "She/Her/Hers":
            $ pronounChoice = 2
        "They/Them/Theirs":
            $ pronouncHoice = 3

    "{i}[last_name[0]]., [first_name], Planetary Diplomat at the International Space Aeronautics and Astronomy Center.{/i}"

    menu:
        "Has a nice ring to it, doesn't it?":
            pass
        "It'll take some getting used to.":
            pass

    "I put the nametag on my chest. There. That should be it."

    "I look around, making a last-second sweep to make sure I have everything that I need on me. With everything seemingly taken care of, I head out."

    scene bg house outside with fade:
        zoom 0.5

    "Outside, a tall man sporting sunglasses, a black suit, and a full beard stands upright in front of a black sedan. Upon seeing me, he opens the passenger seat door and gestures for me to go in, his expression stoic."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "???" "[first_name] [last_name], right?"

    "I nod."

    show theo smile

    "???" "Theodore Guydon, at your service. I’ll be your secretary during your time at ISAAC."

    "{i}Secretary? I was told I would have a secretary, but I don’t remember being told I would have one that would drive me…{/i}"

    mc "It's good to meet you."

    "Theodore" "Pleasure's mine."

    stop music fadeout 2

    scene bg black with fade

    play sound "audio/SFX_Drive_Away_1.mp3" volume 0.1

    pause 2.0

    scene bg theo sedan with fade

    play music "audio/OST_Mr_Secretary_You_Have_A_Call.mp3" fadein 0.5 volume 0.1

    "I sigh and look outside the window, down at the water underneath the bridge we’re currently stuck on. I was wondering as to why the ride over was scheduled so early: the reason was right in front of me, manifested in the miles-long line of cars in our way."

    show theo neutral at right with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60
    
    "Theodore" "So, how’re you feelin’?"

    menu:
        "Nervous: \"I have no clue how this is going to go.\"":

            "Theodore" "That’s what they get for hiring an astronomy major and not a PR or an IR one."

        "Excited: \"I get to be one of the first people to talk to these… planets.\"":

            "Theodore" "I’m surprised, considering most of you Astronomy majors are more likely to get caught talking to a planet than a person."

        "Confident: \"One Small step for man, one big step, for my bank account.\"":

            "Theodore" "I’m surprised, considering most of you Astronomy majors are more likely to get caught talking to a planet than a person."

    "{i}Huh, didn’t expect a government-issued secretary to have so much sass.{/i}"

    menu:
        "\"You’d do best to stop talking to me like that, Guydon.\"":

            show theo smile

            "Theodore lets out a hearty laugh before grinning at me through the rearview mirror."

            "Theodore" "Hey, hey. Calm down. I’m just messing with you. No need for formalities, you can just call me Theo."

            $ calm_down = True

        "\"Yeah, and I wish some of that scholarship money went towards getting you a razor.\"":

            show theo smile

            "Theodore lets out a hearty laugh before grinning at me through the rearview mirror."

            "Theodore" "Hey, hey. Calm down. I’m just messing with you. No need for formalities, you can just call me Theo."

            $ calm_down = True

        "\"Sorry, did we get off on a bad foot?\"":

            show theo sweat

            "Theodore sighs, a bit of his bravado leaving him."

            "Theodore" "Hey, chin up, I’m just messing with you, boss. And you can call me Theo if that’s better for you."

            $ calm_down = False

        "\"Huh?\"":

            show theo sweat

            "Theodore sighs, a bit of his bravado leaving him."

            "Theodore" "Hey, chin up, I’m just messing with you, boss. And you can call me Theo if that’s better for you."

            $ calm_down = False


    "{i}Alright, Theo...{/i}"

    show theo neutral

    theo "I didn’t mean anything by the astronomy major stuff, by the way. Few of my friends studied the same thing, it’s the only reason I ended up working something like this."

    mc "What did you end up majoring in, then?"

    if calm_down:

        show theo smile

        theo "Not some bitch shit like astronomy, that’s what."

    else:
        
        theo "I bounced between a couple. Psychology, kinesiology, theatre. Landed on business management at the end of it all."

    theo "Either way, I ended up working for ISAAC. Buddy said a position opened up here, good paying. I barely fit the requirements and got the job anyways."

    hide theo with dissolve

    "I nod, still processing this introduction to my secretary. The last bit about not feeling qualified, though, I can relate to. I only got this job because I was on the team that worked on the technology that allowed us to bring these planets to life."

    "So it {i}is{/i} weird that I got this job. I’m just some amateur astronomer, fresh out of my studies, out of a project I only participated in for my senior thesis. I was contacted by ISAAC that summer, and here I am now."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Would you look at that? Traffic’s letting up."

    hide theo with dissolve

    "As Theo’s words pull me out of my thoughts and back into real life, I start to feel the car begin to move once more."

    stop music fadeout 2

    scene bg black with fade

    play sound "audio/SFX_Drive_Away_1_Cut.mp3" volume 0.1

    queue sound "audio/SFX_Car_Door_1.mp3" volume 0.1

    pause 3.0

    show bg isaac ext with fade

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Alright, boss. Here’s your stop."

    hide theo with dissolve

    "Ahead of me is the eleven story tall International Space Aeronautics and Astronomy Center. A shiver crawls down my spine. Whether that’s due to the imposing size of the building or the weight of my upcoming task slowly settling in is unclear."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "You head in first. I’ll get this thing parked and meet you in the lobby."

    hide theo with dissolve

    "I nod and leave the car, my eyes still on the building in front of me. It gets larger and larger as I cross the plaza in front of it and approach its entrance."