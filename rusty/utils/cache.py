from typing import (
    Dict,
    Any,
    Optional
)


class LockedCache:
    def __init__(self):
        self._internal: Dict[Any, Any] = {}
        self.__locked: bool = False

    def lock(self) -> None:
        """Locks the cache.

        :raises ValueError: Raises a ValueError if the cache is already locked.
        :return: Returns None.
        :rtype: None
        """
        if self.__locked is True:
            raise ValueError("Cache is already locked")

        self.__locked = True
        return None

    def get(self, key: str) -> Optional[Any]:
        """Gets a value from the cache regardless of whether the cache is locked. This is by design.

        :param key: The key attached to the value in the cache.
        :type key: str
        :return: It could be None, and it could also be a value.
        :rtype: Optional[Any]
        """
        
        value = self._internal.get(key, None)
        return value

    def insert(self, key: Any, value: Any, *, upsert: bool = False) -> Dict[Any, Any]:
        """Insert/Upsert a key and value to the cache.

        :param key: The key to assign a value to in the cache. This does not have to be a string.
        :type key: Any
        :param value: The value that is assigned to the key. This does not have to be a string.
        :type value: Any
        :param upsert: Whether to update if the key already exists, defaults to False
        :type upsert: bool, optional
        :raises ValueError: Raises a value error if upsert is False and the key already exists.
        :return: Returns a simple abstraction of your given values. Example: Key: 1, Value: 2 - Abstraction: {1: 2}
        :rtype: Dict[Any, Any]
        """

        _abstraction = {key: value}
        if key in self._internal:
            if upsert is True:
                pass
            else:
                raise ValueError("Key already exists. Consider using the upsert kwarg instead.")

        self._internal[key] = value
        return _abstraction
