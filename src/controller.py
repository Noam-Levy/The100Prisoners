from listener import *
from model import Model
from views.view import View

from strategy import GuessRandomly, GuessOptimized

class Controller(UIEventsListener, ModelEventsListener):
    def __init__(self, view: View, model: Model):
        self.model = model
        self.view = view
        self.reqSimulationNumber = -1
        self.reqPrisonerNumber = -1
        self._req_guess_list = None
        self.model.attach(self)
        self.view.attach(self)
        self.view.run()
    
    def start_simulation(self, strategy: int, numberOfSimulations: int, numberOfPrisoners: int):
        if strategy == -1:
            raise ValueError("Prisoner's strategy was not specified") 
        
        self.model.setNumberOfPrisoners(numberOfPrisoners)
        self.model.setNumberOfSimulations(numberOfSimulations)
        self.model.setStrategy(GuessRandomly() if strategy == 0 else GuessOptimized())
        self.model.run()

    def statistics_report(self, report):
        self.view.displayStatistics(report)

    def simulation_report(self, report):
        self.view.displaySimulationResults(report)       
    
    def fetch_next_guess(self, simulationNumber: int, prisonerNumber: int):
        if simulationNumber < 1 or self.model.simulations < simulationNumber:
            raise ValueError("Invalid simulation number")
        if prisonerNumber < 1 or self.model.number_of_prisoners < prisonerNumber:
            raise ValueError("Invalid prisoner number")

        if self._req_guess_list == None or self.reqPrisonerNumber != prisonerNumber or self.reqSimulationNumber != simulationNumber:
            self.view.rest_boxes_request()
            self.reqPrisonerNumber = prisonerNumber
            self.reqSimulationNumber = simulationNumber
            # create generator for requested prisoner and simulation
            self._req_guess_list = iter(self.model.results[2][simulationNumber - 1][prisonerNumber - 1])
            if self.model.strategy.__class__ .__name__== GuessOptimized.__name__:
                return prisonerNumber

        return self._req_guess_list.__next__()


    