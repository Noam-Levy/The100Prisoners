from listener import *
from model import Model
from views.view import View

from strategy import GuessRandomly, GuessOptimized

class Controller(UIEventsListener, ModelEventsListener):
    def __init__(self, view: View, model: Model):
        self.model = model
        self.view = view
        self.model.attach(self)
        self.view.attach(self)
    
    def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
        if strategy == -1:
            raise ValueError("Prisoner's strategy was not specified") 
        
        self.model.setNumberOfPrisoners(numberOfPrisoners)
        self.model.setNumberOfSimulations(numberOfSimulations)
        self.model.setStrategy(GuessRandomly() if strategy == 0 else GuessOptimized())
        self.model.run()

    def simulation_report(self, report):
        pass


    