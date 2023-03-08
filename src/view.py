import ttkbootstrap as ttk

class View:

  def __init__(self):
    self.root = ttk.Window(themename="superhero")
    self.root.title("The 100 Prisoners")
    self.root.iconbitmap('./src/images/prison.png')
    self.root.geometry("1200x600")
    self._drawMenuDrawer()

  def _drawMenuDrawer(self):
    pass


  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  root = View()
  root.run()
