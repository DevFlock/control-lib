from enum import Enum

class Event:
    def __init__(self) -> None:
        pass


class InputType(Enum):
    Text=1
    Number=2
    MultiChoice=3
    SingleChoice=4
    Dropdown=5
    Button=6
    Toggle=7


class BaseInput:
    def __init__(self, _id: str, input_type: InputType, title: str) -> None:
        self.id = _id
        self.input_type = input_type
        self.title = title

# Inputs
class Text(BaseInput):
    def __init__(self, _id: str, title: str, placeholder: str, callback: function) -> None:
        super().__init__(_id, InputType.Text, title)
        self.placeholder = placeholder
        self.callback = callback
    
    def _event(self, data: dict):
        self.callback(data)
    