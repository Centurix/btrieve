import struct
from .v6_file_control_record import V6FileControlRecord
from .v8_file_control_record import V8FileControlRecord
from exceptions import InvalidFileControlRecord


class FileControlRecordFactory:
    _fcr_versions = [
        None,
        None,
        None,
        None,
        None,
        None,
        V6FileControlRecord,
        None,
        V8FileControlRecord
    ]

    @classmethod
    def version(cls, block):
        """
        Determine the version number of the FCR from the block data alone

        Use a combination of the magic number, V6 and V8 page sizes
        """
        magic, _, v6_page_size, _, v8_page_size = struct.unpack(
            '< 2s 7s b 33s b', 
            block[:44]
        )

        if magic != b"FC":
            return 5

        if v6_page_size > 0:
            return 6
        
        if v8_page_size > 0:
            return 8

    @classmethod
    def from_block(cls, block):
        """
        Return a FCR from raw block data
        """
        try:
            return cls._fcr_versions[cls.version(block)].from_block(block)
        except Exception as ex:
            raise InvalidFileControlRecord("Unsupported file version")

    @classmethod
    def from_blocks(cls, block_1, block_2):
        """
        Find the latest block and return the FCR
        """
        try:
            return cls._fcr_versions[cls.version(block_1)].from_blocks(block_1, block_2)
        except Exception as ex:
            raise InvalidFileControlRecord("Unsupported file version")
