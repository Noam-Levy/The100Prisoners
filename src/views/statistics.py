import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from constants import *
from views.subview import Subview

class StatisticsView(Subview):
  def __init__(self, parent_frame):
      """
        Initializes the statistics subview
        :param parent_frame: subview parent frame
        :type parent_frame: ttk.Frame
        :returns: None
        :rtype: None
      """
      self.root = ttk.Frame(parent_frame, bootstyle=LIGHT)
      
  def draw(self):
      ttk.Label(self.root, text = "Simulation Statistics", font=(DEFAULT_FONT, DEFAULT_HEADERS_SIZE), bootstyle=(LIGHT, INVERSE))\
        .grid(row=0, column=1, columnspan=5, sticky=N)
      return self.root
  
  def showStatistics(self, data: dict):
    """
      Creates the statistics plot and packs it into the statistics frame.
      :param data:  Statistics data dictionary containing the calculated success rate for each relevant population size
      :type data: dict
      :returns: None
      :rtype: None
    """
    self.statistics = ttk.Canvas(self.root)
    
    # create dataframe from data dict
    values = list(data.values())
    df_data = {
      'population': list(data.keys()),
      'simulated success rate': list(map(lambda x: x[0], values)),
      'calculated success rate': list(map(lambda x: x[1], values))
    }
    df = pd.DataFrame(df_data)
    melted_df = pd.melt(df, id_vars=['population'], value_vars=['simulated success rate', 'calculated success rate'])    
    
    # create the bar chart using Seaborn
    plt.figure(figsize=(6, 4))
    plot = sns.barplot(data=melted_df, x='population', y='value', hue='variable', palette='Blues')
    plt.legend(loc='lower left')
    
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
      class function to reset the view
      :returns: None
      :rtype: None
    """
    if self.statistics:
      for child in self.statistics.winfo_children():
        child.destroy() 
      self.statistics.destroy()
        
        
             
