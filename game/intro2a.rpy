
# Intro scene part 2, learn more about the device
label intro2a:
    
    mc "Did you want to learn more about it?"

    show pluto flustered:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "Pluto’s looks towards me as I ask that."

    show pluto shy

    pluto "Oh, I... well, I mean, only if you want to... I probably wouldn’t understand it anyways..."

    mc "I mean, it makes sense that you’re curious about it. And it just looks scary. Once you know more about it, all you have to do is go through the motions."
    
    "Pluto hesitates for a second before looking to the latch under the glass case."

    pluto "That one looks... Important."

    mc "That’s the emergency power off switch. Starting up the machine needs like, a lot of power, and there is a small, small chance of something lighting ablaze or blowing up."

    show pluto flustered

    "Already anticipating that I was about to worry her, I continue on to the reassuring part."

    mc "But it’ll notify us if things get too hot. And that’s why the switch is there, so if things get bad, we flip it. Now that the device has already booted up, it shouldn’t reach any temperature like that."

    show pluto neutral

    pluto "That’s... good."

    "She waddles around, eventually stopping at a panel of flashing lights."

    pluto "Are these supposed to be stars? I-I know that you guys, well... Earth told me that some of you guys can’t see the stars. So it would make sense if... S-sorry, nevermind..."

    menu:
        "\"No, go on.\"":

            show pluto shy

            "Pluto inhales sharply before quickly exhaling again, her face flushed."

            pluto "O-Oh, I... I was just going to say that, that if you guys couldn’t see the stars, it would make sense if you like... you know, made your own stars."

            "She looks back down at her feet as the last words leave her lips."

            mc "I guess you could call them that, yeah. I don’t think anyone sees them as actual stars, though. Stuff like that actually makes it harder to see the stars, you know?"

            "I gesture to the panel she was just looking at."

            mc "Things like that don’t actually make it harder. But bigger lights, like street lamps, outdoor lights, that kind of thing. Just like how we can’t see the stars during the day because of the sun, too much light at night does the same thing."

        "\"Well, it depends on the night...\"":

            "Pluto sighs, seemingly with relief, as I take over the conversation yet again."

            mc "We have a lot of lights around here. Not... stars, but street lights, lamps, electric billboards and all that. I don’t think anyone sees them as stars, though. In fact, the lights we have on Earth make it a lot harder to see the actual stars."

            "Pluto frowns, but doesn’t say anything."

            mc "Yeah, nowadays you have to go to a park. Or a forest, or the mountains. If you want to see the stars, that is. Or else there’s too much light, which kind of blocks out the stars."

    show pluto neutral

    pluto "Oh... But those lights, they make Earth look so beautiful, don’t they? Only Jupiter doesn’t like how Earth looks, and Jupiter just hates everything..."

    "I nod before getting an idea in my head, turning on like a lightbulb."

    mc "Well, we could go and see Earth right now. You’re on its surface, anyways, so might as well, don’t you think?"

    show pluto shy

    pluto "O-oh, well, I uh... Jupiter said that this was just going to be a short introduction... A-and Neptune, she wanted to stop by too, so maybe not now... I should be free by my next rotation, though..."

    "{i}Pluto’s rotation, that must be her way of saying a day in her time.{/i}"

    mc "How does four-fifths of a rotation from now sound to you? I’ll... send a message out to you and let you in with the Astroplacation device when it’s time."

    "{i}That should be about noon, five days from now.{/i}"

    show pluto flustered

    "She appears to think for a bit before looking back at me."

    show pluto neutral

    pluto "Okay. I-I can do that. Yeah."

    mc "Cool."

    "There’s a moment of silence."

    show pluto shy

    pluto "I-I think that you have to do something with the machine to send me back..."

    mc "Y-yeah, you’re right..."

    "Pluto steps aside as I flip a couple of smaller switches and type a couple of sequences into the number pad."

    show pluto neutral

    pluto "See you soon..."

    mc "You too!"

    hide pluto with dissolve

    "The machine roars to life as I say my farewell, drowning out my words a little bit. Eventually, the roar becomes a drone, then the drone becomes a hum, and then the hum becomes silence."

    "I look around. I’m alone in the room."

    "That is, until..."

    show theo smile with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "How’d it go, boss?"

    "Theo opens the door to the room with a smile. He’s got a journal in his hand, where I can see bullet points but can’t make out any of the words that follow them."

    mc "Uh, alright. We’ve got something more... Professional, scheduled in five days. Noon."

    show theo neutral

    "I’m met with a raised eyebrow and a gesture for me to follow as Theo starts walking towards the elevator."

    scene bg isaac hallway with dissolve

    show theo sweat with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "You know I have to be with you for that, right?"

    menu:
        "\"I forgot, to be honest.\"":
            pass
        "\"It’ll be fine.\"":
            pass
    
    "Theo sighs as we enter the elevator. It seems like all the scans were only to get in, as all he has to do this time is press the ground floor button and the elevator doors close."

    show theo neutral

    theo "I’ll just... do my best to not get in your way, alright? Do your thing. Sounded like you did a fine job here already, though. Don’t think I had any expectations, but you surpassed any I would have had."

    mc "Thanks."

    theo "Just calling what I’m seeing."

    hide theo with dissolve

    "We’re back at the lobby when the elevator doors open again, and I’m left alone with my thoughts as Theo goes to fetch the car to bring me back home."

    call pluto_date1