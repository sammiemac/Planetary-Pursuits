
# Intro scene part 2
label intro2:
    
    #show bg isaac int with dissolve

    play music "audio/OST_Retrograding_With_You.mp3" volume 0.1

    "{i}So, here I am, the lobby…{/i}"

    "It’s not the first time I’ve been here. I remember coming here and taking an elevator up to the second or third floor, answering some questions from an interviewer in some room, and then taking my leave."
    
    "The whole process was a blur to me, so it was even more bewildering when the acceptance email came in a few weeks later."

    "{i}No way they take in some kid just based on the fact that they worked on the Astroplacation Project…{/i}"

    "The lobby is the same as it was before: clean, spacious, and well air-conditioned. I appreciated that last quality when I came here in the summer, but now that it’s fall it’s much less welcoming."

    show theo sweat with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "God damn, this lobby is cold."

    hide theo with dissolve

    "He rubs his arms then gestures for me to follow him. We eventually reach an elevator and head inside, where he presses a series of numbers on the number pad, one that appears to have the numbers 1-12, excluding the number 8."
    
    "Two glass panels next to the number pad reveal themselves, as Theo lays his hand on one and lifts his sunglasses to look directly into the other. A red light scans both as the elevator doors close shut."

    "Elevator" "Floor 8."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Planets ain’t waitin’ for us or anything– Though, uh, as much as I wish I didn’t need to say it right now, RWJ hopes to keep everything on schedule."

    mc "Huh?"

    "The response is involuntary as the news steals the air from my lungs."

    "{i}When I saw “President” in the email communications, I thought they meant the President of ISAAC, not Renee Whitaker Jiang, President of the United States…{/i}"

    show theo sweat

    theo "Yeah. I’m, uh, legally obligated to remind you of that part. I’ll be giving her progress reports, that sort of thing."

    menu:
        "\"Got it. Anything else?\"":

            show theo neutral

            theo "Nothing I’m legally bound to say. We’re kind of charting new territory here, so it’s up to you to set the standard. Just... handle it how you think you should. ISAAC didn’t choose you for nothin’."

        "\"Honestly, Theo? I had no idea...\"":

            show theo neutral

            theo "I get it. Government communications are a lot vaguer than I thought they would be going into this job. I guess this whole communicating with planets thing is... a shot in the dark for everyone involved."

        "{i}Stay silent.{/i}":

            mc "..."
    
    "It’s silent for the rest of the elevator ride."
    
    scene bg isaac hallway with dissolve

    "The doors in front of us slide open. Theo walks out and makes a sharp right turn, walking until he reaches a door close to the end of the hallway." 
    
    "There’s a slightly rusted metal \"52\" on the door, flush with its mahogany wood surface. Theo slaps his hand on the door and looks towards me."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Right here."

    "As he takes his hand off the door, he reaches into his pocket and pulls out a key before holding it out to me."

    show theo smile

    theo "Honor’s all yours."

    "I nod and take the keys out of his hand. It’s made of a gray metal, dully gleaming against the hallway’s white lights."

    "{i}Well, here goes nothing.{/i}"

    play sound "<from 0 to 2.5>audio/SFX_click.wav" volume 0.05

    scene bg control room with dissolve

    "I enter the room to a small booth, half of which is taken up by part of the device I remember spending so much of my later college years working on." 
    
    "A few swivel chairs are dotted along the panels and switches: they seemed to be under the assumption that it would need multiple people to run, given the machine’s size."

    show theo neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Here it is."

    "I nod, my eyes still on the machine in front of me. It’s strange to see it in a setting like this, but I can already tell operating it will be a breeze."

    show theo sweat

    theo "You’re looking at this like it’s a beauty but it just looks like something out of some sci-fi video game to me."

    show theo smile

    "Theo crosses his arms and chuckles. However, as I start reaching for some of the device’s implements, his expression becomes more stoic."

    show theo neutral

    theo "Once you start that thing up, I’m legally obligated to leave the room, as to not affect your communications with the planets. So if you’ve got any burning questions, hit me with them."

    $ already_asked_1 = False
    $ already_asked_2 = False
    $ already_asked_3 = False
    $ already_asked_4 = False

    label theo_question:

        menu:
            "\"Any specific way I should handle things?\"" if not already_asked_1:

                show theo smile
                
                "Theo laughs."

                theo "If there was an agenda, I would have told you by now. Just... be yourself. As Disney as that fucking sounds. Just don’t immediately tank our relations with them and we should be in the clear."

                show theo neutral

                theo "Anything else?"

                $ already_asked_1 = True

                jump theo_question

            "\"How long should I maintain communication with them?\"" if not already_asked_2:

                theo "As long as you feel necessary, boss. I think the time slot is pretty much until 8 tonight, so we’ve pretty much got the whole day ahead of us."

                theo "Anything else?"

                $ already_asked_2 = True

                jump theo_question

            "\"Am I going to be talking to every planet?\"" if not already_asked_3:

                theo "We issued an initial contact message to all of them not long ago, but the only ones who you’ll be speaking with are the “ones willing”, according to your old boss. Whatever that means."

                theo "Anything else?"

                $ already_asked_3 = True

                jump theo_question
                
            "\"Was that suit of yours government-issued or did you have to buy it?\"" if not already_asked_4:

                "Theo thinks for a second, as if trying to discern how much he should divulge."

                theo "First one was government issued, but I ripped it after a night with your mom."

                "His stoic expression becomes a smirk, then a hearty laugh."

                show theo smile

                theo "It’s a work expense, so it’s basically given to me. Anything else?"

                $ already_asked_4 = True

                show theo neutral

                jump theo_question

            "\"I don’t have anything else.\"":

                theo "Then break a leg, boss."

    hide theo with dissolve

    #A 33% chance of the Jupiter encounter happening.
    $ jupiter_encounter = renpy.random.randint(1, 3)
    if jupiter_encounter is 1:
        $ meet_jupiter = True
        call jupiter

    "With that, Theo leaves, and I’m alone in the booth. With Theo gone, the room is completely silent, aside from the hum of the lights above my head."

    "There’s nothing left to do but get the Astroplacation device running."

    stop music fadeout 2

    "It comes naturally to me, just like how the Professor taught me."

    "{i}Power switch on, check levels, make sure the machine is emitting a quiet hum before doing anything else. Activate the location transmitter, isolation levels are okay, take into account the Earth’s magnetic field in our calculations...{/i}"

    "It’s like I’m that college kid again. I guess I always was, but I feel even more so now that I’m getting back in the groove of things. Maybe I’m more like the Professor now. In charge. I know what I’m doing. And now I get to make money doing it!"

    "{i}What?{/i}"

    "{i}Oh no. That light shouldn’t be red. That wave should be less violent, the levels here are just completely off…{/i}"

    "{i}Sirens. Oh, those sirens, that... that might be the worst thing that could happen...{/i}"

    "I reach for the emergency shutdown latch and flip it. However, the machine’s initially stable humming begins to heighten, destabilizing until…"

    "Calm. Levels return to normal. The intercom to the far left of the device lights up, as if everything was going as planned. I run over to the chair closest to it and put my lips up to the microphone next to the intercom."

    mc "Hello? This is [first_name] [last_name] speaking from the International Space Aeronautics and Astronomy center, speaking. "

    "Female Voice" ". . . hi."

    "The voice is unfamiliar, and doesn’t even come from the intercom. Either way, I flinch and fall backwards in my chair with a {i}THUMP{/i}."

    "Looking down on me is a brown-skinned girl, both of her hands cupped over her face. Above those hands are a pair of bespectacled, widened gray eyes, along with a mop of gray hair topped by a heart-shaped cowlick."

    play music "audio/OST_A_Thawing_Heart.mp3" fadein 0.5 volume 0.07

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "Female Stranger" "Oh my, I’m so sorry, here, let me…"

    "The stranger appears to look around panicked before she steps back and extends a hand sheepishly."

    menu:
        "Take her hand.":

            "Despite appearing to be just short of five feet tall, the stranger’s grip is firm. It’s icy cold as well, far colder than the unheated room around me."

        "Get up yourself.":

            "The stranger moves her extended hand behind her back and shies away as I get up."
    
    show pluto shy

    "Female Stranger" "Sorry about that, I-I didn’t mean for that to happen..."

    mc "Don’t worry about it."

    "{i}This must be what the Professor was talking about when referring to the planet’s persona, that the machine would form one relating to their nature or our perception of it. I didn’t realize it would create a whole person, though...{/i}"

    mc "You must be..."

    menu:
        "\"Mercury.\"":

            "Female Stranger" "N-no, that’s... that’s not it… I’m Pluto."

        "\"Jupiter.\"":
            
            "The stranger shakes her head."

            "Female Stranger" "Ha, I’m not nearly as... as big, or loud enough to be Jupiter. I’m Pluto."

        "\"Uranus.\"":

            "Female Stranger" "N-no, that’s... that’s not it… I’m Pluto."

        "\"Pluto.\"":

            show pluto joy

            "The stranger nods, a small smile gracing her lips."

            pluto "Mhm."

    show pluto neutral

    "She looks down at her feet and does a little bow."

    pluto "It’s... good to meet you."

    mc "It’s nice to meet you, too, Pluto."

    pluto "..."

    show pluto shy

    "Pluto starts glancing around a bit, silently taking in her surroundings."

    mc "So you’re... the actual planet Pluto. Right?"

    show pluto neutral

    "She nods, her focus returning to me. There’s a bout of silence before she goes to pick up the chair that I just fell out of. As she moves to do that, there’s a knock at the door."

    hide pluto with dissolve

    theo "Boss, you good?"

    show pluto cry with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "Pluto flinches away from the doorway as I look to respond."

    mc "Y-yeah, I’m good!"

    hide pluto with dissolve

    theo "Alright, just checkin’ in. Heard some noise and was worried something happened."

    show pluto cry with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    "Meanwhile, Pluto lowers her voice to a whisper."

    pluto "Wh-who’s that?"

    menu:
        "A friend of mine.":

            show pluto neutral

            "Pluto nods, seeming a bit relieved."

        "My secretary.":

            show pluto shy

            "Pluto nods."

        "Just my lackey.":

            show pluto flustered

            "Pluto looks to me, then towards the door, then back to me, her glasses slightly fogged."
    
    pluto "O-ok..."

    hide pluto with dissolve

    "From what I remember from my training sessions with the Professor, these personas were personalities, ones I had to befriend. This would make their natural resources more accessible and possibly open up the avenue for inhabitation."

    "If what Theo said was true, though, Pluto was the only planet initially open to this idea of communication. Which sounds plain inconvenient. Do I have to introduce myself to every planet one by one? A group setting might have been more... easy to navigate."

    "This can’t be how this is supposed to go."

    show pluto neutral with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    mc "Hey, Pluto, just... give me a second, okay? And don’t... don’t touch anything in here."

    show pluto shy

    pluto "Oh, o-okay."

    hide pluto with dissolve

    "I open the door just a crack and slip out as quickly as I can."

    scene bg isaac hallway with dissolve

    show theo smile with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    theo "Chocolate or maple?"

    "Right next to the doorway is Theo, leaning on the wall holding out two bar-shaped donuts."

    menu:
        "\"Chocolate.\"":

            "Theo hands me my choice of donut, then takes a bite of the one remaining."

            theo "You know, these things are actually called long johns. I  never knew that. Anyways, you need something?"

            $ theo_donut = True

        "\"Maple.\"":

            "Theo hands me my choice of donut, then takes a bite of the one remaining."
            
            theo "You know, these things are actually called long johns. I  never knew that. Anyways, you need something?"

            $ theo_donut = True

        "\"Theo, we need to talk.\"":

            show theo sweat

            "Theo sighs, lowering the donuts as if the offer was now rescinded."

            theo "What’s goin’ on?"

            $ theo_donut = False

    mc "So the planet’s like, an actual person."

    if theo_donut:

        show theo neutral

        "Theo swallows the piece of donut in his mouth before nodding."

    else: 

        show theo neutral

        "Theo looks at me blankly before wrapping one of the donuts in a napkin and pocketing it."

    theo "Like, a physical, real human? And this isn’t supposed to happen, right?"

    mc "I mean, I guess this is my first time going through with the entire procedure, I just didn’t expect a whole person to materialize in front of me..."

    "Theo takes a bite of the remaining donut before pulling a journal out of his bag and beginning to write."

    theo "It’s just one person, then? Which planet?"

    mc "Pluto."

    "He gives me another affirmative nod, writing as he replies."

    theo "Mission probably doesn’t change from here. Communicate, build rapport. You’re the boss, though. So you take care of it how you will."

    menu:
        "\"Got it.\"":

            pass

        "\"Any advice?\"":

            "Theo shrugs."
            
            theo "You said they’re a person, right? Just like one?"

            "I nod."

            theo "Then just treat them like you would any other. Right? It’s not like we’ve got rules telling you what to do."

            "He’s not wrong. Pluto seemed pretty... human. Or, at least, if I just met her on the street, I might have just mistook her for a random college student."

        "\"Can I still have the donut?\"" if not theo_donut:

            show theo smile

            theo "Sure."
            
            "Theo hands me the remaining donut, the chocolate one."
    
    mc "Thank you Theo."

    theo "Anytime."

    hide theo with dissolve

    "With that, I go back into Room 52."

    scene bg control room with dissolve

    "As I enter, I’m met with Pluto sitting down in one of the chairs. Upon closer inspection, she’s actually... in a sitting position, floating just an inch or two above the chair."

    mc "Sorry about that- are you floating?"

    "She falls back down into the chair, a brief squeaking sound coming out as she lands. Whether it was from her or the chair was unclear."

    show pluto flustered with dissolve:
        xalign 0.5
        yalign 0.005
        zoom 0.60

    pluto "O-Oh! Sorry, I thought you said not to touch anything, so I..."

    mc "No, it’s okay, I more meant all the tech stuff right there."

    "I gesture to the Astroplacation device next to her. It still hums ever so slightly."

    show pluto shy

    pluto "Oh, I-I’m sorry, I probably should have got that..."

    mc "It’s fine, it’s not like there was any way you would have known if I didn’t tell you."

    "Pluto nods, whether that’s for me or herself, I’m not sure. She goes on to look at the Astroplacation device, this time from a couple feet’s distance."

    menu:
        "Ask if she wants to learn more about the device.":
            call intro2a from _call_intro2a
        "Ask how she could levitate.":
            call intro2b from _call_intro2b