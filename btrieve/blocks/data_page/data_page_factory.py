from .v6_data_page import V6DataPage


class DataPageFactory:
    @classmethod
    def from_fcr_and_block(cls, fcr, block):
        return V6DataPage.from_fcr_and_block(fcr, block)
