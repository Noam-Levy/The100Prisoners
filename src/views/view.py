import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import time

from constants import *
from views.settings import SettingsView
from views.statistics import StatisticsView
from views.simulationControls import simulationControlsView
from views.boxMatrix import BoxMatrix
from listener import UIEventsListener

class View():
  def __init__(self):
    """
      Initialize main view\n
      Returns:
        View instance
    """
    self._listeners: list[UIEventsListener] = []
    image_dir = os.path.join(os.getcwd(), 'images', 'prison.png')
    self.root = ttk.Window(title="The 100 Prisoners",
                           themename="superhero",
                           size=(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT),
                           iconphoto=image_dir)
    self.root.style.configure('TCheckbutton', background=LIGHT_BG_HEX, foreground=DARK_FG_HEX)
    self.root.style.configure('TRadiobutton', background=LIGHT_BG_HEX, foreground=DARK_FG_HEX)
    self.root.style.configure('TScale', background=LIGHT_BG_HEX, thumbcolor=DARK_FG_HEX)
    self.root.style.configure('TEntry', background=LIGHT_BG_HEX)
    self.root.attributes('-fullscreen', True)

    self.strategySelector = ttk.IntVar(value=NO_STRATEGY_SELECTED)
    self.numberOfPrisoners = ttk.IntVar(value=DEFAULT_PRISONERS_COUNT)
    self.numberOfSimulations = ttk.IntVar(value=MIN_SIMULATIONS_COUNT)
    self.simulationSpeed = ttk.DoubleVar(value=SIMULATION_SPEED_MEDIUM)
    self.currentPrisoner = 1
    self.selectedSimulation = -1
  
  def run(self):
    """
      Draws and renders UI\n
      Returns:
        None
    """
    # Menu
    menu_frame = ttk.Frame(self.root, bootstyle=LIGHT)
    self.statistics_frame = StatisticsView(menu_frame)
    self.simulation_controls = simulationControlsView(menu_frame, self.numberOfSimulations, self.simulationSpeed, self.on_next)
    self.settings_frame = SettingsView(
                                        menu_frame,
                                        self.numberOfPrisoners,
                                        self.numberOfSimulations,
                                        self.strategySelector,
                                        self.onNumberOfPrisonersChanged,
                                        self.on_start,
                                        self.on_quit,
                                        self.on_reset
                                      )

    self.statistics_frame.draw().pack()
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    self.simulation_controls.draw().pack()
    ttk.Separator(menu_frame, bootstyle=SECONDARY).pack(pady=DEFAULT_PADDING, fill=X)
    self.settings_frame.draw().pack()
    menu_frame.pack(side=LEFT, fill=Y, ipadx=DEFAULT_PADDING)
    
    # Simulation view
    self.simulation_view = BoxMatrix(self.root, self.numberOfPrisoners)
    simulation_view_frame = self.simulation_view.draw()
    simulation_view_frame.pack(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, anchor=CENTER)
    
    # bind os window close button and escape to the on_quit method
    self.root.protocol('WM_DELETE_WINDOW', self.on_quit) 
    self.root.bind("<Escape>", lambda _: self.on_quit())
    
    self.root.mainloop()
  
  def displayStatistics(self, results):
    """
      Handling the display of the statistical calculations
      Parameters: 
        results (dict) - statistical calculations data (population size: success %)
      Returns: None
    """
    self.statistics_frame.showStatistics(results)

  def displaySimulationResults(self, results):
    self.simulation_view.setAverageSimulationTime(results[1])

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
    self.simulation_controls.enableControls()
    for listener in self._listeners:
      try:
        listener.start_simulation(self.strategySelector.get(), self.numberOfSimulations.get(), self.numberOfPrisoners.get())
      except ValueError as e:
        self.settings_frame.enableControls()
        self.simulation_controls.disableControls()
        self.settings_frame.setErrorMessage(e.args[0])

  def on_next(self):
    """
      Listener function for next button press.\n
      the function handles all necessary logic to update the UI in accordance to the simulation results.
      Returns:
        None
    """
    if self.currentPrisoner > self.numberOfPrisoners.get():
      # print simulation results
      self.currentPrisoner = 1 # TODO: CURRENTLY ALLOWS FOR THE RUN TO REPEAT - THINK
      return
    
    simulation_number = int(self.simulation_controls.sim_num_entry.get())
    if simulation_number != self.selectedSimulation:
      self.currentPrisoner = 1
      self.selectedSimulation = simulation_number
    
    for listener in self._listeners:
        next_run = listener.fetch_next_run(self.selectedSimulation, self.currentPrisoner)
        self._displaySimulationRun(next_run)
    
    self.currentPrisoner += 1

  def on_quit(self):
    """
      Listener function for quit button press\n
      Returns:
        None
    """
    self.root.quit()

  def on_reset(self):
    """
      Resetting simulation statistics
      Returns:
        None  
    """
    self.statistics_frame.reset()
    self.simulation_controls.reset()
    self.currentPrisoner = 1
    self.selectedSimulation = -1
  
  def rest_boxes_request(self):
    """
      Resetting simulation view boxes to unvisited state
      Returns:
        None
    """
    self.simulation_view.resetBoxes()

  def _displaySimulationRun(self, data):
    """
      Handling the display of a prisoner path
      
      Parameters:
        data (tuple): prisoner run data (guess list, success)
      
      Returns:
        None
    """
    delay = self.simulationSpeed.get()
    guess_list, success = data
    if self.strategySelector.get() == OPTIMIZED_STRATEGY:
      self.simulation_view.drawVisitingBox(self.currentPrisoner)
      self.root.update()  # force GUI to update
      time.sleep(delay)
    
    prisoner_guess_list = guess_list[self.currentPrisoner - 1]
    for guess in prisoner_guess_list:
      time.sleep(delay)
      self.simulation_view.drawVisitingBox(guess)
      self.root.update()  # force GUI to update
    
    # TODO: set prisoner run results text
