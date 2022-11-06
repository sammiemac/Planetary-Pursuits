
# Intro scene
label intro1:

    #scene bg black

    "My body feels light, like a feather in the air. I try to observe my surroundings, but… there are none to observe. Everything is dark. Fear is the first thing that rises in my throat, but it quickly dissipates, leaving me empty, at peace."

    "I close my eyes, and I let the wind carry me. Then, I feel something warm, the sun’s heat, followed by a slight chill passing by, like a cool autumn breeze that tousles my hair. And then, I feel like I've landed, like the wind has placed me gingerly on the ground."

    "I open my eyes."

    scene bg space:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with dissolve

    "I look around me, my surroundings suddenly lit up by a vast universe. I'm standing on a comet as it flies through space, as if it's giving me a tour of the galaxy. I can see all the planets of our solar system; from Mars, to Jupiter, even Pluto. And of course, our Earth. It's beautiful. A satellite passes by me, slowly beeping away."

    "Satellite" "{i}*Beep. Beep. Beep.*{/i}"

    "{i}Why does that sound familiar?{/i}"

    "Satellite" "{i}*Beep! Beep! Beep!*{/i}"

    "{i}Now that I mention it, it isn’t passing by - at least, it isn’t anymore.{/i}"

    "Satellite" "{i}*BEEP. BEEP. BEEP.*{/i}"

    "{i}Okay, that’s a little too close for comfo-!{/i}"

    "Satellite" "{i}*BEEP! BEEP! BEEP!*{/i}"

    #scene bg black

    #scene bg bedroom with dissolve

    "I sit up straight, a rush of cold hitting me immediately thanks to the sweat on the collar of my pajama shirt. I look to the source of beeping: it’s coming from my cell phone, laying there idly as it charges on my nightstand."

    mc "6:16… 16 minutes past the alarm…"

    menu:
        "\"Oh, well that’s better than usual.\"":
            $ menu1_choice = True

        "\"Huh? 16 minutes?!\"":
            $ menu1_choice = False

    if menu1_choice:
        "{i}Well, there’s no point in continuing to lay down here. Not like I can go back to bed with this sweat on my back.{/i}"
    else:
        "{i}I shouldn’t be late for work if I start getting ready now…{/i}"

    #scene bg bedroom with dissolve

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

    #scene bg outside house

    "Outside, a tall man sporting sunglasses, a black suit, and a full beard stands upright in front of a black sedan. Upon seeing me, he opens the passenger seat door and gestures for me to go in, his expression stoic."

    show theo test:
        xalign 0.5
        yalign 0.5
        zoom 0.25
    play music "audio/theo-theme.mp3" fadein 2 volume 0.25

    "???" "[first_name] [last_name], right?"

    "I nod."

    "???" "Theodore Guydon, at your service. I’ll be your secretary during your time at ISAAC."

    "{i}Secretary? I was told I would have a secretary, but I don’t remember being told I would have one that would drive me…{/i}"

    mc "It's good to meet you."

    "Theodore" "Pleasure's mine."

    scene bg theo sedan

    "I sigh and look outside the window, down at the water underneath the bridge we’re currently stuck on. I was wondering as to why the ride over was scheduled so early: the reason was right in front of me, manifested in the miles-long line of cars in our way."

    show theo test:
        xalign 0.5
        yalign 0.5
        zoom 0.25
    "Theodore" "So, how’re you feelin’?"

    menu:
        "Nervous: \"I have no clue how this is going to go.\"":
            jump nervous
        "Excited: \"I get to be one of the first people to talk to these… planets.\"":
            jump excited_or_confident
        "Confident: \"One Small step for man, one big step, for my bank account.\"":
            jump excited_or_confident

    label nervous:
        "Theodore" "That’s what they get for hiring an astronomy major and not a PR or an IR one."

        jump menu2_done

    label excited_or_confident:
        "Theodore" "I’m surprised, considering most of you Astronomy majors are more likely to get caught talking to a planet than a person."

        jump menu2_done

    label menu2_done:
        "{i}Huh, didn’t expect a government-issued secretary to have so much sass.{/i}"

    menu:
        "\"You’d do best to stop talking to me like that, Guydon.\"":
            jump calm_down
        "\"Yeah, and I wish some of that scholarship money went towards getting you a razor.\"":
            jump calm_down
        "\"Sorry, did we get off on a bad foot?\"":
            jump chin_up
        "\"Huh?\"":
            jump chin_up

    label calm_down:
        "Theodore lets out a hearty laugh before grinning at me through the rearview mirror."

        "Theodore" "Hey, hey. Calm down. I’m just messing with you. No need for formalities, you can just call me Theo."

        $ menu3_choice = True

        jump menu3_done

    label chin_up:
        "Theodore sighs, a bit of his bravado leaving him."

        "Theodore" "Hey, chin up, I’m just messing with you, boss. And you can call me Theo if that’s better for you."

        $ menu3_choice = False

        jump menu3_done

    label menu3_done:
        "{i}Alright, Theo...{/i}"

    theo "I didn’t mean anything by the astronomy major stuff, by the way. Few of my friends studied the same thing, it’s the only reason I ended up working something like this."

    mc "What did you end up majoring in, then?"

    if menu3_choice:
        theo "Not some bitch shit like astronomy, that’s what."
    else:
        theo "I bounced between a couple. Psychology, kinesiology, theatre. Landed on business management at the end of it all."

    theo "Either way, I ended up working for ISAAC. Buddy said a position opened up here, good paying. I barely fit the requirements and got the job anyways."

    "I nod, still processing this introduction to my secretary. The last bit about not feeling qualified, though, I can relate to. I only got this job because I was on the team that worked on the technology that allowed us to bring these planets to life."

    "So it {i}is{/i} weird that I got this job. I’m just some amateur astronomer, fresh out of my studies, out of a project I only participated in for my senior thesis. I was contacted by ISAAC that summer, and here I am now."

    theo "Would you look at that? Traffic’s letting up."

    "As Theo’s words pull me out of my thoughts and back into real life, I start to feel the car begin to move once more."
