import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from abstractSubject import AbstractSubject
from abstractObserver import AbstractObserver

class View(AbstractSubject):

  def __init__(self):
    self._observers: list[AbstractObserver] = []
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

  def attach(self, observer: AbstractObserver):
    self._observers.append(observer)

  def detach(self, observer: AbstractObserver):
    self._observers.remove(observer)
  
  def notify(self):
    for observer in self._observers:
      observer.update(self) # TODO: consider notify implementation.

if __name__ == "__main__":
  root = View()
  root.run()
