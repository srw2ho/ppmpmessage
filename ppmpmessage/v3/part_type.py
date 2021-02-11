from enum import Enum

class PartType(Enum):
    SINGLE = "SINGLE"
    BATCH = "BATCH"

    def __getstate__(self):
        return self.value
