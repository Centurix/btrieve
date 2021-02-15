import struct
from .file_control_record import FileControlRecord
from exceptions import InvalidFileControlRecord


class V6FileControlRecord(FileControlRecord):
    _block_size = 256

    def __init__(
        self, 
        magic, 
        usage_count, 
        page_blocks, 
        record_size, 
        record_physical_size,
        total_records
    ):
        super().__init__()
        self.magic = magic
        self.usage_count = usage_count
        self.page_blocks = page_blocks
        self.record_size = record_size
        self.record_physical_size = record_physical_size
        self.total_records = total_records

    @property
    def page_size(self):
        return self.page_blocks * self._block_size

    @property
    def page_records(self):
        return (self.page_blocks * self._block_size) // self.record_physical_size

    """
    Factories
    """
    @classmethod
    def from_block(cls, block):
        # magic, = struct.unpack("< 2s", block[:2])
        # _, usage_count = struct.unpack("< 4s L", block[:8])
        # _, page_blocks = struct.unpack('< 9s b', block[:10])
        # _, record_size = struct.unpack('< 22s H', block[:24])
        # _, record_physical_size = struct.unpack('< 24s H', block[:26])
        # _, total_records = struct.unpack('< 28s I', block[:32])

        magic, _, usage_count, _, page_blocks, _, record_size, record_physical_size, _, total_records = struct.unpack("< 2s 2s L b b 12s H H 2s I", block[:32])

        return cls(
            magic, 
            usage_count, 
            page_blocks, 
            record_size, 
            record_physical_size,
            total_records
        )

    @classmethod
    def from_blocks(cls, block_1, block_2):
        """
        Figure out which block is later
        """
        _, block_1_version = struct.unpack('< 4s L', block_1[:8])
        _, block_2_version = struct.unpack('< 4s L', block_2[:8])

        if block_1_version > block_2_version:
            return cls.from_block(block_1)

        return cls.from_block(block_2)
