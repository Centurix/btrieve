from .btrieve_file_exception import BtrieveFileException


class InvalidFileControlRecord(BtrieveFileException):
    """
    Something wrong with the FCR
    """
    pass
