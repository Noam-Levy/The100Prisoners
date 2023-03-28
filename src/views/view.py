import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from constants import *
from views.settings import SettingsView
from views.statistics import StatisticsView
from views.prisonerData import PrisonerDataView
from views.boxMatrix import BoxMatrix
from listener import UIEventsListener

class View():
  def __init__(self):
    """
      Initialize simulation view\n
      Returns:
        View instance
    """
    self._listeners: list[UIEventsListener] = []
    self.root = ttk.Window(title="The 100 Prisoners", themename="superhero", size=(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), iconphoto='./src/images/prison.png')
    self.root.style.configure('TCheckbutton', background=LIGHT_BG_HEX, foreground=DARK_FG_HEX)
    self.root.style.configure('TScale', background=LIGHT_BG_HEX, thumbcolor=DARK_FG_HEX)
    self.strategySelector = ttk.IntVar(value=-1)
    self.numberOfPrisoners = ttk.IntVar(value=DEFAULT_PRISONERS_COUNT)
    self.numberOfSimulations = ttk.IntVar(value=MIN_SIMULATIONS_COUNT)
    self.prisonerData = {}
  
  def run(self):
    """
      Draws and renders UI\n
      Returns:
        None
    """
    menu_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    
    # Menu
    self.statistics_frame = StatisticsView(menu_frame)
    simulation_statistics_frame = self.statistics_frame.draw()
    
    self.prisonerData = PrisonerDataView(menu_frame)
    prisoner_data_frame = self.prisonerData.draw()
    
    self.settings_frame = SettingsView(menu_frame, self.numberOfPrisoners, self.numberOfSimulations, self.strategySelector, self.onNumberOfPrisonersChanged)
    simulation_settings_frame = self.settings_frame.draw(self.on_start, self.on_quit)
        
    simulation_statistics_frame.pack()
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    prisoner_data_frame.pack(ipadx=DEFAULT_PADDING)
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    simulation_settings_frame.pack(ipadx=DEFAULT_PADDING)
    menu_frame.pack(side=LEFT, fill=Y)
    
    # Simulation view
    self.simulation_view = BoxMatrix(self.root, self.numberOfPrisoners.get())
    simulation_view_frame = self.simulation_view.draw()
    simulation_view_frame.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

    self.root.mainloop()

  def onNumberOfPrisonersChanged(self):
    """
      Listener function for prisoner number scale change\n
      Returns:
        None
    """
    self.simulation_view.setNumberOfBoxes()
    self.simulation_view.draw()
 
  def attach(self, listener: UIEventsListener):
    """
      Attaches new UIEventsListener to the view listeners list\n
      Returns:
        None
    """
    self._listeners.append(listener)

  def detach(self, listener: UIEventsListener):
    """
      Removes existing UIEventsListener from the view listeners list\n
      Returns:
        None
    """
    try:
      self._listeners.remove(listener)
    except:
      return

  def on_start(self):
    """
      Listener function for simulation start button press\n
      Returns:
        None
    """
    for listener in self._listeners:
      listener.start_simulation(self.strategySelector.get(), self.numberOfSimulations.get(), self.numberOfPrisoners.get())

  def on_quit(self):
    """
      Listener function for quit button press\n
      Returns:
        None
    """
    self.root.quit()
