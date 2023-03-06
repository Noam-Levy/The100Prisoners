import random
 
class Model():
    
    def __init__(self, number_of_prisoners : int = 2,
                 strategy: function = None, simulations: int = 1):
        """
          Initialize simulation model\n
          Parameters:
            number_of_prisoners (int) - number of prisoners (n >= 2)\n
            simulations (int) - number of simulations (n >= 1)\n
            strategy (function) - selected guessing strategy of prisoners\n
          Returns:
            Model instance
        """
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

    def setStrategy(self, strategy: function):
      """
        Sets prisoners strategy\n
        Parameters: 
          strategy (function) - prisoners guessing strategy
        Returns:
          none
      """
      if not strategy:
          raise ValueError("invalid strategy")
      self.strategy = strategy
    
    def guessRandomly(self):
        pass
    
    def optimizedGuess(self):
        pass


    
