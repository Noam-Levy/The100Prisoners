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
    menu_frame = ttk.Frame(self.root, bootstyle=LIGHT)

    simulation_settings_frame = self._drawSimulationSettingsFrame(menu_frame)

    simulation_settings_frame.pack()
    menu_frame.pack(side=LEFT, fill=Y)



    # settings_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    # statistics_label = ttk.Label(settings_frame,text = "Statistics", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))

    # prisonerNum_label = ttk.Label(settings_frame,text = "Prisoner Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle =(LIGHT, INVERSE))
    # boxNum_label = ttk.Label(settings_frame,text = "Box Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))
    # foundNum_label = ttk.Label(settings_frame,text = "Found Number :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))
    # guessNum_label = ttk.Label(settings_frame,text = "Number of Guesses :", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),bootstyle=(LIGHT, INVERSE))

    

    # settings_frame.pack(side=LEFT, fill=Y)
    # statistics_label.pack(padx=10, pady=10)
    # ttk.Separator(settings_frame, bootstyle=SECONDARY).pack(side=LEFT, padx=10,pady=10)
    # prisonerNum_label.pack(padx=10, pady=(400,10))

    # boxNum_label.pack(padx=10, pady=10)
    # foundNum_label.pack(padx=10, pady=10)
    # guessNum_label.pack(padx=10, pady=10)
    

  def _drawSimulationSettingsFrame(self, parent_frame):
    setting_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    ##ttk.Separator(setting_frame, bootstyle=SECONDARY).pack()
    ttk.Label(setting_frame,text = "Settings", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE)).pack(padx=10, pady=10)

    prisoners_num_frame = self._drawSimulationPrisonersFrame(setting_frame)
    prisoners_num_frame.pack()
    
    simulations_num_frame = self._drawSimulationSimulationsFrame(setting_frame)
    simulations_num_frame.pack()

    ttk.Checkbutton(setting_frame,text = "select randomly", bootstyle=(SECONDARY, ROUND, TOGGLE)).pack(padx=10, pady=10)
    ttk.Checkbutton(setting_frame,text = "apply strategy", bootstyle=(SECONDARY, ROUND, TOGGLE)).pack(padx=10, pady=10)
    
    ttk.Button(setting_frame,text = "Start",bootstyle=SUCCESS, command=self.on_start).pack(side=LEFT, expand=YES, pady=(15,10))
    ttk.Button(setting_frame,text = "Quit", bootstyle=DANGER, command=self.on_quit).pack(side=LEFT, expand=YES, pady=(15,10))

    return setting_frame
  
  def _drawSimulationPrisonersFrame(self, parent_frame):
    prisoners_num_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)

    ttk.Label(prisoners_num_frame,text = "# of prisoners", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(side=LEFT, padx=10, pady=10)
    ttk.Scale(prisoners_num_frame, bootstyle=DARK).pack(side=RIGHT, padx=10, pady=10)

    return prisoners_num_frame
  
  def _drawSimulationSimulationsFrame(self, parent_frame):
    simulations_num_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)

    ttk.Label(simulations_num_frame,text = "# of simulations", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(side=LEFT, padx=10, pady=10)
    ttk.Scale(simulations_num_frame, bootstyle=DARK).pack(side=RIGHT, padx=10, pady=10)

    return simulations_num_frame



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
