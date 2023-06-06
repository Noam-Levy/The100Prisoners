import concurrent.futures

from strategy import Strategy
from listener import ModelEventsListener
from constants import DEFAULT_WORKER_THREADS, MIN_PRISONER_COUNT, MIN_SIMULATIONS_COUNT

class Model():
        
  def __init__(self, number_of_prisoners: int = MIN_PRISONER_COUNT, strategy: Strategy = None, simulations: int = MIN_SIMULATIONS_COUNT):
      """
        Initialize simulation model
        :param number_of_prisoners: number of prisoners (n >= 2)
        :type number_of_prisoners: int
        :param strategy: selected guessing strategy of prisoners
        :type strategy: Strategy
        :param simulations: number of simulations (n >= 1)
        :type simulations: int
        :returns: Model instance
        :rtype: Model
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
        Sets number of prisoners
        :param n: number of prisoners (n >= 2)
        :type n: int
        :returns: None
        :rtype: None
      """
      if n < 2:
          raise ValueError("invalid number of prisoners")
      self.number_of_prisoners = n
  
  def setNumberOfSimulations(self, n: int):
      """
        Sets number of simulation runs
        :param n: number of simulations (n >= 1)
        :type n: int
        :returns: None
        :rtype: None
      """
      if n < 1:
          raise ValueError("invalid number of simulations")
      self.simulations = n

  def setStrategy(self, strategy: Strategy):
    """
      Sets prisoners strategy
      :param strategy: prisoners guessing strategy
      :type strategy: Strategy
      :returns: None
      :rtype: None
    """
    if not strategy:
        raise ValueError("invalid strategy")
    self.strategy = strategy
  
  def run(self):
    """
      executes simulations implementing selected prisoners strategy.
      :returns: None
      :rtype: None
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
        success, exec_time, visited_list = future.result() # (success: bool, execution_time: float, sim_data: (visited_list: dict, success: bool))
        total_exec_time += exec_time
        sim_data.append((visited_list, success))
        if success:  # checks if prisoners were successful in current simulation run
            total_successes += 1
   
    success_rate = (100 * (total_successes / self.simulations))
    average_sol_time = total_exec_time / self.simulations
    self.results = (success_rate, average_sol_time, sim_data)
    self._reportResults()

  def attach(self, observer: ModelEventsListener):
      """
        Adds new observer to the observer list
        :param observer: observer to attach
        :type observer: ModelEventsListener
        :returns: None
        :rtype: None
      """
      self._observers.append(observer)
    
  def detach(self, observer: ModelEventsListener):
      """
        Removes existing observer from the observer list
        :param observer: observer to detach
        :type observer: ModelEventsListener
        :returns: None
        :rtype: None
      """
      self._observers.remove(observer)

  def _statisticsCreator(self):
    """
      Helper function to create the statistic report
      :returns: None
      :rtype: None
    """
    populations = list(filter(lambda x: x <= self.number_of_prisoners, [2,5] if self.number_of_prisoners < 10 else [2, 10, 25, 50, 100, 150]))
    interpolated_data = {}
    for pop in populations:
      results = [self.strategy.execute(pop) for _ in range(self.simulations)]
      theoretical_success_rate = self._calcTheoreticalSuccessRate(pop)
      total_successes = 0
      for result in results:
         if result[0]: # result = (success: bool, execution_time: float, sim_data: tuple)
            total_successes += 1

      interpolated_data[pop] = [100 * (total_successes / self.simulations), theoretical_success_rate]
    
    self.statisticsData = interpolated_data

  def _reportResults(self):
    """
      Calss function to send simulation results to the observers
      :returns: None
      :rtype: None
    """
    while not (self.statisticsData and self.results): # wait for both statistics and simulation results
       pass
    
    for observer in self._observers:
        observer.statistics_report(self.statisticsData)
        observer.simulation_report(self.results)

  def _calcTheoreticalSuccessRate(self, population):
    """
      Calculates the theoretical success rate for the given population
      The calculation is based on the selected strategy and its respective mathematical equation.
      :param population: the number of prisoners
      :type population: int
      :returns: success rate int percent
      :rtype: float
    """
    if not self.strategy.__class__.__name__ == 'GuessOptimized':
       return 100 * (1 / 2 ** population)
    
    sum = 0
    half_pop = population / 2
    for i in range(population//2):
      sum += 1 / (half_pop + (i + 1))
    
    return 100 * (1 - sum)

