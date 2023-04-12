"""
@author: TODO: put your name here
"""

import turtle
import math
import time
import random
import tkinter as tk


# Question 1 ===================================================================


# TODO: Complete the __init__ method and write the spotify method in the
#  class below


class SpotGUI:
    """
    Draws a GUI window with a title label, a quit button, and a canvas
    with a green Dackdrop. The canvas responds to mouse clicks with the
    spotify callback function. The Quit button responds to clicks with the
    doQuit callback function.
    """

    def __init__(self):
        self.colorList = ["#FF0018", '#FFA52C', '#FFFF41', '#008018', '#0000F9',
                          '#86007D']
        self.mainWin = tk.Tk()
        self.mainWin.title("Spots!")

        self.titleLabel = tk.Label(self.mainWin, text="Spots!",
                                   font="Verdana 20 bold", relief=tk.GROOVE,
                                   justify=tk.CENTER, bd=5)
        self.titleLabel.grid(row=0, column=1, padx=10, pady=10)

        self.quitButton = tk.Button(self.mainWin, text="Quit",
                                    command=self.doQuit)
        self.quitButton.grid(row=0, column=0, padx=10, pady=10)
        # TODO: Add lines to the __init__ method here as directed in the
        #  assignment

    # TODO: Add a canvas callback method, spotify, here as directed in the
    #  assignment

    def go(self):
        self.mainWin.mainloop()

    def doQuit(self):
        """Callback function for the Quit button, closes the main window and
        ends the
        event loop."""
        self.mainWin.destroy()


# Question 2 ===================================================================

# TODO: Create the ColorPicker GUI class here; incorporate the makeTkColor
#  method from the assignment


# Question 3 ===================================================================


def merge(sListA, sListB):
    """Takes in two sorted lists, and combines them to create a new list
    where all values in order. For
    efficiency, we avoid calling the sort method: we want to do this with a
    minimum effort!"""
    if len(sListA) == 0:
        return sListB[:]
    elif len(sListB) == 0:
        return sListA[:]
    elif sListA[0] < sListB[0]:
        recurAnswer = merge(sListA[1:], sListB)
        recurAnswer.insert(0, sListA[0])
        return recurAnswer
    else:
        recurAnswer = merge(sListA, sListB[1:])
        recurAnswer.insert(0, sListB[0])
        return recurAnswer

# TODO: Create a happy robot diagram in hw6HappyRobot.md or upload a drawn
#  picture into your repository

# TODO: Add the unit test for the merge function in hw6Test.py


# Question 4 ===================================================================

# TODO: Define the function dragonOfEve here


def runDragonOfEve(startR, endR):
    """
    Takes two inputs, the starting number of recursive levels and the ending
    number of recursive levels, and it draws the Dragon of Eve fractal for
    each rep value, sleeping for 2 seconds between the end of one and the
    start of the next.
    """
    s = turtle.Screen()
    drawt = turtle.Turtle()
    textt = turtle.Turtle()
    for r in range(startR, endR):
        textt.reset()
        textt.hideturtle()
        textt.up()
        textt.color("green")
        textt.goto(-100, 300)
        drawt.reset()
        drawt.hideturtle()
        drawt.speed(0)
        drawt.up()
        drawt.backward(150)
        drawt.down()
        drawt.color('blue')

        dragonOfEve(drawt, 300, r)
        textt.write("Reps = " + str(r), False, font=("Verdana", 36, ""))
        time.sleep(2.0)
    # changes background color when all the drawing is done so you know it is
    # ready to quit
    s.bgcolor("lightsalmon")
    s.exitonclick()


# Sample runs ==================================================================
if __name__ == '__main__':
    print("Sample runs...")

    # Question 1 sample run
    # print("Question 1")
    # spot = SpotGUI()
    # spot.go()

    # Question 2 sample run
    # print("Question 2")
    # picker = ColorPicker()
    # picker.go()

    # Question 3 sample run
    # res0 = merge([1, 2, 5], [3, 4])
    # print(res0)
    # res1 = merge([1, 3, 5], [2, 4, 7, 8])
    # print(res1)
    # res2 = merge([55, 102, 503], [1, 2, 4, 60, 63, 110, 239, 488, 1005])
    # print(res2)

    # Question 4 sample run
    # print("Question 4")
    # runDragonOfEve(1, 7)
