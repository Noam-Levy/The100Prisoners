import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from constants import *
from views.subview import Subview

class PrisonerDataView(Subview):
    def __init__(self, parent_frame):
        self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
        self.prisoner_number_label = ttk.Label(self.root, text = "Prisoner Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
        self.box_number_label = ttk.Label(self.root, text = "Box Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
        self.found_number_label = ttk.Label(self.root, text = "Found Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
        self.guess_number_label = ttk.Label(self.root, text = "Number of Guesses:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
        self.prisoner_image = PhotoImage(file='./src/images/prisoner.png')
        self.prisoner_number = ttk.IntVar()
        self.box_number = ttk.IntVar()
        self.found_number = ttk.IntVar()
        self.total_guesses = ttk.IntVar(value=1)

    def draw(self):
      img_label = ttk.Label(self.root, image=self.prisoner_image, bootstyle=(LIGHT, INVERSE))
      img_label.grid(row=0, column=0, rowspan=4)
      self.prisoner_number_label.grid(row=0, column=1, sticky=W)
      self.box_number_label.grid(row=1, column=1, sticky=W)
      self.found_number_label.grid(row=2, column=1, sticky=W)
      self.guess_number_label.grid(row=3, column=1, sticky=W)
            
      return self.root
    
    def setPrisonerNumber(self, number):
      """
         Setter function for prisoner number
         Returns:
            None
      """
      self.prisoner_number.set(number)
      self.prisoner_number_label.config(text=f"Prisoner Number: {self.prisoner_number.get()}")
      
    def setBoxNumber(self, number):
      """
         Setter function for box number
         Returns:
            None
      """
      self.box_number.set(number)
      self.box_number_label.config(text=f"Box Number: {self.box_number.get()}")
    
    def setFoundNumber(self, number):
      """
         Setter function for found box ticket number
         Returns:
            None
      """
      self.found_number.set(number)
      self.found_number_label.config(text=f"Found Number: {self.found_number.get()}")
    
    def incrementGuessNumber(self):
      """
         Setter function for total number of guesses
         Returns:
            None
      """
      self.total_guesses.set(self.total_guesses.get() + 1)
      self.guess_number_label.config(text=f"Number of Guesses: {self.total_guesses.get()}")

    def resetGuessNumber(self):
      """
         Resets total number of guesses to 1
         Returns:
            None
      """
      self.total_guesses.set(1)
      self.guess_number_label.config(text=f"Number of Guesses: {self.total_guesses.get()}")

    def reset(self):
      self.prisoner_number_label.config(text="Prisoner Number:")
      self.box_number_label.config(text="Box Number:")
      self.found_number_label.config(text="Found Number:")
      self.guess_number_label.config(text="Number of Guesses:")
       
      
