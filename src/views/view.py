import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time

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
    self.root.style.configure('TEntry', background=LIGHT_BG_HEX)
    self.strategySelector = ttk.IntVar(value=NO_STRATEGY_SELECTED)
    self.numberOfPrisoners = ttk.IntVar(value=DEFAULT_PRISONERS_COUNT)
    self.numberOfSimulations = ttk.IntVar(value=MIN_SIMULATIONS_COUNT)
    self.simulationSpeed = ttk.DoubleVar(value=SIMULATION_SPEED_SLOW)
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
    
    self.settings_frame = SettingsView(menu_frame, self.numberOfPrisoners, self.numberOfSimulations, self.strategySelector, self.simulationSpeed,
                                       self.onNumberOfPrisonersChanged, self.on_start, self.on_quit, self.on_next)
    simulation_settings_frame = self.settings_frame.draw()
        
    simulation_statistics_frame.pack()
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    prisoner_data_frame.pack(ipadx=DEFAULT_PADDING)
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    simulation_settings_frame.pack(ipadx=DEFAULT_PADDING)
    menu_frame.pack(side=LEFT, fill=Y)
    
    # Simulation view
    self.simulation_view = BoxMatrix(self.root, self.numberOfPrisoners)
    simulation_view_frame = self.simulation_view.draw()
    simulation_view_frame.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=CENTER)

    self.root.mainloop()
  
  def displayStatistics(self, results):
    """
      Handling the display of the statistical calculations
      Parameters: 
        results (dict) - statistical calculations data (population size: success %)
      Returns: None
    """
    self.statistics_frame.showStatistics(results)

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
    self.settings_frame.setErrorMessage()
    self.settings_frame.disableControls()
    for listener in self._listeners:
      try:
        listener.start_simulation(self.strategySelector.get(), self.numberOfSimulations.get(), self.numberOfPrisoners.get())
      except ValueError as e:
        self.settings_frame.enableControls()
        self.settings_frame.setErrorMessage(e.args[0])

  def on_next(self):
    for listener in self._listeners:
      try:
        prisoner_number = int(self.settings_frame.pris_entry.get())
        simulation_number = int(self.settings_frame.sim_entry.get())
        next_guess = listener.fetch_next_guess(simulation_number, prisoner_number)
        if next_guess == prisoner_number: # first guess or user changed requested simulation number or prisoner number
          self.simulation_view.resetBoxes()
        
        # set box matrix view
        self.simulation_view.drawVisitingBox(next_guess - 1) # box illustrations are stored in a zero based array
        self.root.update()  # force GUI to update
      except StopIteration:
        self.settings_frame.onInvalidUserEntry() # disables "next" button
      except ValueError as e:
        self.settings_frame.setErrorMessage(e.args[0])

  def on_quit(self):
    """
      Listener function for quit button press\n
      Returns:
        None
    """
    self.root.quit()
