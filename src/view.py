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
    priNum_scroll = ttk.Scrollbar(settings_frame, orient=HORIZONTAL, bootstyle="secondary")

    simNum_label = ttk.Label(settings_frame,text = "# of simulations", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE))

    random_label = ttk.Checkbutton(settings_frame,text = "select randomly", bootstyle="SECONDARY-ROUND-TOGGLE")
    strategy_label = ttk.Checkbutton(settings_frame,text = "apply strategy", bootstyle="SECONDARY-ROUND-TOGGLE")
    start_button = ttk.Button(settings_frame,text = "Start",bootstyle="success", command=self.on_start)
    quit_button = ttk.Button(settings_frame,text = "Quit", bootstyle="danger", command=self.on_quit)

    settings_frame.pack(side=LEFT, fill=Y)
    statistics_label.pack(padx=10, pady=10)
    ttk.Separator(settings_frame, bootstyle=SECONDARY).pack(side=LEFT, padx=10,pady=10)
    prisonerNum_label.pack(padx=10, pady=(400,10))

    boxNum_label.pack(padx=10, pady=10)
    foundNum_label.pack(padx=10, pady=10)
    guessNum_label.pack(padx=10, pady=10)
    

    ttk.Separator(settings_frame, bootstyle=SECONDARY).pack(side=LEFT, padx=10,pady=10)
    setting_label.pack(padx=10, pady=10)
    priNum_label.pack(padx=10, pady=10)
    priNum_scroll.pack(side=LEFT)
    simNum_label.pack(padx=10, pady=10)

    random_label.pack(padx=10, pady=10)
    strategy_label.pack(padx=10, pady=10)
    start_button.pack(side=LEFT, expand=YES, padx=10, pady=(15,10))
    quit_button.pack(side=LEFT, expand=YES, padx=10, pady=(15,10))


  def _drawBoxMatrix(self):
    matrix_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    label = ttk.Label(matrix_frame, text="Simulation viewer", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))
    label.pack(pady=10)
    matrix_frame.pack(pady=10)

  def run(self):
    self._drawMenuDrawer()
    self._drawBoxMatrix()
    self.root.mainloop()

  def attach(self, observer: UIEventsListener):
    self._observers.append(observer)

  def detach(self, observer: UIEventsListener):
    self._observers.remove(observer)

  
  
  def on_start(self):
    return

  def on_quit(self):
    return
