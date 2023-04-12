"""
File: sliderExample.py
Builds a simple GUI to show how to create Scale widgets (sliders) and how to access the value and use it
with a Scale callback function
"""


import tkinter as tk



class SliderDemo:
    """A simple demo showing how to set up a vertical slider and display the value"""

    def __init__(self):
        """Sets up the slider demo and a label to display the result"""

        self.boss = tk.Tk()
        self.boss['bg'] = 'ivory'
        self.slide = tk.Scale(self.boss, from_=100, to=0, orient=tk.VERTICAL, relief=tk.GROOVE, command=self.updateLabel)
        self.slide.grid(row=0, column=0, padx=10, pady=10)

        self.slideVal = tk.Label(self.boss, text = "", font="Arial 16", padx=10, pady=10,
                                 bg="lightblue", width=25)
        self.slideVal.grid(row=1, column=0, padx=10, pady=10)

    def go(self):
        """Sets the event loop going to run the GUI"""
        self.boss.mainloop()

    def updateLabel(self, currValue):
        """Given the current (new) value from the slider, this prints it, and its type, and then sets the label to
        display the current value."""
        print(currValue, type(currValue))
        self.slideVal['text'] = "Current slider value = " + currValue



sd = SliderDemo()
sd.go()
