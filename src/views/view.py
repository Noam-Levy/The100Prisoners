import ttkbootstrap as ttk
from tkinter import messagebox
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
                                       self.onNumberOfPrisonersChanged, self.on_start, self.on_quit)
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
  
  def displaySimulationResults(self, results):
    """
      Handling the display of simulation results
      Parameters: 
        results (tuple) - simulation results data (success rate, average solution time, prisoners guesses lists)
      Returns: None
    """
    delay = self.simulationSpeed.get()
    _, exec_time, visited_list = results
    self.simulation_view.setAverageSimulationTime(exec_time)
    for prisoner_number, guess_list in visited_list[0].items():
      self.prisonerData.setPrisonerNumber(prisoner_number + 1)
      self.prisonerData.resetGuessNumber()
      l = len(guess_list)

      for index, guess in enumerate(guess_list):
        # set prisoner data view
        self.prisonerData.setBoxNumber(guess + 1)
        if not self.strategySelector.get() == RANDOM_STRATEGY and index < l - 1:
          self.prisonerData.setFoundNumber(guess_list[index + 1])

        # set box matrix view
        self.simulation_view.drawVisitingBox(guess)
        
        self.root.update()  # force GUI to update
        time.sleep(delay)  # delay to help user to keep track of the simulation
        self.prisonerData.incrementGuessNumber()
      self.simulation_view.resetBoxes()
      
    self.settings_frame.enableControls()

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

  def on_quit(self):
    """
      Listener function for quit button press\n
      Returns:
        None
    """
    self.root.quit()
