from abc import abstractmethod
  
class UIEventsListener():
   @abstractmethod
   def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
      raise NotImplementedError()
   
   @abstractmethod
   def fetch_next_guess(self, simulationNumber: int, prisonerNumber: int):
      raise NotImplementedError()
   
class ModelEventsListener():
   @abstractmethod
   def statistics_report(self, report):
      raise NotImplementedError()
   
   @abstractmethod
   def simulation_report(self, report):
      raise NotImplementedError()
