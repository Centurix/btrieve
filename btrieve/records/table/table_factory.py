from .v6_table import V6Table


class TableFactory:
    @classmethod
    def from_raw_record(cls, raw_record):
        return V6Table.from_raw_record(raw_record)
