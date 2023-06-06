from abc import ABC, abstractmethod

class Subview(ABC):
  @abstractmethod
  def draw(self):
    """
      Draws the subview frame.
      :returns: frame with all subview elements
      :rtype: ttk.Frame
    """
    raise NotImplementedError()
