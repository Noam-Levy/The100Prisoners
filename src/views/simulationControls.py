import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import Callable

from constants import *
from views.subview import Subview

class simulationControlsView(Subview):
  def __init__(self, parent_frame: ttk.Frame, number_of_simulations: ttk.IntVar, simulation_speed: ttk.DoubleVar, on_next: Callable):
      """
        Initializes the simulation controls subview
        :param parent_frame: subview parent frame
        :type parent_frame: ttk.Frame
        :param number_of_simulations: pointer to the number of simulations variable
        :type number_of_simulations: ttk.IntVar
        :param simulation_speed: pointer to the simulation speed variable
        :type simulation_speed: ttk.DoubleVar
        :param on_next: pointer to a function to be called when user presses the next button
        :type on_next: Callable
        :returns: None
        :rtype: None
      """
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      self.number_of_simulations = number_of_simulations
      self.simulation_speed = simulation_speed
      
      # Simulation number and prisoner number entries
      sim_val_func = self.root.register(self._validate_simulation_number)
      invalid_cmd = self.root.register(self._onInvalidUserEntry)
      
      self.sim_num_entry = ttk.Entry(self.root,
                                     validate="key",
                                     validatecommand=(sim_val_func, '%P'),
                                     invalidcommand=invalid_cmd)
      
      # Next button
      self.next_button = ttk.Button(self.root, text="Next", bootstyle=INFO, command=on_next)

      # Simulation speed radio buttons
      self.slow_selector = ttk.Radiobutton(self.root,
                                                text = "Slow",
                                                variable=self.simulation_speed,
                                                value=SIMULATION_SPEED_SLOW,
                                                bootstyle=(SECONDARY, TOGGLE),
                                                style='TRadiobutton')
      self.medium_selector = ttk.Radiobutton(self.root,
                                                text = "Medium",
                                                variable=self.simulation_speed,
                                                value=SIMULATION_SPEED_MEDIUM,
                                                bootstyle=(SECONDARY, TOGGLE),
                                                style='TRadiobutton')
      self.fast_selector = ttk.Radiobutton(self.root,
                                            text = "Fast",
                                            variable=self.simulation_speed,
                                            value=SIMULATION_SPEED_FAST,
                                            bootstyle=(SECONDARY, TOGGLE),
                                            style='TRadiobutton')
      self.disableControls()


  def draw(self):
    ttk.Label(self.root,
              text="Simulation number",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE)).grid(row=0, column=0, padx=DEFAULT_PADDING)
    self.sim_num_entry.grid(row=0, column=1, sticky=W, pady=DEFAULT_PADDING)
    self.next_button.grid(row=0, column=2, columnspan=2,
                          sticky=EW, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)
    ttk.Label(self.root,
              text="Simulation speed",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE)).grid(row=1, column=0, padx=DEFAULT_PADDING)
    self.slow_selector.grid(row=1, column=1, pady=DEFAULT_PADDING, sticky=W)
    self.medium_selector.grid(row=2, column=1, pady=DEFAULT_PADDING, sticky=W)
    self.fast_selector.grid(row=3, column=1, pady=DEFAULT_PADDING, sticky=W)
          
    return self.root
  

  def disableControls(self):
    """
      Disables basic controls from view and adds simulation controls into view
      :returns: None
      :rtype: None
    """
    self.next_button.config(state=DISABLED)
    self.sim_num_entry.config(state=DISABLED)
    self.slow_selector.config(state=DISABLED)
    self.medium_selector.config(state=DISABLED)
    self.fast_selector.config(state=DISABLED)

  def enableControls(self):
    """
      Enables basic controls from view and adds simulation controls into view
      :returns: None
      :rtype: None
    """
    self.next_button.config(state='')
    self.sim_num_entry.config(state='')
    self.slow_selector.config(state='')
    self.medium_selector.config(state='')
    self.fast_selector.config(state='')

  def reset(self):
    """
      Resets the view
      :returns: None
      :rtype: None
    """
    self.sim_num_entry.delete(0, END)
    self.disableControls()

  def _validate_simulation_number(self, simulation_number):
    """
      Class function to validate the selected simulation number
      :param simulation_number: selected simulation number
      :type simulation_number: int
      :returns: None
      :rtype: None
    """
    if simulation_number == "":
      return True
    
    res= simulation_number.isdigit() and (1 <= int(simulation_number) <= self.number_of_simulations.get())
    if res:
      self._onInvalidUserEntry("")
    return res
  
  def _onInvalidUserEntry(self, state=DISABLED):
    """
      Class function to set the next button state in accordance to user entry validation
      :param simulation_number: new state, optional, default is disabled
      :type simulation_number: string
      :returns: None
      :rtype: None
    """
    self.next_button.config(state=state)
