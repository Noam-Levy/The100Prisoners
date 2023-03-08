import ttkbootstrap as ttk

class View:

  def __init__(self):
    self.root = ttk.Window(themename="superhero")
    self.root.title("The 100 Prisoners")
    ##self.root.iconbitmap('./src/images/prison.png')
    self.root.geometry("1200x600")
    self._drawMenuDrawer()

  def _drawMenuDrawer(self):
    settings_frame = ttk.Frame(self.root, bootstyle = "light")
    statistics_label = ttk.Label(settings_frame,text = "Statistics", font=("Helvetica", 15),bootstyle = "inverse light")

    prisonerNum_label = ttk.Label(settings_frame,text = "Prisoner Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    boxNum_label = ttk.Label(settings_frame,text = "Box Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    foundNum_label = ttk.Label(settings_frame,text = "Found Number :", font=("Helvetica", 10),bootstyle = "inverse light")
    guessNum_label = ttk.Label(settings_frame,text = "Number of Guesses :", font=("Helvetica", 10),bootstyle = "inverse light")

    setting_label = ttk.Label(settings_frame,text = "Settings", font=("Helvetica", 15),bootstyle = "inverse light")
    priNum_label = ttk.Label(settings_frame,text = "# of prisoners", font=("Helvetica", 10),bootstyle = "inverse light")
    simNum_label = ttk.Label(settings_frame,text = "# of simulations", font=("Helvetica", 10),bootstyle = "inverse light")
    random_label = ttk.Label(settings_frame,text = "select randomly", font=("Helvetica", 10),bootstyle = "inverse light")
    strategy_label = ttk.Label(settings_frame,text = "apply strategy", font=("Helvetica", 10),bootstyle = "inverse light")

    statistics_label.pack()
    ttk.Separator(settings_frame, bootstyle="secondary").pack()
    prisonerNum_label.pack()
    boxNum_label.pack()
    foundNum_label.pack()
    guessNum_label.pack()
    settings_frame.pack()
    ttk.Separator(settings_frame, bootstyle="secondary").pack()
    setting_label.pack()
    priNum_label.pack()
    simNum_label.pack()
    random_label.pack()
    strategy_label.pack()




  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  root = View()
  root.run()
