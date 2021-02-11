from enum import Enum

class DeviceState(Enum):
    OK = "OK"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"

    def __getstate__(self):
        return self.value