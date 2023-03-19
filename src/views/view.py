import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

from constants import *
from views.settings import SettingsView
from views.statistics import StatisticsView
from views.prisonerData import PrisonerDataView
from views.boxMatrix import BoxMatrix

from listener import UIEventsListener

class View():
  def __init__(self):
    self._listeners: list[UIEventsListener] = []
    self.root = ttk.Window(title="The 100 Prisoners", themename="superhero", size=(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), iconphoto='./src/images/prison.png')
    self.root.style.configure('TCheckbutton', background=LIGHT_BG_HEX, foreground=DARK_FG_HEX)
    self.root.style.configure('TScale', background=LIGHT_BG_HEX, thumbcolor=DARK_FG_HEX)
    self.strategySelector = ttk.IntVar(value=-1)
    self.numberOfPrisoners = ttk.IntVar(value=DEFAULT_PRISONERS_COUNT)
    self.numberOfSimulations = ttk.IntVar(value=DEFAULT_SIMULATIONS_COUNT)
    self.prisonerData = {}
    self.run()
  
  def run(self):
    menu_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    
    # Menu
    self.statistics_frame = StatisticsView(menu_frame)
    simulation_statistics_frame = self.statistics_frame.draw()
    
    self.prisonerData = PrisonerDataView(menu_frame)
    prisoner_data_frame = self.prisonerData.draw()
    
    self.settings_frame = SettingsView(menu_frame)
    simulation_settings_frame = self.settings_frame.draw(self.on_start, self.on_quit)
        
    simulation_statistics_frame.pack()
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    prisoner_data_frame.pack(ipadx=DEFAULT_PADDING)
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    simulation_settings_frame.pack(ipadx=DEFAULT_PADDING)
    menu_frame.pack(side=LEFT, fill=Y)
    
    # Simulation view
    self.simulation_view = BoxMatrix(self.root, self.settings_frame.number_of_prisoners.get())
    simulation_view_frame = self.simulation_view.draw()
    simulation_view_frame.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

    self.root.mainloop()
    
  def attach(self, listener: UIEventsListener):
    self._listeners.append(listener)

  def detach(self, listener: UIEventsListener):
    self._listeners.remove(listener)

  def on_start(self):
    pass

  def on_quit(self):
    self.root.quit()
