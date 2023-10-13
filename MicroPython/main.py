"""
Created by: Ernest
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from random import *
from microbit import *


display.clear
display.show(Image.HAPPY)

rock_paper_scissors = -1
score_value = 0


while True:
    if accelerometer.was_gesture("shake"):
        rock_paper_scissors = randint(0, 2)

    if rock_paper_scissors == 0:
        rock = Image("99009:" "99090:" "99900:" "99090:" "99009:")
        display.show(rock)
        sleep(1000)
        display.show(Image.HAPPY)

    if rock_paper_scissors == 1:
        scissors = Image("00000:" "09990:" "09990:" "09990:" "00000:")
        display.show(scissors)
        sleep(1000)
        display.show(Image.HAPPY)

    if rock_paper_scissors == 2:
        paper = Image("99999:" "90009:" "90009:" "90009:" "99999:")
        display.show(paper)
        sleep(1000)
        display.show(Image.HAPPY)

    if button_a.is_pressed():
        score_value = score_value + 1
        display.show(Image.YES)
        sleep(1000)
        display.show(Image.HAPPY)

    if button_b.is_pressed():
        display.scroll("score is:" + str(score_value))
        display.show(Image.HAPPY)
