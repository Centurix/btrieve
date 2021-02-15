import struct
from .pointer_types import PointerTypes


class V6PageAllocationTable:
    def __init__(self, pointers):
        # super().__init__()
        self.pointers = pointers

    """
    Factories
    """
    @classmethod
    def from_block(cls, block):
        """
        Given the PAT block, build a list of pointers
        """
        pat_pointers = block[8:]
        pointers = list()
        for i in range(0, len(pat_pointers), 4):
            ptype, poffset = struct.unpack('< 2s H', pat_pointers[i:i + 4])
            if ptype == PointerTypes.END.value:
                break

            pointers.append((PointerTypes(ptype), poffset))

        return cls(pointers)

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
