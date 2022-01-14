import logging
import warnings

_logger = logging.getLogger(__name__)
from exception_util.custom_exception import BusinessException

def exception_test(param):
    if param == 1:
        raise BusinessException("123","custom error exception")
    if param == 2:
        raise Exception("exception")

def main():
    print("start")
    try:
        exception_test(1)
    except BusinessException as customErr:
        _logger.error(customErr.get_message())
    except Exception as customErr:
        _logger.error(customErr)
    finally:
        print("finally")

if __name__ == "__main__":
    main()
