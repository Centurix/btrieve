import struct
from .field_types import FieldTypes


class V6Field:
    """
    Provide metadata services for the schema
    """
    def __init__(
        self,
        record_id, 
        file_id, 
        field_name, 
        data_type, 
        offset, 
        size, 
        decimal_places
    ):
        self.record_id = record_id
        self.file_id = file_id
        self.field_name = field_name
        self.data_type = data_type
        self.offset = offset
        self.size = size
        self.decimal_places = decimal_places
    
    @classmethod
    def from_raw_record(cls, raw_record):
        record_id, file_id, field_name, data_type, offset, size, decimal_places = struct.unpack(
            '< H H 20s b H H b',
            raw_record[:30]
        )

        if field_name[:1] == "\x00":
            return None

        return cls(
            record_id, 
            file_id, 
            field_name.strip(), 
            FieldTypes(data_type), 
            offset, 
            size, 
            decimal_places
        )
