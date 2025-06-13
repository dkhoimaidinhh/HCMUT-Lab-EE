from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class IQueue(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, e: T):
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass

    @abstractmethod
    def empty(self) -> bool:
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

class Queue(IQueue, Generic[T]):
    def __init__(self):
        self._data = []

    def enqueue(self, e: T):
        self._data.append(e)

    def dequeue(self) -> T:
        if self.empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.pop(0)

    def front(self) -> T:
        if self.empty():
            raise IndexError("Front from empty queue")
        return self._data[0]

    def empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self):
        self._data.clear()

    def to_string(self) -> str:
        return str(self._data)
