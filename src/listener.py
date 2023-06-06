from abc import abstractmethod
  
class UIEventsListener():
   @abstractmethod
   def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
      """
         Triggers the simulation according to the given strategy
         
         Parameters:
            strategy (int): an integer specifying the strategy: 0 - Random, otherwise Optimized
            numberOfSimulations (int): the number of simulation iterations
            numberOfPrisoners (int): the number of participating prisoners
         
         Returns: 
            None
      """
      raise NotImplementedError()

   @abstractmethod
   def fetch_next_run(self, simulationNumber: int, prisonerNumber: int):
      """
         fetches the simulation data for the given prisoner in a given simulation
         
         Parameters:
            simulationNumber (int): simulation number
            prisonerNumber (int): prisoner number
         
         Returns: 
            simulation run (tuple): (visit list, success)
      """
      raise NotImplementedError()

class ModelEventsListener():
   @abstractmethod
   def statistics_report(self, report):
      """
         control method to render the statistics report
         
         Parameters:
            report: the statistics report
         
         Returns:
            None
      """
      raise NotImplementedError()
   
   @abstractmethod
   def simulation_report(self, report):
      """
         control method to render the simulation report
         
         Parameters:
            report: the simulation report
         
         Returns:
            None
      """
      raise NotImplementedError()
