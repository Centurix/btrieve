from .v6_page_allocation_table import V6PageAllocationTable
from .v8_page_allocation_table import V8PageAllocationTable


class PageAllocationTableFactory:
    _fcr_versions = [
        None,
        None,
        None,
        None,
        None,
        None,
        V6PageAllocationTable,
        None,
        V8PageAllocationTable
    ]

    @classmethod
    def from_block(cls, block):
        """
        Return a PAT
        """
        return V6PageAllocationTable.from_block(block)

    @classmethod
    def from_blocks(cls, block_1, block_2):
        """
        Find the latest block and return the FCR
        """
        return V6PageAllocationTable.from_blocks(block_1, block_2)
