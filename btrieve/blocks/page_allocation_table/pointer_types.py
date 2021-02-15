from enum import Enum


class PointerTypes(Enum):
    END         = b"\x00\x00"
    UNKNOWN_1   = b"\x00\x80"
    UNKNOWN_2   = b"\x00\x81"
    UNKNOWN_3   = b"\x00\x82"
    UNKNOWN_4   = b"\x00\x83"
    UNKNOWN_5   = b"\x00\x84"
    UNKNOWN_6   = b"\x00A"
    DATA        = b"\x00D"
    UNKNOWN_7   = b"\x00E"
