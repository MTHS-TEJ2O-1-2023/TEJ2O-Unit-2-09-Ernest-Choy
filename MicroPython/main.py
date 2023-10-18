"""
Created by: Ernest
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from random import *
from microbit import *

rock_paper_scissors = -1
score_value = 0

display.clear
display.show(Image.HAPPY)

gesture = accelerometer.current_gesture()
if gesture == "shake":
    rock_paper_scissors = randint(0, 2)
    # if number is 0 show paper
    if rock_paper_scissors == 0:
        display.show(Image.SQUARE)
        sleep(5000)
        display.show(Image.HAPPY)

    # if number is 1 show rock
    if rock_paper_scissors == 1:
        display.show(Image.SQUARE_SMALL)
        sleep(5000)
        display.show(Image.HAPPY)

    # If number is 2 show scissor
    if rock_paper_scissors == 2:
        scissors = Image("99009:" "99090:" "99900:" "99090:" "99009:")
        display.show(scissors)
        sleep(5000)
        display.show(Image.HAPPY)

    if button_a.is_pressed():
        score_value = score_value + 1
        display.show(Image.YES)
        sleep(1000)
        display.clear()
        display.show(Image.HAPPY)

    if button_b.is_pressed():
        display.scroll("score is:" + str(score_value))
        display.show(Image.HAPPY)
