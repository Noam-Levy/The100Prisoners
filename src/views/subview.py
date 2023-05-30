from abc import ABC, abstractmethod

class Subview(ABC):
  @abstractmethod
  def draw(self):
    """
      Getter method that returns the subview frame.
      
      Returns:
        tkinter frame with all subview elements. 
    """
    raise NotImplementedError()
