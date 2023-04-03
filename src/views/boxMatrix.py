from math import sqrt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import PhotoImage
from constants import *
from views.subview import Subview

class BoxMatrix(Subview):
    def __init__(self, parent_frame, numberOfBoxes: ttk.IntVar):
        self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
        self.box_list = {} # hashes box labels for easy access to change state {box_number: ttk.label} 
        self.last_visited = -1 # keeps track of last visited box
        self.unvisited_box = PhotoImage(file='./src/images/unvisited-box.png')
        self.visited_box = PhotoImage(file='./src/images/visited-box.png')
        self.visiting_box = PhotoImage(file='./src/images/prisoner-box.png')
        self.numberOfBoxes = numberOfBoxes
        self.setNumberOfBoxes()
        
    def draw(self):
      self._clearFrame()
      ttk.Label(self.root, text="Simulation viewer", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
        .grid(row=0, columnspan=MAX_COLS)
      box_number, numberOfBoxes = 1, self.numberOfBoxes.get()
      for row in range(1, self.rows + 1):
        for col in range(self.cols):
          if (box_number <= numberOfBoxes):
            box_label = ttk.Label(self.root, image=self.unvisited_box, bootstyle=(LIGHT, INVERSE))
            self.box_list[box_number - 1] = box_label # adds box label to the map in a zero based numbering
            box_label.grid(row=row, column=col, padx=DEFAULT_PADDING)
            ttk.Label(self.root, text=box_number, bootstyle=(SECONDARY, INVERSE)).grid(row=row, column=col, sticky=S)
          box_number += 1
          
      self.average_solution_label = ttk.Label(self.root, text="Average solution time: ", font=(DEFAULT_FONT, DEFAULT_SUBHEADERS_SIZE), bootstyle=(LIGHT, INVERSE))
      self.average_solution_label.grid(row=self.rows + 1, columnspan=MAX_COLS, pady=DEFAULT_PADDING)
      return self.root
    
    def setNumberOfBoxes(self):
      """
         Setter function for total number boxes (which is also the total number of prisoners)\n
         the function determines how many rows and columns should be drawn
         Returns:
            None
      """
      numberOfBoxes = self.numberOfBoxes.get()
      self.rows = min(int(sqrt(numberOfBoxes)), MAX_ROWS)
      cols = (numberOfBoxes // self.rows) if (sqrt(numberOfBoxes)).is_integer() else (numberOfBoxes // self.rows) + 1
      self.cols = min(cols, MAX_COLS)

    def setAverageSimulationTime(self, average_time):
      """
         Setter function for average solution time label
         Returns:
            None
      """
      self.average_solution_label.config(text = "Average solution time: {:.2f} seconds".format(average_time))

    def drawVisitingBox(self, box_number):
      """
        Sets requested box image to show prisoner visiting and sets last visited box image to visited
        Parameters:
          box_number (int): referral box number
        Returns:
          None
      """
      if not box_number in self.box_list:
        return
      
      if self.last_visited >= 0:
        self.box_list[self.last_visited].config(image=self.visited_box)
      self.last_visited = box_number
      self.box_list[box_number].config(image=self.visiting_box)

    def resetBoxes(self):
      """
        Resets boxes image to unvisited
        Returns:
          None
      """
      for label in self.box_list.values():
        label.config(image=self.unvisited_box)
      
    def _clearFrame(self):
      """
        Clears all widgets currently packed into the matrix frame
        Returns:
          None
      """
      self.box_list.clear()
      for widget in self.root.winfo_children():
        widget.destroy()
