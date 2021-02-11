from enum import Enum

class ValueType(Enum):
    BASE64 = "BASE64"
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"
    OTHER = "OTHER"
    REF = "REF"
    STRING = "STRING"

    def __getstate__(self):
        return self.value
