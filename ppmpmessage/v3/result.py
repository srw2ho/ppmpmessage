from enum import Enum

class Result(Enum):
    OK = "OK"
    NOK = "NOK"
    UNKNOWN = "UNKNOWN"

    def __getstate__(self):
        return self.value
