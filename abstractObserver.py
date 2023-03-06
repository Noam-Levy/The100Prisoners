from abc import ABC, abstractmethod
from abstractSubject import AbstractSubject

class AbstractObserver(ABC):
    """
    The Observer interface declares the update method, to be used by subjects.
    """

    @abstractmethod
    def update(self, subject: AbstractSubject): # TODO: consider removing subject from function signature.
        """
          Receives update from subject.\n
          Parameters: 
            subject (AbstractSubject) - updating subject
          Returns:
            none
        """
        pass
