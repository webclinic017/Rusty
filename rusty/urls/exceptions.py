from typing import Tuple


__all__: Tuple[str, ...] = (
    "UrlException",
    "TypeConversionFailed"
)

class UrlException(Exception):
    """
    The Exception that all url based exceptions will inherit from.
    """

class TypeConversionFailed(UrlException):
    """
    The error that is raised when a type conversion fails in a url path argument.
    """

    def __init__(
        self,
        argument: str,
        tried_type: type
    ):
        self.argument = argument
        self.type = tried_type


    def __str__(self) -> str:
        return "Failed to convert {0.argument} into a {0.type} type".format(self)