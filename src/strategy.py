from abc import ABC, abstractmethod

class Strategy(ABC):
    """
      The Strategy interface declares operations common to all supported versions of some algorithm.
      The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
    
class GuessRandomly(Strategy):
    #TODO: add docstring. implement random selection algorithm
    def execute(self):
        pass

class GuessOptimized(Strategy):
    #TODO: add docstring. implement optimized selection algorithm
    def execute(self):
        pass
