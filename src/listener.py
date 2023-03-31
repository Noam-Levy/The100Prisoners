from abc import abstractmethod
  
class UIEventsListener():
   @abstractmethod
   def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
      raise NotImplementedError()

class ModelEventsListener():
   @abstractmethod
   def simulation_report(self, report):
      raise NotImplementedError()
