from abc import ABC, abstractmethod
from listener import ModelEventsListener
import random

class Strategy(ABC):
    """
      The Strategy interface declares operations common to all supported versions of some algorithm.
      The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def execute(self, number_of_prisoners, number_of_simulations):
        raise NotImplementedError()
    
class GuessRandomly(Strategy, ModelEventsListener): 
    """
        Implementation of random guessing strategy. 
        This is the most obvious approach that can be taken by the prisoners,
        but it's surely the wrong one as it yields close to zero percent chance of winning.\n
        Methods:
            execute(number_of_prisoners: int, number_of_simulations: int):
                executes random guessing strategy.
                returns simulation results:
                    (number_of_prisoners, number_of_simulations, successes, success_rate, visited_list)
    """

    def execute(self, number_of_prisoners, number_of_simulations):
        successes = 0
        visited_list = {} # saves each prisoner guesses
        for _ in range(number_of_simulations):
            res = number_of_prisoners * [0]
            for prisoner_number in range(number_of_prisoners):
                visited = set() # keeps track of prisoner's guesses (which boxes were looked in)
                while len(visited) < (number_of_prisoners // 2): # allow current prisoner to guess upto guess limit 
                    current_box = random.randint(0, number_of_prisoners - 1)
                    #TODO: update view on selected box if on view thread
                    if current_box in visited:
                        continue
                    visited.add(current_box)
                    if current_box == prisoner_number: # check if box contains current prisoner number
                        res[prisoner_number] = 1
                        break
                visited_list[prisoner_number] = visited
            if sum(res) == number_of_prisoners: 
                successes += 1
        
        success_rate = 100 * (successes / number_of_simulations)
        return (number_of_prisoners, number_of_simulations, successes, success_rate, visited_list)

class GuessOptimized(Strategy, ModelEventsListener):
    """
        Implementation of an optimized guessing strategy. 
        according to this strategy, each prisoner will first open the box with his/hers number,
        and then will follow the the tickets inside the boxes until he/she finds his/hers number.
        by following this strategy the chances of success are greatly improved to around 30%\n
        Methods:
            execute(number_of_prisoners: int, number_of_simulations: int):
                executes optimized guessing strategy.
                returns simulation results:
                    (number_of_prisoners, number_of_simulations, successes, success_rate, visited_list)
    """

    def execute(self, number_of_prisoners, number_of_simulations):          
        successes = 0
        visited_list = {} # saves each prisoner guesses
        for _ in range(number_of_simulations):
            boxes = [i for i in range(number_of_prisoners)] 
            random.shuffle(boxes) # shuffle boxes values
            res = number_of_prisoners * [0]
            
            for prisoner_number in range(number_of_prisoners):
                visited = set() # keeps track of prisoner's guesses (which boxes were looked in)
                ticket_number = boxes[prisoner_number]
                while len(visited) < (number_of_prisoners // 2): # allow current prisoner to guess upto guess limit 
                    visited.add(ticket_number)
                    #TODO: update view on selected box if on view thread
                    if ticket_number == prisoner_number: # check if box contains current prisoner number
                        res[prisoner_number] = 1
                        break
                    ticket_number = boxes[ticket_number] # current prisoner picks the box numbered as the current ticket
                visited_list[prisoner_number] = visited
            if sum(res) == number_of_prisoners:
                successes += 1
        
        success_rate = 100 * (successes / number_of_simulations)
        return (number_of_prisoners, number_of_simulations, successes, success_rate, visited_list)
