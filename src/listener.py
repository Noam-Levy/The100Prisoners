from abc import abstractmethod
  
class UIEventsListener():
   @abstractmethod
   def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
      """
         Triggers the simulation according to the given strategy
         :param strategy: an integer specifying the strategy: 0 - Random, otherwise Optimized
         :type strategy: int
         :param numberOfSimulations: the number of simulation iterations
         :type numberOfSimulations: int
         :param numberOfPrisoners: the number of participating prisoners
         :type numberOfPrisoners: int
         :returns: None
         :rtype: None
      """
      raise NotImplementedError()

   @abstractmethod
   def fetch_next_run(self, simulationNumber: int, prisonerNumber: int):
      """
         fetches the simulation data for the given prisoner in a given simulation
         :param simulationNumber: the required simulation number
         :type simulationNumber: int
         :param prisonerNumber: the required prisoner number
         :type prisonerNumber: int
         :returns: simulation run (visit list, success)
         :rtype: tuple
      """
      raise NotImplementedError()

class ModelEventsListener():
   @abstractmethod
   def statistics_report(self, report):
      """
         control method to render the statistics report
         :param report: the statistics report
         :type report: dict
         :returns: None
         :rtype: None
      """
      raise NotImplementedError()
   
   @abstractmethod
   def simulation_report(self, report):
      """
         control method to render the simulation report
         :param report: the simulation report
         :type report: dict
         :returns: None
         :rtype: None
      """
      raise NotImplementedError()
