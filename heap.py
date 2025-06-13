from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')

class IHeap(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T):
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

class Heap(IHeap, Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    def push(self, item: T):
        # Add item and maintain heap property (min-heap by default)
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        # Remove and return the smallest item (min-heap)
        if self.empty():
            raise IndexError("Pop from empty heap")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._sift_down(0)
        return item

    def peek(self) -> T:
        # Return the smallest item without removing it
        if self.empty():
            raise IndexError("Peek from empty heap")
        return self._data[0]

    def empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self):
        self._data.clear()

    def to_string(self) -> str:
        return str(self._data)

    def _sift_up(self, idx: int):
        # Move the item at idx up to maintain heap property
        parent = (idx - 1) // 2
        while idx > 0 and self._data[idx] < self._data[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx: int):
        # Move the item at idx down to maintain heap property
        n = len(self._data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i: int, j: int):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __str__(self):
        return self.to_string()

    def reheapup(self, idx: int):
        # Restore heap property by moving the item at idx up
        self._sift_up(idx)

    def reheapdown(self, idx: int):
        # Restore heap property by moving the item at idx down
        self._sift_down(idx)

    def delete(self, idx: int) -> T:
        # Remove and return the item at index idx
        if idx < 0 or idx >= len(self._data):
            raise IndexError("Index out of range")
        self._swap(idx, len(self._data) - 1)
        item = self._data.pop()
        if idx < len(self._data):
            self._sift_down(idx)
            self._sift_up(idx)
        return item

    def build_heap(self, arr: List[T]):
        # Build a heap from an arbitrary list
        self._data = arr[:]
        n = len(self._data)
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)

    def insert(self, item: T):
        # Alias for push
        self.push(item)

    def heapsort(self) -> List[T]:
        # Return a sorted list using heap sort (does not modify the original heap)
        copied = self._data[:]
        result = []
        n = len(copied)
        # Build heap in-place
        for i in range((n // 2) - 1, -1, -1):
            self._heapsort_sift_down(copied, i, n)
        for _ in range(n):
            copied[0], copied[-1] = copied[-1], copied[0]
            result.append(copied.pop())
            self._heapsort_sift_down(copied, 0, len(copied))
        return result

    def _heapsort_sift_down(self, arr: List[T], idx: int, n: int):
        # Helper for heapsort to maintain heap property in a given array
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and arr[left] < arr[smallest]:
                smallest = left
            if right < n and arr[right] < arr[smallest]:
                smallest = right
            if smallest == idx:
                break
            arr[idx], arr[smallest] = arr[smallest], arr[idx]
            idx = smallest
