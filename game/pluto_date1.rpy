
# Pluto's first date, ice rink
label pluto_date1:

    scene bg black with dissolve

    #show bg pluto outside with dissolve

    centered "{b}{color=#ffffff}A few days later, around noon...{/b}{/color}"

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

        "Stay quiet.":

            "Deciding not to come off strong and seeing Pluto in a vulnerable state, I choose to let the topic of her choice in dress slide and focus on the task at hand."

            show pluto flustered

            "Pluto seems surprised to not be put down for her choice in fashion."

        "Make a joke.":

            mc "Wow, we’re going ice skating, not to a ball!"

            show pluto flustered

            "Just as I finish, Pluto is visibly devastated. A mixture of sadness and confusion on her face."

            show pluto shy

            pluto "I-I'm sorry, I'm not too familiar with Earth's customs yet, figures I'd mess up already."

            mc "Actually, I was just making a joke... I didn't mean to offend you."

            pluto "No, you're right, this dress doesn't look good on me in the first place. I don't know what I was thinking..."

            "{i}Well that was terrible, way to go me...{/i}"

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

    