import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import Callable
from constants import *
from views.subview import Subview

class SettingsView(Subview):
  def __init__(self, parent_frame: ttk.Frame,
               number_of_prisoners: ttk.IntVar,
               number_of_simulations: ttk.IntVar,
               strategy: ttk.IntVar,
               simulation_speed: ttk.DoubleVar,
               onNumberOfPrisonersChanged: Callable,
               on_start: Callable, on_quit: Callable, displaySimulationResults: Callable):
      
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      self.number_of_prisoners = number_of_prisoners
      self.number_of_simulations = number_of_simulations
      self.strategy = strategy
      self.simulation_speed = simulation_speed
      self.onNumberOfPrisonersChanged = onNumberOfPrisonersChanged

      # scale values labels
      self.number_of_prisoners_label = ttk.Label(self.root,
                                    text = self.number_of_prisoners.get(),
                                    font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
                                    bootstyle=(LIGHT, INVERSE))
      self.number_of_simulations_label = ttk.Label(self.root,
                                              text = self.number_of_simulations.get(),
                                              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
                                              bootstyle=(LIGHT, INVERSE))
      # simulation parameters scales
      self.number_of_prisoners_scale = ttk.Scale(self.root,
                                                  from_=MIN_PRISONER_COUNT,
                                                  to=MAX_PRISONER_COUNT,
                                                  variable=self.number_of_prisoners,
                                                  command=self._onNumberOfPrisonersChange,
                                                  bootstyle=DARK,
                                                  style='TScale')
      self.number_of_simulations_scale = ttk.Scale(self.root,
                                                    from_=MIN_SIMULATIONS_COUNT,
                                                    to=MAX_SIMULATIONS_COUNT,
                                                    variable=self.number_of_simulations,
                                                    command=self._onNumberOfSimulationsChange,
                                                    bootstyle=DARK,
                                                    style='TScale')
      # prisoners strategies check buttons
      self.random_selector = ttk.Checkbutton(self.root,
                                                text = "Select randomly",
                                                variable=self.strategy,
                                                onvalue=RANDOM_STRATEGY,
                                                offvalue=NO_STRATEGY_SELECTED,
                                                bootstyle=(SECONDARY, ROUND, TOGGLE),
                                                style='TCheckbutton')
      self.strategy_selector = ttk.Checkbutton(self.root,
                                                text = "Apply strategy",
                                                variable=self.strategy,
                                                onvalue=OPTIMIZED_STRATEGY,
                                                offvalue=NO_STRATEGY_SELECTED,
                                                bootstyle=(SECONDARY, ROUND, TOGGLE),
                                                style='TCheckbutton')
      self.speed_selector = ttk.Checkbutton(self.root,
                                               text="Fast simulation",
                                               variable=self.simulation_speed,
                                               onvalue=SIMULATION_SPEED_FAST,
                                               offvalue=SIMULATION_SPEED_SLOW,
                                               bootstyle=(
                                                   SECONDARY, ROUND, TOGGLE),
                                               style='TCheckbutton')
      
      self.start_button = ttk.Button(self.root, text = "Start", bootstyle=SUCCESS, command=on_start)
      self.reset_button = ttk.Button(self.root, text = "Reset", bootstyle=SECONDARY, command=self._on_reset)
      self.quit_button = ttk.Button(self.root, text = "Quit", bootstyle=DANGER, command=on_quit)
      self.next_button = ttk.Button(self.root, text = "Next", bootstyle=INFO, command=displaySimulationResults)
    
  def _onNumberOfPrisonersChange(self, value):
    """
      Listener for number of prisoners value change
      Returns:
        None
    """
    self.number_of_prisoners_label.config(text = "{:03.0f}".format(int(float(value))))
    self.onNumberOfPrisonersChanged()
  
  def _onNumberOfSimulationsChange(self, value):
    """
      Listener for number of simulations value change
      Returns:
        None
    """
    self.number_of_simulations_label.config(text = "{:04.0f}".format(int(float(value))))
  
  def _on_reset(self):
    """
      Setter function for resetting simulation settings
      Returns:
        None  
    """
    self.number_of_prisoners.set(DEFAULT_PRISONERS_COUNT)
    self._onNumberOfPrisonersChange(DEFAULT_PRISONERS_COUNT)
    self.number_of_simulations.set(MIN_SIMULATIONS_COUNT)
    self._onNumberOfSimulationsChange(MIN_SIMULATIONS_COUNT)
    self.strategy.set(-1)

  def disableControls(self):
    self.start_button.grid_remove()
    self.reset_button.grid_remove()
    self.quit_button.grid_remove()
    self.next_button.grid(row=6, column=1, pady=DEFAULT_PADDING)

  def enableControls(self):
    self.start_button.grid()
    self.reset_button.grid()
    self.quit_button.grid()
    self.next_button.grid_remove()
     
  def draw(self):
    # Header
    ttk.Label(self.root, text = "Settings", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
      .grid(row=0, column=0, columnspan=3, pady=DEFAULT_PADDING)
    # Number of prisoners scale
    ttk.Label(self.root,
              text="# of prisoners",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE))\
      .grid(row=1, column=0, padx=DEFAULT_PADDING)
    self.number_of_prisoners_scale.grid(row=1, column=1, padx=DEFAULT_PADDING)
    self.number_of_prisoners_label.grid(row=1, column=2, padx=DEFAULT_PADDING)
    
    # Number of simulations scale
    ttk.Label(self.root,
              text = "# of simulations",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE))\
      .grid(row=2, column=0, padx=DEFAULT_PADDING)
    self.number_of_simulations_scale.grid(row=2, column=1, padx=DEFAULT_PADDING)
    self.number_of_simulations_label.grid(row=2, column=2, padx=DEFAULT_PADDING)

    #Strategy check buttons
    self.random_selector.grid(row=3, column=1, sticky=W, pady=DEFAULT_PADDING)
    self.strategy_selector.grid(row=4, column=1, sticky=W, pady=DEFAULT_PADDING)

    # speed selector
    self.speed_selector.grid(row=5, column=1, sticky=W, pady=DEFAULT_PADDING)

    self.start_button.grid(row=6, column=0, pady=DEFAULT_PADDING)
    self.reset_button.grid(row=6, column=1, pady=DEFAULT_PADDING)
    self.quit_button.grid(row=6, column=2, pady=DEFAULT_PADDING, padx=DEFAULT_PADDING)

    return self.root
