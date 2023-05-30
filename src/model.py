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
      self.results = None
      self.statisticsData = None
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
      
      Returns:
        None
    """
    if not self.strategy:
        raise ValueError("Strategy was not defined")
    self.results = self.statisticsData = None # remove older simulation data
    
    sim_data = []
    total_successes = 0
    total_exec_time = 0
    self.executer.submit(self._statisticsCreator) # assign one thread to create simulation statistics
    futures = [self.executer.submit(self.strategy.execute, self.number_of_prisoners) for _ in range(self.simulations)]
    for future in concurrent.futures.as_completed(futures):
        success, exec_time, visited_list = future.result() # (success: bool, execution_time: float visited_list: dict)
        total_exec_time += exec_time
        sim_data.append(visited_list)
        if success:  # checks if prisoners were successful in current simulation run
            total_successes += 1
    success_rate = (100 * (total_successes / self.simulations))
    average_sol_time = total_exec_time / self.simulations
    self.results = (success_rate, average_sol_time, sim_data)
    self._reportResults()

  def attach(self, observer: ModelEventsListener):
      """
        Adds new observer to the observer list
        
        Parameters:
          observer (ModelEventsListener): observer to attach
        
        Returns:
          None
      """
      self._observers.append(observer)
    
  def detach(self, observer: ModelEventsListener):
      """
        Removes existing observer from the observer list
        
        Parameters:
          observer (ModelEventsListener): observer to be removed
        
        Returns:
          None
      """
      self._observers.remove(observer)

  def _statisticsCreator(self):
    """
      Helper function to create the statistic report
    """
    populations = list(filter(lambda x: x <= self.number_of_prisoners, [10, 25, 50, 100, 150]))
    interpolated_data = {}
    for pop in populations:
      results = [self.strategy.execute(pop) for _ in range(self.simulations)]
      total_successes = 0
      for result in results:
         if result[0]: # result = (success: bool, execution_time: float visited_list: dict)
            total_successes += 1
      
      interpolated_data[pop] = 100 * (total_successes / self.simulations)    
    self.statisticsData = interpolated_data
 
  def _reportResults(self):
    """
      Helper function to send simulation results to the observers
    """
    while not (self.statisticsData and self.results): # wait for both statistics and simulation results
       pass
    
    for observer in self._observers:
        observer.statistics_report(self.statisticsData)
        observer.simulation_report(self.results)
