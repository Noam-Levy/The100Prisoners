from abc import ABC, abstractmethod
from listener import ModelEventsListener
import random
import timeit

class Strategy(ABC):
    """
      The Strategy interface declares operations common to all supported versions of some algorithm.
      The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def execute(self, number_of_prisoners):
        raise NotImplementedError()
    
class GuessRandomly(Strategy, ModelEventsListener): 
    """
        Implementation of random guessing strategy. 
        This is the most obvious approach that can be taken by the prisoners,
        but it's surely the wrong one as it yields close to zero percent chance of winning.\n
        Methods:
            execute(number_of_prisoners: int):
                executes random guessing strategy.
                returns simulation results:
                    (success: bool, execution_time: float visited_list: dict)
    """

    def execute(self, number_of_prisoners):
        visited_list = {} # saves each prisoner guesses (which boxes were looked in)
        res = number_of_prisoners * [0]
        
        t1 = timeit.default_timer()
        for prisoner_number in range(number_of_prisoners):
            visited = [] # keeps track of prisoner's guesses
            while not res[prisoner_number]: # allow current prisoner to guess upto guess limit 
                current_box = random.randint(0, number_of_prisoners - 1) + 1
                if current_box in visited:
                    continue

                visited.append(current_box)
                if current_box - 1 == prisoner_number:
                    res[prisoner_number] = 1 if len(visited) <= (number_of_prisoners // 2) else 0
                    break
            visited_list[prisoner_number] = visited
        
        execution_time = timeit.default_timer() - t1
        success = sum(res) == number_of_prisoners
        return (success, execution_time, visited_list)

class GuessOptimized(Strategy, ModelEventsListener):
    """
        Implementation of an optimized guessing strategy. 
        according to this strategy, each prisoner will first open the box with his/hers number,
        and then will follow the the tickets inside the boxes until he/she finds his/hers number.
        by following this strategy the chances of success are greatly improved to around 30%\n
        Methods:
            execute(number_of_prisoners: int):
                executes optimized guessing strategy.
                returns simulation results:
                    (success: bool, execution_time: float visited_list: dict)
    """

    def execute(self, number_of_prisoners):
        guess_lists = {} # tracks each prisoner's decision path (which boxes were looked in)
        boxes = [i for i in range(number_of_prisoners)] # create boxes and shuffle "tickets"
        random.shuffle(boxes)
        
        res = number_of_prisoners * [0]  # tracks success or failure of prisoner[k]
        t1 = timeit.default_timer()
        for prisoner_number in range(number_of_prisoners):
            guess_history = [] # saves the prisoner's guesses (which boxes were opened)
            current_box = boxes[prisoner_number]
            
            while not res[prisoner_number]:
                guess_history.append(current_box + 1)
                if current_box == prisoner_number:
                    res[prisoner_number] = 1 if len(guess_history) <= (number_of_prisoners // 2) else 0
                    break
                else:
                    current_box = boxes[current_box]
            guess_lists[prisoner_number] = guess_history 
        
        # aggregate data to return
        success = sum(res) == number_of_prisoners
        execution_time = timeit.default_timer() - t1
        return (success, execution_time, guess_lists)
