import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from constants import *
from views.subview import Subview
class SettingsView(Subview):
  def __init__(self, parent_frame, number_of_prisoners, number_of_simulations, strategy, onNumberOfPrisonersChanged):
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      self.number_of_prisoners = number_of_prisoners
      self.number_of_simulations = number_of_simulations
      self.strategy = strategy
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
                                                  from_=2,
                                                  to=150,
                                                  variable=self.number_of_prisoners,
                                                  command=self._setNumberOfPrisonersLabel,
                                                  bootstyle=DARK,
                                                  style='TScale')
      self.number_of_simulations_scale = ttk.Scale(self.root,
                                                    from_=100,
                                                    to=5000,
                                                    variable=self.number_of_simulations,
                                                    command=self._setNumberOfSimulationsLabel,
                                                    bootstyle=DARK,
                                                    style='TScale')
      # prisoners strategies check buttons
      self.random_selector = ttk.Checkbutton(self.root,
                                                text = "select randomly",
                                                variable=self.strategy,
                                                onvalue=0,
                                                offvalue=-1,
                                                bootstyle=(SECONDARY, ROUND, TOGGLE),
                                                style='TCheckbutton')
      self.strategy_selector = ttk.Checkbutton(self.root,
                                                text = "apply strategy",
                                                variable=self.strategy,
                                                onvalue=1,
                                                offvalue=-1,
                                                bootstyle=(SECONDARY, ROUND, TOGGLE),
                                                style='TCheckbutton')
          
  def _setNumberOfPrisonersLabel(self, value):
    """Setter function for number of prisoners label"""
    self.number_of_prisoners_label.config(text = "{:03.0f}".format(int(float(value))))
    self.onNumberOfPrisonersChanged()
  
  def _setNumberOfSimulationsLabel(self, value):
    """Setter function for number of simulations label"""
    self.number_of_simulations_label.config(text = "{:04.0f}".format(int(float(value))))
  
  def _on_reset(self):
    """Setter function for resetting simulation settings"""
    self.number_of_prisoners.set(DEFAULT_PRISONERS_COUNT)
    self._setNumberOfPrisonersLabel(DEFAULT_PRISONERS_COUNT)
    self.number_of_simulations.set(DEFAULT_SIMULATIONS_COUNT)
    self._setNumberOfSimulationsLabel(DEFAULT_SIMULATIONS_COUNT)
    self.strategy.set(-1)
     
  def draw(self, on_start, on_quit):
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
 
      ttk.Button(self.root, text = "Start", bootstyle=SUCCESS, command=on_start).grid(row=5, column=0, pady=DEFAULT_PADDING)
      ttk.Button(self.root, text = "Reset", bootstyle=SECONDARY, command=self._on_reset).grid(row=5, column=1, pady=DEFAULT_PADDING)
      ttk.Button(self.root, text = "Quit", bootstyle=DANGER, command=on_quit).grid(row=5, column=2, pady=DEFAULT_PADDING, padx=DEFAULT_PADDING)

      return self.root
