from .v6_field import V6Field


class FieldFactory:
    @classmethod
    def from_raw_record(cls, raw_record):
        return V6Field.from_raw_record(raw_record)
