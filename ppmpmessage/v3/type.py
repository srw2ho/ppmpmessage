from enum import Enum

class Type(Enum):
    DEVICE = "DEVICE"
    TECHNICAL_INFO = "TECHNICAL_INFO"

    def __getstate__(self):
        return self.value
