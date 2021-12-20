from typing import (
    Coroutine,
    Callable,
    Optional,
)

from views import View, ViewCallback


__all__ = (
    "path",
)

def path(endpoint: str, function: Callable[..., Coroutine], *, name: Optional[str] = None) -> View:
    """Creates a View object out of the given args/kwargs.

    :param endpoint: The url that this view will be binded to.
    :type endpoint: str
    :param function: The Awaitable function that is called when the route is visited.
    :type function: Callable[..., Coroutine]
    :param name: An optional name to bind to the view, defaults to None
    :type name: Optional[str], optional
    :return: A clean object containing all the information that this path function takes into consideration.
    :rtype: View
    """
    view_callback = ViewCallback(function)
    view = View(
        endpoint,
        view_callback,
        assigned_name=name
    )
    return view
