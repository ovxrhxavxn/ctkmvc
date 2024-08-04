from abc import ABC

from interface import ModelObserver

class ObservableModel(ABC):

    def __init__(self):

        self._observers: list[ModelObserver] = []

    def add_observer(self, observer: ModelObserver):
        
        self._observers.append(observer)

    def remove_observer(self, observer: ModelObserver):
        
        self._observers.remove(observer)

    def notify_observers(self):
        
        for observer in self._observers:

            observer.model_is_changed()