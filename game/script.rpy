# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("Me")
define pluto = Character("Pluto", who_color="#ff75d8")
define theo = Character("Theo")

python:
# TODO: Implement hashmap/dictionary for MC's pronouns
# Code: Choice 1 when prompted by the game would designate pronouns as he/him/his, 2 would be she/her/hers, 3 would be they/them/their.
# Set pronoun choice to either 1 2 or 3 whenever the prompt comes up mid game.
# Refer to pronouns in the script using this syntax: subjectPronouns['choice number']
    pronounChoice = 0
    subjectPronouns = {1: he, 2: she, 3: they}
    objectPronouns = {1: him, 2: her, 3: them}
    possPronouns = {1: his, 2: hers, 3: theirs}
    possAdjectives = {1: his, 2: hers, 3: their}
# TODO: Implement variables for characters' affinities towards the MC
    plutoAff = 0
    theoAff = 0
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
    call intro1

    # This ends the game.
    return
