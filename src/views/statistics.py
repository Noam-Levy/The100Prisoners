import seaborn as sns
import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from constants import *
from views.subview import Subview

class StatisticsView(Subview):
  def __init__(self, parent_frame):
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      
  def draw(self):
      ttk.Label(self.root, text = "Simulation Statistics", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
        .grid(row=0, column=1, columnspan=5, sticky=N)
      return self.root
  
  def showStatistics(self, data: dict):
    """
      Creates the statistics plot and packs it into the statistics frame.
      Parameters:
        data (dict): Statistics data dictionary containing the calculated success rate for each relevant population size
      Returns:
        None
    """
    self.statistics = ttk.Canvas(self.root)
    # create the bar chart using Seaborn
    plt.figure(figsize=(4.5, 4))
    plot = sns.barplot(x=list(data.keys()), y=list(data.values()), palette='Blues')
    # add labels to axis and each bar
    for container in plot.containers:
      ax = plot.axes
      for bar in container.patches:
        text_x_pos = bar.get_x() + bar.get_width() / 2
        text_y_pos = bar.get_height()
        label = f"{round(bar.get_height(), 2)}%"
        ax.text(text_x_pos, text_y_pos, label, ha='center', va='bottom')

    plot.set_xlabel("Population Size")
    plot.set_ylabel("Success Rate (%)")

    # pack plot as image into statistics canvas
    figure = FigureCanvasTkAgg(plot.get_figure(), master=self.statistics)
    figure.get_tk_widget().pack()
    self.statistics.grid(row=1, column=1)   

  def reset(self):
    """
      Resets the view
    """
    if self.statistics:
      for child in self.statistics.winfo_children():
        child.destroy() 
      self.statistics.destroy()
        
        
             
