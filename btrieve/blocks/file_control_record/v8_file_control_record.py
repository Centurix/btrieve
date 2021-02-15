import struct
from .file_control_record import FileControlRecord


class V8FileControlRecord(FileControlRecord):
    def __init__(self, magic, usage_count):
        super().__init__()
        self.magic = magic
        self.usage_count = usage_count

    @classmethod
    def from_block(cls, block):
        magic, = struct.unpack("< 2s", block[:2])
        if magic != b"FC":
            """
            We don't support < V6 records, yet.
            """
            raise InvalidFileControlRecord("Invalid magic number")

        usage_count = struct.unpack("< 4s L", block[:8])

        return cls(magic, usage_count)
