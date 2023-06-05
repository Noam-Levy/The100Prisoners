from math import sqrt
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import PhotoImage
from constants import *
from views.subview import Subview

class BoxMatrix(Subview):
    def __init__(self, parent_frame, numberOfBoxes: ttk.IntVar):
        self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
        self.box_list = {} # hashes box labels for easy access to change state {box_number: (row, col, box_label, ticket_label)} 
        self.last_visited = -1 # keeps track of last visited box
        image_dir = os.path.join(os.getcwd(), 'images')
        self.unvisited_box = PhotoImage(file=os.path.join(image_dir, 'unvisited-box.png'))
        self.visited_box = PhotoImage(file=os.path.join(image_dir,'visited-box.png'))
        self.visiting_box = PhotoImage(file=os.path.join(image_dir,'prisoner-box.png'))
        self.numberOfBoxes = numberOfBoxes
        self.setNumberOfBoxes()
        
    def draw(self):
      self._clearFrame()
      ttk.Label(self.root, text="Simulation viewer", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
        .grid(row=0, columnspan=MAX_COLS)
      box_number, numberOfBoxes = 1, self.numberOfBoxes.get()
      for row in range(1, self.rows + 1):
        for col in range(self.cols):
          if (box_number > numberOfBoxes):
            break
          box_label = ttk.Label(self.root, image=self.unvisited_box, bootstyle=(LIGHT, INVERSE))
          ticket_label = ttk.Label(self.root, text="", font=(DEFAULT_FONT, DEFAULT_SUBHEADERS_SIZE), bootstyle=(SECONDARY, INVERSE))
          self.box_list[box_number] = (row, col, box_label, ticket_label) # add box label and ticket label to the map in a zero based numbering
          box_label.grid(row=row, column=col, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
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
      self.average_solution_label.config(text = "Average solution time: {:.06f} seconds".format(average_time))

    def drawVisitingBox(self, box_number):
      """
        Sets requested box image to show prisoner visiting and sets last visited box image to visited
        Parameters:
          box_number (int): referral box number
        Returns:
          None
      """     
      if self.last_visited >= 0:
        row, col, box_label, ticket_label = self.box_list[self.last_visited]
        box_label.config(image=self.visited_box)
        ticket_label.config(text=(box_number))
        ticket_label.grid(row=row, column=col)
       
      self.last_visited = box_number
      self.box_list[box_number][2].config(image=self.visiting_box)

    def resetBoxes(self):
      """
        Resets boxes image to unvisited
        Returns:
          None
      """
      self.last_visited = -1
      for _, _, box_label, ticket_label in self.box_list.values():
        box_label.config(image=self.unvisited_box)
        ticket_label.grid_remove()
      
    def _clearFrame(self):
      """
        Clears all widgets currently packed into the matrix frame
        Returns:
          None
      """
      self.box_list.clear()
      for widget in self.root.winfo_children():
        widget.destroy()
