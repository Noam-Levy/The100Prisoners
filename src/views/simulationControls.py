import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import Callable

from constants import *
from views.subview import Subview

class simulationControlsView(Subview):
  def __init__(self, parent_frame: ttk.Frame, number_of_prisoners: ttk.IntVar, number_of_simulations: ttk.IntVar, on_next: Callable):
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      self.number_of_prisoners = number_of_prisoners
      self.number_of_simulations = number_of_simulations
      
      # Simulation number and prisoner number entries
      sim_val_func = self.root.register(self._validate_simulation_number)
      pris_val_func = self.root.register(self._validate_prisoner_number)
      invalid_cmd = self.root.register(self._onInvalidUserEntry)
      
      self.sim_num_entry = ttk.Entry(self.root,
                                     validate="key",
                                     validatecommand=(sim_val_func, '%P'),
                                     invalidcommand=invalid_cmd)
      self.pris_num_entry = ttk.Entry(self.root,
                                      validate="key",
                                      validatecommand=(pris_val_func, '%P'),
                                      invalidcommand=invalid_cmd)
      
      # Next button
      self.next_button = ttk.Button(self.root, text="Next", bootstyle=INFO, command=on_next)
      
      # Success/Failure message label
      self.success_fail_message = ttk.Label(
                                    self.root,
                                    text="",
                                    font=(DEFAULT_FONT, DEFAULT_SUBHEADERS_SIZE),
                                    foreground='red',
                                    bootstyle=(LIGHT, INVERSE)
                                  )
      self.disableControls()


  def draw(self):
    ttk.Label(self.root,
              text="Simulation number",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE)).grid(row=0, column=0, padx=DEFAULT_PADDING)
    self.sim_num_entry.grid(row=0, column=1, sticky=W, pady=DEFAULT_PADDING)
    ttk.Label(self.root,
              text="Prisoner number",
              font=(DEFAULT_FONT, DEFAULT_FONT_SIZE),
              bootstyle=(LIGHT, INVERSE)).grid(row=1, column=0, padx=DEFAULT_PADDING)
    self.pris_num_entry.grid(row=1, column=1, sticky=W, pady=DEFAULT_PADDING)
    self.next_button.grid(row=0, column=2, rowspan=2,
                          sticky=EW, padx=DEFAULT_PADDING)
    self.success_fail_message.grid(row=2, column=0, columnspan=2)
          
    return self.root
  

  def disableControls(self):
    """
      Disables basic controls from view and adds simulation controls into view
    """
    self.next_button.config(state=DISABLED)
    self.sim_num_entry.config(state=DISABLED)
    self.pris_num_entry.config(state=DISABLED)

  def enableControls(self):
    """
      Enables basic controls from view and adds simulation controls into view
    """
    self.next_button.config(state='')
    self.sim_num_entry.config(state='')
    self.pris_num_entry.config(state='')

  def setSuccessFailMessage(self, message: str = '', isError: bool = False):
      self.success_fail_message.config(text=message, foreground='red' if isError else 'green')

  def reset(self):
    self.sim_num_entry.delete(0, END)
    self.pris_num_entry.delete(0, END)
    self.disableControls()

  def _validate_simulation_number(self, simulation_number):
    """
      Validates the selected simulation number
    """
    if simulation_number == "":
      return True
    
    res= simulation_number.isdigit() and (1 <= int(simulation_number) <= self.number_of_simulations.get())
    if res:
      self.setSuccessFailMessage()
      self._onInvalidUserEntry("")
    return res

  def _validate_prisoner_number(self, prisoner_number):
    """
      Validates the selected prisoner number
    """
    if prisoner_number == "":
      return True
    res = prisoner_number.isdigit() and (1 <= int(prisoner_number) <= self.number_of_prisoners.get())
    if res:
      self.setSuccessFailMessage()
      self._onInvalidUserEntry("")
    return res
  
  def _onInvalidUserEntry(self, state=DISABLED):
    """
      Helper method to set the next button state in accordance to user entry validation
    """
    self.next_button.config(state=state)
