# CTkMVC

## Install

```
pip install ctkmvc
```

## Description

The library that provides a few base classes for easy using MVC architecture pattern together with CTk library to make simple and lightweight desktop applications.

## Using example

In this example we will create a simple system that let us to make a button changing its text by clicking on it. To make your own `View`, `Controller` and `Model` classes you should inherit them from base abstract classes `View`, `Controller` and `ObservableModel` like that:

* Imports

```python
from customtkinter import CTkButton
from random import Random

from view import View
from model import ObservableModel
from controller import Controller
```

* Our View

```python
class MyWindow(View):

    def __init__(self, controller, model):

        super().__init__(controller, model)

        self.wm_title('Papa')

        self.resizable(False, False)

        self.geometry('600x400')

        self.button = CTkButton(self, command=self._controller.button_click)

        self.button.grid(row=4, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")


    def model_is_changed(self):
        
        self.button.configure(text=self._model.button_text)
```

Inherit our `View`from `View` abstract class and override `model_is_changed` method to react to `Model` changes. Then in `__init__` method we create CTk attributes to design our window and do not forget to call super `__init__` method to construct base `View` class by passing our `Controller` and `Model` objects.

* Our Model

```python
class MyWindowModel(ObservableModel):

    def __init__(self):

        super().__init__()
        
        self.__button_text = None

    @property
    def button_text(self):
        return self.__button_text
    
    @button_text.setter
    def button_text(self, value):

        self.__button_text = value

        self.notify_observers()
```

Inherit our `Model` from `ObservableModel` base abstract class and implement necessary properties our `View` observes. In setter method we call `notify_observers` method to notify subscibed views.

* Our Controller

```python
class MyWindowController(Controller):

    def __init__(self, view_cls, model):

        super().__init__(view_cls, model)

    
    def button_click(self):

        button_names = ['ctk', 'MVC', 'architecture', 'pattern']

        self._model.button_text = Random().choice(button_names)
```

Inherit our `Controller` from `Controller` base abstract class. Our `Controller` controles creating `View` object therefore in its `__init__` method we pass our `Model` object and CLASS itself but not certain object of our `View` beacuse of this:

```python
class Controller(ABC):

    def __init__(self, view_cls: 'type[View]', model: ObservableModel):

        self._view = view_cls(self, model)
        
        # Some code...
```

### Result

```python
from window import MyWindow, MyWindowModel, MyWindowController

def main():
    
    MyWindowController(

        MyWindow,
        MyWindowModel()
    )


if __name__=='__main__':
    main()
```

We get a window with a button that changes its text by clicking on it.