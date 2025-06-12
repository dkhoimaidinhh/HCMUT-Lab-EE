from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IList(ABC, Generic[T]):
    @abstractmethod
    def add(self, e: T):
        pass

    @abstractmethod
    def add_at(self, index: int, e: T):
        pass

    @abstractmethod
    def remove_at(self, index: int) -> T:
        pass

    @abstractmethod
    def remove_item(self, item: T) -> bool:
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
    def get(self, index: int) -> T:
        pass

    @abstractmethod
    def set(self, index: int, e: T):
        pass

    @abstractmethod
    def index_of(self, item: T) -> int:
        pass

    @abstractmethod
    def contains(self, item: T) -> bool:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass

class XArraylist(IList, Generic[T]):
    def __init__(self):
        self._data = []

    def add(self, e: T):
        self._data.append(e)

    def add_at(self, index: int, e: T):
        if 0 <= index <= len(self._data):
            self._data.insert(index, e)
        else:
            raise IndexError("Index out of range.")

    def remove_at(self, index: int) -> T:
        if 0 <= index < len(self._data):
            return self._data.pop(index)
        else:
            raise IndexError("Index out of range.")

    def remove_item(self, item: T) -> bool:
        if (not self.contains(item)):
            return False
        self._data.remove(item)
        return True

    def empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self):
        self._data.clear()

    def get(self, index: int) -> T:
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Index out of range.")

    def set(self, index: int, e: T):
        if 0 <= index < len(self._data):
            self._data[index] = e
        else:
            raise IndexError("Index out of range.")

    def index_of(self, item: T) -> int:
        if self.contains(item):
            return self._data.index(item)
        else:
            return -1

    def contains(self, item: T) -> bool:
        return item in self._data

    def to_string(self) -> str:
        return str(self._data)

# Example usage
if __name__ == "__main__":
    arr = XArraylist[int]()
    arr.add(1)
    arr.add(2)
    arr.add(3)
    print("ArrayList:", arr.to_string())
    arr.remove_item(2)
    print("After removing 2:", arr.to_string())
    print("Element at index 1:", arr.get(1))
    arr.set(0, 10)
    print("After setting index 0 to 10:", arr.to_string())
    print("Size:", arr.size())