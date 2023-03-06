from abc import ABC, abstractmethod
from abstractObserver import AbstractObserver

class AbstractSubject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: AbstractObserver):
        """
          Attach an observer to the subject.\n
          Parameters: 
            observer (abstractObserver) - observer to be attached
          Returns:
            none
        """
        raise NotImplementedError()

    @abstractmethod
    def detach(self, observer: AbstractObserver):
        """
          Detach an observer from the subject.\n
          Parameters: 
            observer (abstractObserver) - observer to be detached
          Returns:
            none
        """
        raise NotImplementedError()

    @abstractmethod
    def notify(self):
        """
          Notify all observers about an event.\n
          Returns:
            none
        """
        raise NotImplementedError()
