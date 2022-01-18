import logging
import warnings

_logger = logging.getLogger(__name__)

""" it is custom exception """
class BusinessException(Exception):

    """ 
    it is constructor of custom exception 
     :param code: code of message exception
    :param message: exception message and frontend modal content
    """
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code