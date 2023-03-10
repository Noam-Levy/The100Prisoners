import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from listener import UIEventsListener

DEFAULT_FONT = "Helvetica"
DEFAULT_FONT_SIZE = 10
DEFAULT_PADDING = 10

class View():

  def __init__(self):
    self._observers: list[UIEventsListener] = []
    self.root = ttk.Window(title="The 100 Prisoners", themename="superhero", size=(1200,600), iconphoto='./src/images/prison.png')
    self.run()

  def _drawMenuDrawer(self):
    menu_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    statistics_frame = self._drawStatisticsFrame(menu_frame)
    prisoner_data_frame = self._drawPrisonersDataFrame(menu_frame)
    simulation_settings_frame = self._drawSimulationSettingsFrame(menu_frame)
    statistics_frame.pack(ipadx=DEFAULT_PADDING)
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    prisoner_data_frame.pack(ipadx=DEFAULT_PADDING)
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    simulation_settings_frame.pack(ipadx=DEFAULT_PADDING)
    menu_frame.pack(side=LEFT, fill=Y)
    
  def _drawPrisonersDataFrame(self, parent_frame):
    data_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    img = PhotoImage(file='./src/images/prisoner.png')
    img_label = ttk.Label(data_frame, image=img, bootstyle=(LIGHT, INVERSE))
    img_label.pack(side=LEFT, padx=DEFAULT_PADDING)
    img_label.image = img
    ttk.Label(data_frame, text = "Prisoner Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle =(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Box Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Found Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Number of Guesses:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    
    return data_frame
  
  def _drawStatisticsFrame(self, parent_frame):
    statistics_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    ttk.Label(statistics_frame, text = "Simulation Statistics", font=(DEFAULT_FONT, 2*DEFAULT_FONT_SIZE), bootstyle =(LIGHT, INVERSE)).pack()
    
    return statistics_frame
   
  def _drawSimulationSettingsFrame(self, parent_frame):
    setting_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    ttk.Label(setting_frame,text = "Settings", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE)).pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

    prisoners_num_frame = ttk.Frame(setting_frame, bootstyle=LIGHT)
    ttk.Label(prisoners_num_frame,text = "# of prisoners", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(side=LEFT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=W)
    ttk.Scale(prisoners_num_frame, bootstyle=DARK).pack(side=RIGHT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=E)
    prisoners_num_frame.pack()
    
    simulations_num_frame = ttk.Frame(setting_frame, bootstyle=LIGHT)
    ttk.Label(simulations_num_frame,text = "# of simulations", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(side=LEFT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=W)
    ttk.Scale(simulations_num_frame, bootstyle=DARK).pack(side=RIGHT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=E)
    simulations_num_frame.pack()

    ttk.Checkbutton(setting_frame,text = "select randomly", bootstyle=(SECONDARY, ROUND, TOGGLE)).pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
    ttk.Checkbutton(setting_frame,text = "apply strategy", bootstyle=(SECONDARY, ROUND, TOGGLE)).pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
    
    ttk.Button(setting_frame,text = "Start",bootstyle=SUCCESS, command=self.on_start).pack(side=LEFT, expand=YES, pady=DEFAULT_PADDING)
    ttk.Button(setting_frame,text = "Quit", bootstyle=DANGER, command=self.on_quit).pack(side=LEFT, expand=YES, pady=DEFAULT_PADDING)

    return setting_frame

  def _drawBoxMatrix(self):
    matrix_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    label = ttk.Label(matrix_frame, text="Simulation viewer", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))
    label.pack(pady=DEFAULT_PADDING)
    matrix_frame.pack(pady=DEFAULT_PADDING)

  def run(self):
    self._drawMenuDrawer()
    self._drawBoxMatrix()
    self.root.mainloop()

  def attach(self, observer: UIEventsListener):
    self._observers.append(observer)

  def detach(self, observer: UIEventsListener):
    self._observers.remove(observer)

  def on_start(self):
    pass

  def on_quit(self):
    pass
