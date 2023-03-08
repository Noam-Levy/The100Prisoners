import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from listener import UIEventsListener

class View():

  def __init__(self):
    self._observers: list[UIEventsListener] = []
    self.root = ttk.Window(themename="superhero")
    self.root.title("The 100 Prisoners")
    photo = PhotoImage(file = './src/images/prison.png')
    self.root.iconphoto(False, photo)
    self.root.geometry("1200x600")
    self._drawMenuDrawer()
    self._drawBoxMatrix()

  def _drawMenuDrawer(self):
    pass
  
  def _drawBoxMatrix(self):
    matrix_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    label = ttk.Label(matrix_frame, text="Simulation viewer")
    label.pack()
    matrix_frame.pack()

  def run(self):
    self.root.mainloop()

  def attach(self, observer: UIEventsListener):
    self._observers.append(observer)

  def detach(self, observer: UIEventsListener):
    self._observers.remove(observer)

