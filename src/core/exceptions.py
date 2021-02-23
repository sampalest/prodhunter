class ResponseErrorException(Exception):
    """
    Raise when response is not OK
    """
    pass

class ParseRequestException(Exception):
    """
    Raise when response is not OK
    """
    pass

class ObjectDoesNotExist(Exception):
    """
    Raise when object does not exist
    """
    pass