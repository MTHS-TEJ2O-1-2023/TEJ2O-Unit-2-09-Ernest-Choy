"""
Created by: Ernest
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from random import *
from microbit import *

score_value = 0

display.clear
display.show(Image.HAPPY)


while True:
    gesture = accelerometer.current_gesture()
    if accelerometer.was_gesture("shake"):
        rock_paper_scissors = randint(0, 2)

        # if number is 0 show scissors
        if rock_paper_scissors == 0:
            scissors = Image("99009:" "99090:" "99900:" "99090:" "99009:")
            display.show(scissors)
            sleep(2000)
            display.show(Image.HAPPY)

        # if number is 1 show rock
        if rock_paper_scissors == 1:
            rock = Image("00000:" "09990:" "09990:" "09990:" "00000:")
            display.show(rock)
            sleep(2000)
            display.show(Image.HAPPY)

        # If number is 2 show paper
        if rock_paper_scissors == 2:
            paper = Image("99999:" "90009:" "90009:" "90009:" "99999:")
            display.show(paper)
            sleep(2000)
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
