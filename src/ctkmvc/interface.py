from abc import ABC, abstractmethod


class ModelObserver(ABC):

    @abstractmethod
    def model_is_changed(self):
        pass