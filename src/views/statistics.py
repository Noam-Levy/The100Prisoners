import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from constants import *
from views.subview import Subview

class StatisticsView(Subview):
    def __init__(self, parent_frame):
        self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)

    def draw(self):
        ttk.Label(self.root, text = "Simulation Statistics", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
          .grid(row=0, column=1, columnspan=3, sticky=W)
        
        return self.root
