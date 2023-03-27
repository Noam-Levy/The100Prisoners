from math import sqrt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import PhotoImage
from constants import *
from views.subview import Subview

class BoxMatrix(Subview):
    def __init__(self, parent_frame, numberOfBoxes: ttk.IntVar):
        self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
        self.box = PhotoImage(file='./src/images/open-box.png')
        self.visiting = PhotoImage(file='./src/images/prisoner-box.png')
        self.numberOfBoxes = numberOfBoxes
        self.setNumberOfBoxes()
        
    def draw(self):
      self._clearFrame()
      ttk.Label(self.root, text="Simulation viewer", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
        .grid(row=0, columnspan=MAX_COLS)
      box_label, numberOfBoxes = 1, self.numberOfBoxes.get()
      for row in range(1, self.rows + 1):
        for col in range(self.cols):
          if (box_label <= numberOfBoxes):
            ttk.Label(self.root, image=self.box, bootstyle=(LIGHT, INVERSE)).grid(row=row, column=col, padx=DEFAULT_PADDING)
            ttk.Label(self.root, text=box_label, bootstyle=(SECONDARY, INVERSE)).grid(row=row, column=col, sticky=S)
          box_label += 1
          
      self.average_solution_label = ttk.Label(self.root, text="Average solution time: ", font=(DEFAULT_FONT, DEFAULT_SUBHEADERS_SIZE), bootstyle=(LIGHT, INVERSE))
      self.average_solution_label.grid(row=self.rows + 1, columnspan=MAX_COLS, pady=DEFAULT_PADDING)
      return self.root
    
    def setNumberOfBoxes(self):
      numberOfBoxes = self.numberOfBoxes.get()
      self.rows = min(int(sqrt(numberOfBoxes)), MAX_ROWS)
      cols = (numberOfBoxes // self.rows) if (sqrt(numberOfBoxes)).is_integer() else (numberOfBoxes // self.rows) + 1
      self.cols = min(cols, MAX_COLS)

    def setAverageSimulationTime(self, average_time):
      self.average_solution_label.config(text = "Average solution time: {:.2f}".format(average_time))
  
    def _clearFrame(self):
       for widget in self.root.winfo_children():
          widget.destroy()
