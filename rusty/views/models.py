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
        function: Callable,
        args: List[Any],
        kwargs: Dict[str, Any]
    ):
        self.func = function
        self.args = args
        self.kwargs = kwargs



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

    async def execute_callback(self) -> Optional[CallbackResult]:
        args = self.callback.args
        kwargs = self.callback.kwargs

        _callback = self.callback.func(*args, **kwargs)
        _result = None

        try:
            _result = await _callback
        except Exception as exc:
            raise ViewCallbackFailed(exc)
        else:
            cb_result = CallbackResult(self.callback, _result)
            return cb_result
    