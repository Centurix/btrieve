import struct


class V6Table:
    def __init__(self, table_id, table_name, location, flags):
        self.table_id = table_id
        self.table_name = table_name
        self.location = location
        self.flags = flags

    @classmethod
    def from_raw_record(cls, raw_record):
        """
        Name: b'Xf$Id'
        Type: FieldTypes.INTEGER
        Size: 2
        Offset: 0

        Name: b'Xf$Name'
        Type: FieldTypes.CHAR
        Size: 20
        Offset: 2

        Name: b'Xf$Loc'
        Type: FieldTypes.CHAR
        Size: 64
        Offset: 22

        Name: b'Xf$Flags'
        Type: FieldTypes.INTEGER
        Size: 1
        Offset: 86
        """
        table_id, table_name, location, flags = struct.unpack(
            '< H 20s 64s b',
            raw_record[:87]
        )
        return cls(table_id, table_name.strip(), location.strip(), flags)
