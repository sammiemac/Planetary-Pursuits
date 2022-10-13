# Intro scene
label intro:

    # TODO: Implement the intro scene

    # TODO: Section one, from "MAIN CHARACTER (MC)" to "INT. MC'S HOME - BEDROOM - MORNING"

    # TODO: Section two, from "INT. MC’S HOME - BEDROOM - MORNING" to "INT. THEGUY’S SEDAN"
    "{i}Alright, I'm as ready as I'll ever be. Uniform and everything...{/i}"

    "{i}Oh! Almost forgot my nametag.{/i}"

    "I pick up my nametag. It reads: "

    python:
        first_name = renpy.input("What's your first name?")
        first_name = first_name.strip() or "Taylor"

    python:
        last_name = renpy.input("What's your last name?")
        last_name = last_name.strip() or "Nova"

    "{i}[last_name[0]]., [first_name], Planetary Diplomat at the International Space Aeronautics and Astronomy Center.{/i}"

    menu:
        "Has a nice ring to it, doesn't it?":
            pass
        "It'll take some getting used to.":
            pass

    "I put the nametag on my chest. There. That should be it."

    "I look around, making a last-second sweep to make sure I have everything that I need on me. With everything seemingly taken care of, I head out."

    #scene outside mc house
    "Outside, a tall man sporting sunglasses, a black suit, and a full beard stands upright in front of a black sedan. Upon seeing me, he opens the passenger seat door and gestures for me to go in, his expression stoic."

    "???" "[first_name] [last_name], right?"

    "I nod."

    "???" "Theodore Guydon, at your service. I’ll be your secretary during your time at ISAAC."

    "{i}Secretary? I was told I would have a secretary, but I don’t remember being told I would have one that would drive me…{/i}"

    mc "It's good to meet you."

    "Theodore" "Pleasure's mine."

    # TODO: Section three, from "INT. THEGUY’S SEDAN" to "EXT. ISAAC BUILDING - MORNING"
