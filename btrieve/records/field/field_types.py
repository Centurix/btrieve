from enum import Enum


class FieldTypes(Enum):
    UNKNOWN_0       = -1
    CHAR            = 0
    INTEGER         = 1
    UNKNOWN_1       = 2
    DATE            = 3  # DDMMYYYY
    UNKNOWN_2       = 4  # TIME? SIZE=4 HHMM?
    DECIMAL         = 5
    UNKNOWN_3       = 6
    UNKNOWN_4       = 7
    UNKNOWN_5       = 8
    UNKNOWN_6       = 9
    UNKNOWN_7       = 10
    ZSTRING         = 11  # codepage 437
    UNKNOWN_8       = 12
    UNKNOWN_9       = 13
    UNSIGNED_BINARY = 14
    UNKNOWN_10      = 15
    UNKNOWN_11      = 16
    UNKNOWN_12      = 17
    UNKNOWN_13      = 18
