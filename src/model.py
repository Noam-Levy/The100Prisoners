import concurrent.futures

from strategy import Strategy
from listener import ModelEventsListener
from constants import DEFAULT_WORKER_THREADS, MIN_PRISONER_COUNT, MIN_SIMULATIONS_COUNT

class Model():
        
  def __init__(self, number_of_prisoners: int = MIN_PRISONER_COUNT, strategy: Strategy = None, simulations: int = MIN_SIMULATIONS_COUNT):
      """
        Initialize simulation model\n
        Parameters:
          number_of_prisoners (int) - number of prisoners (n >= 2)\n
          simulations (int) - number of simulations (n >= 1)\n
          strategy (function) - selected guessing strategy of prisoners\n
        Returns:
          Model instance
      """
      self._observers: list[ModelEventsListener] = []
      self.executer = concurrent.futures.ThreadPoolExecutor(max_workers=DEFAULT_WORKER_THREADS)
      self.setNumberOfPrisoners(number_of_prisoners)
      self.setNumberOfSimulations(simulations)
      self.strategy = strategy
      
  def setNumberOfPrisoners(self, n: int):
      """
        Sets number of prisoners\n
        Parameters: 
          n (int) - number of prisoners (n >= 2)
        Returns:
          None
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
          None
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
        None
    """
    if not strategy:
        raise ValueError("invalid strategy")
    self.strategy = strategy
  
  def run(self):
    """
      executes simulations implementing selected prisoners strategy.\n
      the method will report the results to the model's observers\n
      Returns:
        None
    """
    if not self.strategy:
        raise ValueError("Strategy was not defined")
    
    total_successes = 0
    exec_times = 0
    futures = [self.executer.submit(self.strategy.execute, self.number_of_prisoners) for _ in range(self.simulations)]
    for future in concurrent.futures.as_completed(futures):
        data = future.result() #  (success: bool, execution_time: float visited_list: dict)
        exec_times += data[1]
        if data[0]: 
            total_successes += 1

    success_rate = (100 * (total_successes / self.simulations))
    average_sol_time = exec_times / self.simulations
    data_to_sim_view = futures[0].result()[2] # extract first simulation visited_list to be displayed in view.
    results = (success_rate, average_sol_time, data_to_sim_view)
    for observer in self._observers:
        observer.simulation_report(results)

  def attach(self, observer: ModelEventsListener):
      self._observers.append(observer)
    
  def detach(self, observer: ModelEventsListener):
      self._observers.remove(observer)


    
