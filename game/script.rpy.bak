# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("Me")
define pluto = Character("Pluto", who_color="#ff75d8")
define theo = Character("Theo", who_color="#e68627")

# Declare player's affinites
default theo_aff = 0
default pluto_aff = 0

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

# The game starts here.
label start:

    # This starts the game with the intro1.rpy scene
    call intro1 from _call_intro1
    call intro2 from _call_intro2
    call pluto_date1
    call demo

    # This ends the game.
    return
