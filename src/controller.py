from listener import *
from model import Model
from views.view import View

class Controller(UIEventsListener, ModelEventsListener):
    def __init__(self, view: View, model: Model):
        self.model = model
        self.view = view
        self.model.attach(self)
        self.view.attach(self)

    