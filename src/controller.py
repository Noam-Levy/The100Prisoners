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
        # self._req_guess_generator = None
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
        print(prisonerNumber)
        if self.reqPrisonerNumber != prisonerNumber or self.reqSimulationNumber != simulationNumber:
            self._req_guess_list = self.model.results[2][simulationNumber][prisonerNumber]
            self.reqPrisonerNumber = prisonerNumber
            self.reqSimulationNumber = simulationNumber

        guess = self._req_guess_list.pop(0)
        return guess

    