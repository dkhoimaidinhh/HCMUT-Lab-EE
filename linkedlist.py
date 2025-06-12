from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class ILinkedList(ABC, Generic[T]):
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

class XLinkedList(ILinkedList, Generic[T]):
    def __init__(self):
        pass

    def add(self, e: T):
        pass

    def add_at(self, index: int, e: T):
        pass

    def remove_at(self, index: int) -> T:
        pass

    def remove_item(self, item: T) -> bool:
        pass

    def empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def clear(self):
        pass

    def get(self, index: int) -> T:
        pass

    def set(self, index: int, e: T):
        pass

    def index_of(self, item: T) -> int:
        pass

    def contains(self, item: T) -> bool:
        pass

    def to_string(self) -> str:
        pass

class Node(Generic[T]):
    def __init__(self, value: T, next: 'Node[T]' = None):
        self.value = value
        self.next = next

class TrueLinkedList(ILinkedList, Generic[T]):
    def __init__(self):
        self.head: Node[T] = None
        self.tail: Node[T] = None
        self._size = 0

    def add(self, e: T):
        new_node = Node(e)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def add_at(self, index: int, e: T):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range.")
        new_node = Node(e)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self._size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self._size += 1

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")
        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            removed_value = current.next.value
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        self._size -= 1
        return removed_value

    def remove_item(self, item: T) -> bool:
        current = self.head
        previous = None
        while current is not None:
            if current.value == item:
                if previous is None:
                    self.head = current.next
                    if self._size == 1:
                        self.tail = None
                else:
                    previous.next = current.next
                    if current.next is None:
                        self.tail = previous
                self._size -= 1
                return True
            previous = current
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
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index: int, e: T):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = e

    def index_of(self, item: T) -> int:
        current = self.head
        index = 0
        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, item: T) -> bool:
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def to_string(self) -> str:
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Empty List"