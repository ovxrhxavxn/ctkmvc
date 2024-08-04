from abc import ABC
from typing import TYPE_CHECKING

from model import ObservableModel

if TYPE_CHECKING:
    from view import View


class Controller(ABC):

    def __init__(self, view_cls: 'type[View]', model: ObservableModel):

        self._view = view_cls(self, model)
        self._model = model

        self._view.mainloop()