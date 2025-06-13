from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class IStack(ABC, Generic[T]):
    @abstractmethod
    def push(self, e: T):
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
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

class Stack(IStack, Generic[T]):
    def __init__(self):
        self._data = []

    def push(self, e: T):
        self._data.append(e)

    def pop(self) -> T:
        if self.empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if self.empty():
            raise IndexError("Peek from empty stack")
        return self._data[-1]

    def empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self):
        self._data.clear()

    def to_string(self) -> str:
        return str(self._data)
