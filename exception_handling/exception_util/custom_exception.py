import logging
import warnings

_logger = logging.getLogger(__name__)

class BusinessException(Exception):
    """ it is custom exception """

    def __init__(self, code, message):
        """
        :param message: exception message and frontend modal content
        """
        super().__init__(message)
        self.code = code
        self.message = message

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code