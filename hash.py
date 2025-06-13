from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class IHashTable(ABC, Generic[K, V]):
    @abstractmethod
    def put(self, key: K, value: V):
        pass

    @abstractmethod
    def get(self, key: K) -> Optional[V]:
        pass

    @abstractmethod
    def remove(self, key: K) -> bool:
        pass

    @abstractmethod
    def contains_key(self, key: K) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass

class HashTable(IHashTable, Generic[K, V]):
    def __init__(self):
        self._data = dict()

    def put(self, key: K, value: V):
        self._data[key] = value

    def get(self, key: K) -> Optional[V]:
        return self._data.get(key, None)

    def remove(self, key: K) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False

    def contains_key(self, key: K) -> bool:
        return key in self._data

    def size(self) -> int:
        return len(self._data)

    def clear(self):
        self._data.clear()

    def to_string(self) -> str:
        return str(self._data)
