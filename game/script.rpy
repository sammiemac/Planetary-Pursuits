# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("Me")
define pluto = Character("Pluto", who_color="#ff75d8")
define theo = Character("Theo")


# The game starts here.
label start:

    # Leaving this here as a simple guide to how to get started on implementing these scenes.
    # We will remove them when we're more comfortable with programming in Ren'Py
    # - Sam

    # This shows a background.
    scene bg space:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with dissolve

    # This shows a character sprite.
    show pluto test

    # These display lines of dialogue.
    pluto "You've created a new Ren'Py game."

    pluto "Once you add a story, pictures, and music, you can release it to the world!"

    "Hello world!"

    # This calls the intro.rpy scene
    call intro

    # This ends the game.
    return
