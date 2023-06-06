from listener import *
from model import Model
from views.view import View

from strategy import GuessRandomly, GuessOptimized

class Controller(UIEventsListener, ModelEventsListener):
    def __init__(self, view: View, model: Model):
        """
        Initialize the MVC controller and runs the view
        
        Parameters:
            view (View): simulation view instance
            model (Model): simulation model instance
        
        Returns:
            None
        """
        self.model = model
        self.view = view
        self.reqSimulationNumber = -1
        self.reqPrisonerNumber = -1
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
       
    def fetch_next_run(self, simulationNumber: int, prisonerNumber: int):
        if simulationNumber < 1 or self.model.simulations < simulationNumber:
            raise ValueError("Invalid simulation number")
        if prisonerNumber < 1 or self.model.number_of_prisoners < prisonerNumber:
            raise ValueError("Invalid prisoner number")
        
        if self.reqSimulationNumber != simulationNumber or self.reqPrisonerNumber != prisonerNumber:
            self.view.rest_boxes_request()
            self.reqSimulationNumber = simulationNumber
            self.reqPrisonerNumber = prisonerNumber

        return self.model.results[2][simulationNumber - 1]


    