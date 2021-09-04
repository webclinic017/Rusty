from typing import Tuple

from starlette.requests import Request

from .exceptions import TypeConversionFailed


__all__: Tuple[str, ...] = (
    "Converter",
    "IntConverter"
)

class Converter:
    def __init__(self):
        ...

    async def convert(
        self,
        request: Request,
        argument: str
    ):
        raise NotImplementedError


class IntConverter(Converter):
    async def convert(self, _: Request, argument: str):
        try:
            _c = int(argument)
        except ValueError:
            raise TypeConversionFailed(argument, int)
        else:
            return _c