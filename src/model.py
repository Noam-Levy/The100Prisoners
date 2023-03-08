import random
from strategy import Strategy
from abstractSubject import AbstractSubject
from abstractObserver import AbstractObserver 

class Model(AbstractSubject):
        
    def __init__(self, number_of_prisoners : int = 2, strategy: Strategy = None, simulations: int = 1):
        """
          Initialize simulation model\n
          Parameters:
            number_of_prisoners (int) - number of prisoners (n >= 2)\n
            simulations (int) - number of simulations (n >= 1)\n
            strategy (function) - selected guessing strategy of prisoners\n
          Returns:
            Model instance
        """
        self._observers: list[AbstractObserver] = []
        self.number_of_prisoners = self.setNumberOfPrisoners(number_of_prisoners)
        self.strategy = strategy
        self.simulations = self.setNumberOfSimulations(simulations)
        self.boxes = random.shuffle([i for i in range(self.number_of_prisoners)]) # shuffle boxes values
    
    def setNumberOfPrisoners(self, n: int):
        """
          Sets number of prisoners\n
          Parameters: 
            n (int) - number of prisoners (n >= 2)
          Returns:
            none
        """
        if  n < 2:
            raise ValueError("invalid number of prisoners")
        self.number_of_prisoners = n
    
    def setNumberOfSimulations(self, n: int):
        """
          Sets number of simulation runs\n
          Parameters: 
            n (int) - number of simulations (n >= 1)
          Returns:
            none
        """
        if n < 1:
            raise ValueError("invalid number of simulations")
        self.simulations = n

    def setStrategy(self, strategy: Strategy):
      """
        Sets prisoners strategy\n
        Parameters: 
          strategy (Strategy) - prisoners guessing strategy
        Returns:
          none
      """
      if not strategy:
          raise ValueError("invalid strategy")
      self.strategy = strategy
    
    def run(self):
      """
        executes simulation implementing selected prisoners strategy\n
        Returns:
          simulation results
      """
      if not self.strategy:
          raise ValueError("Strategy was not defined")
      return self.strategy.execute()
    
    def attach(self, observer: AbstractObserver):
        self._observers.append(observer)
      
    def detach(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self) # TODO: consider notify implementation.


    
