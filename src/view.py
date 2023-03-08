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
    settings_frame = ttk.Frame(self.root, bootstyle = "light")
    statistics_label = ttk.Label(settings_frame,text = "Statistics", font=("Helvetica", 15),bootstyle = "inverse light")

    prisonerNum_label = ttk.Label(settings_frame,text = "Prisoner Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    boxNum_label = ttk.Label(settings_frame,text = "Box Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    foundNum_label = ttk.Label(settings_frame,text = "Found Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    guessNum_label = ttk.Label(settings_frame,text = "Number of Guesses :", font=("Helvetica", 10),bootstyle = "inverse light")

    setting_label = ttk.Label(settings_frame,text = "Settings", font=("Helvetica", 15),bootstyle = "inverse light")
    priNum_label = ttk.Label(settings_frame,text = "# of prisoners", font=("Helvetica", 10),bootstyle = "inverse light")
    simNum_label = ttk.Label(settings_frame,text = "# of simulations", font=("Helvetica", 10),bootstyle = "inverse light")
    random_label = ttk.Label(settings_frame,text = "select randomly", font=("Helvetica", 10),bootstyle = "inverse light")
    strategy_label = ttk.Label(settings_frame,text = "apply strategy", font=("Helvetica", 10),bootstyle = "inverse light")

    statistics_label.pack()
    ttk.Separator(settings_frame, bootstyle="secondary").pack()
    prisonerNum_label.pack()
    boxNum_label.pack()
    foundNum_label.pack()
    guessNum_label.pack()
    settings_frame.pack()
    ttk.Separator(settings_frame, bootstyle="secondary").pack()
    setting_label.pack()
    priNum_label.pack()
    simNum_label.pack()
    random_label.pack()
    strategy_label.pack()


  
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
