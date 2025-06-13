from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class IDLinkedList(ABC, Generic[T]):
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

class DNode(Generic[T]):
    def __init__(self, value: T, prev: Optional['DNode[T]'] = None, next: Optional['DNode[T]'] = None):
        self.value = value
        self.prev = prev
        self.next = next

class DLinkedList(IDLinkedList, Generic[T]):
    def __init__(self):
        self.head: Optional[DNode[T]] = None
        self.tail: Optional[DNode[T]] = None
        self._size = 0

    def add(self, e: T):
        new_node = DNode(e)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def add_at(self, index: int, e: T):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        new_node = DNode(e)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif index == self._size:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
        self._size += 1

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if removed == self.tail:
                self.tail = None
        elif index == self._size - 1:
            removed = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            if removed == self.head:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removed = current
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        self._size -= 1
        return removed.value

    def remove_item(self, item: T) -> bool:
        current = self.head
        while current:
            if current.value == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return True
            current = current.next
        return False

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def get(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index: int, e: T):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = e

    def index_of(self, item: T) -> int:
        current = self.head
        idx = 0
        while current:
            if current.value == item:
                return idx
            current = current.next
            idx += 1
        return -1

    def contains(self, item: T) -> bool:
        return self.index_of(item) != -1

    def to_string(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values) if values else "Empty List"
