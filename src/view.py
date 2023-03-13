import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from listener import UIEventsListener

DEFAULT_FONT = "Helvetica"
DEFAULT_FONT_SIZE = 10
DEFAULT_PADDING = 10

LIGHT_BG_HEX = '#ABB6C2'
DARK_FG_HEX = '#20374C'

class View():

  def __init__(self):
    self._listeners: list[UIEventsListener] = []
    self.root = ttk.Window(title="The 100 Prisoners", themename="superhero", size=(1200,600), iconphoto='./src/images/prison.png')
    self.root.style.configure('TCheckbutton', background=LIGHT_BG_HEX, foreground=DARK_FG_HEX)
    self.root.style.configure('TScale', background=LIGHT_BG_HEX, thumbcolor=DARK_FG_HEX)
    self.strategySelector = ttk.IntVar()
    self.numberOfPrisoners = ttk.IntVar(value=100)
    self.numberOfSimulations = ttk.IntVar(value=1000)
    self.prisonerData = {}
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
    
    ttk.Label(data_frame, text = "Prisoner Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Box Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Found Number:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    ttk.Label(data_frame, text = "Number of Guesses:", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack(anchor=W)
    
    return data_frame
  
  def _drawStatisticsFrame(self, parent_frame):
    statistics_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    ttk.Label(statistics_frame, text = "Simulation Statistics", font=(DEFAULT_FONT, 2*DEFAULT_FONT_SIZE), bootstyle=(LIGHT, INVERSE)).pack()
    
    return statistics_frame
   
  def _drawSimulationSettingsFrame(self, parent_frame):
    def _setNumberOfPrisonersLabel(value):
      prisoners_num_label.config(text = "{:03.0f}".format(int(float(value))))
    def _setNumberOfSimulationsLabel(value):
      simulations_num_label.config(text = "{:04.0f}".format(int(float(value))))

    setting_frame = ttk.Frame(parent_frame, bootstyle=LIGHT)
    ttk.Label(setting_frame,text = "Settings", font=(DEFAULT_FONT, DEFAULT_FONT_SIZE + 5), bootstyle=(LIGHT, INVERSE))\
      .pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

    prisoners_num_frame = ttk.Frame(setting_frame, bootstyle=LIGHT)   
    ttk.Label(prisoners_num_frame,
              text="# of prisoners",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE))\
      .pack(side=LEFT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=W)
    prisoners_num_label = ttk.Label(prisoners_num_frame,
                                    text = self.numberOfPrisoners.get(),
                                    font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
                                    bootstyle=(LIGHT, INVERSE))
    prisoners_num_label.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, side=RIGHT)
    ttk.Scale(prisoners_num_frame,
              from_=10,
              to=150,
              variable=self.numberOfPrisoners,
              command=_setNumberOfPrisonersLabel,
              bootstyle=DARK,
              style='TScale')\
      .pack(side=RIGHT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=E)
    prisoners_num_frame.pack()
    
    simulations_num_frame = ttk.Frame(setting_frame, bootstyle=LIGHT)
    ttk.Label(simulations_num_frame,
              text = "# of simulations",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE))\
      .pack(side=LEFT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=W)
    simulations_num_label = ttk.Label(simulations_num_frame,
                                      text = self.numberOfSimulations.get(),
                                      font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
                                      bootstyle=(LIGHT, INVERSE))
    simulations_num_label.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, side=RIGHT)
    ttk.Scale(simulations_num_frame,
              from_=100,
              to=5000,
              variable=self.numberOfSimulations,
              command=_setNumberOfSimulationsLabel,
              bootstyle=DARK,
              style='TScale').pack(side=RIGHT, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=E)
    simulations_num_frame.pack()

    ttk.Checkbutton(setting_frame,
                    text = "select randomly",
                    variable=self.strategySelector,
                    onvalue=1,
                    offvalue=0,
                    bootstyle=(SECONDARY, ROUND, TOGGLE),
                    style='TCheckbutton').pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
    ttk.Checkbutton(setting_frame,
                    text = "apply strategy",
                    variable=self.strategySelector,
                    onvalue=-1,
                    offvalue=0,
                    bootstyle=(SECONDARY, ROUND, TOGGLE),
                    style='TCheckbutton').pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)   
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
    

  def attach(self, listener: UIEventsListener):
    self._listeners.append(listener)

  def detach(self, listener: UIEventsListener):
    self._listeners.remove(listener)

  def on_start(self):
    pass

  def on_quit(self):
    self.root.quit()
