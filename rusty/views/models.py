from typing import (
    Callable, 
    List, 
    Dict,
    Any,
    Optional,
    Tuple
)

from .exceptions import ViewCallbackFailed


__all__: Tuple[str] = (
    "ViewCallback",
    "CallbackResult",
    "View"
)

class ViewCallback:
    def __init__(
        self,
        function: Callable
    ):
        self.func = function


class CallbackResult:
    def __init__(
        self,
        parent: ViewCallback,
        result: Any
    ):
        self.callback = parent
        self.result = result


class View:
    def __init__(
        self,
        endpoint: str,
        callback: ViewCallback, 
        *,
        assigned_name: Optional[str] = None
    ):
        self.endpoint = endpoint
        self.callback = callback
        self.name = assigned_name

    async def execute_callback(self, *args, **kwargs) -> Optional[CallbackResult]:

        _callback = self.callback.func(*args, **kwargs)
        _result = None

        try:
            _result = await _callback
        except Exception as exc:
            raise ViewCallbackFailed(exc)
        else:
            cb_result = CallbackResult(self.callback, _result)
            return cb_result
    