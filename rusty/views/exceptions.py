class ViewException(Exception):
    """
    The Exception that all views based exceptions will inherit from.
    """

class ViewCallbackFailed(ViewException):
    """
    The exception that is raised when a view's callback fails to run.
    """
    def __init__(
        self,
        error: Exception
    ):
        self._error = error

    def __str__(self) -> str:
        e = str(self._error)
        return e

    @property
    def original(self) -> Exception:
        return self._error