/* Copyright (c) 2020 MTHS All rights reserved
 * Created by Ernest
 * Created on: Oct 2023
 * This program ...
*/

basic.clearScreen()
basic.showIcon(IconNames.Happy)

let rockPaperScissors: number = -1
let scoreValue: number = 0

// on shake
input.onGesture(Gesture.Shake, function() {
  rockPaperScissors = randint(0, 2)

  if (rockPaperScissors === 0) {
    basic.showIcon(IconNames.Scissors)
  }

  if (rockPaperScissors === 1) {
    basic.showLeds(`
  # # # # #
  # . . . #
  # . . . #
  # . . . #
  # # # # #
  `)
  }

  if (rockPaperScissors === 2) {
    basic.showLeds(`
  . . . . .
  . # # # .
  . # # # .
  . # # # .
  . . . . .
  `)
  }

  basic.pause(1000)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
  })
// when A button is pressed
input.onButtonPressed(Button.A, function () {
  basic.showIcon(IconNames.Yes)
  scoreValue = scoreValue + 1
  basic.pause(1000)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})
// when B button is pressed
input.onButtonPressed(Button.B, function () {
  basic.clearScreen()
  basic.showString('Score is:' + (scoreValue).toString())
  basic.showIcon(IconNames.Happy)
})
