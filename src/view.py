import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from listener import UIEventsListener

DEFAULT_FONT = "Helvetica"
DEFAULT_FONT_SIZE = 10

class View():

  def __init__(self):
    self._observers: list[UIEventsListener] = []
    self.root = ttk.Window(themename="superhero")
    self.root.title("The 100 Prisoners")
    photo = PhotoImage(file = './src/images/prison.png')
    self.root.iconphoto(False, photo)
    self.root.geometry("1200x600")
    self.run()

  def _drawMenuDrawer(self):
    settings_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    statistics_label = ttk.Label(settings_frame,text = "Statistics", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))

    prisonerNum_label = ttk.Label(settings_frame,text = "Prisoner Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle =(LIGHT, INVERSE))
    boxNum_label = ttk.Label(settings_frame,text = "Box Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))
    foundNum_label = ttk.Label(settings_frame,text = "Found Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))
    guessNum_label = ttk.Label(settings_frame,text = "Number of Guesses :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))

    setting_label = ttk.Label(settings_frame,text = "Settings", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))
    priNum_label = ttk.Label(settings_frame,text = "# of prisoners", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
    simNum_label = ttk.Label(settings_frame,text = "# of simulations", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
    random_label = ttk.Label(settings_frame,text = "select randomly", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))
    strategy_label = ttk.Label(settings_frame,text = "apply strategy", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))

    statistics_label.pack()
    ttk.Separator(settings_frame, bootstyle=SECONDARY).pack()
    prisonerNum_label.pack()
    boxNum_label.pack()
    foundNum_label.pack()
    guessNum_label.pack()
    settings_frame.pack()
    ttk.Separator(settings_frame, bootstyle=SECONDARY).pack()
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
    self._drawMenuDrawer()
    self._drawBoxMatrix()
    self.root.mainloop()

  def attach(self, observer: UIEventsListener):
    self._observers.append(observer)

  def detach(self, observer: UIEventsListener):
    self._observers.remove(observer)

