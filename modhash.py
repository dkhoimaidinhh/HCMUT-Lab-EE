from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class IModHashTable(ABC, Generic[K, V]):
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

class ModHashTable(IModHashTable, Generic[K, V]):
    def __init__(self, capacity=10):
        # Initialize the hash table with a fixed number of buckets (capacity)
        self._capacity = capacity
        self._buckets = [[] for _ in range(capacity)]  # Each bucket is a list for separate chaining
        self._size = 0  # Number of key-value pairs in the table

    def _hash(self, key: K) -> int:
        # Compute the hash index for a given key using modulo division
        return hash(key) % self._capacity

    def put(self, key: K, value: V):
        # Insert or update the key-value pair in the hash table
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair
        self._size += 1

    def get(self, key: K) -> Optional[V]:
        # Retrieve the value associated with the given key, or None if not found
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key: K) -> bool:
        # Remove the key-value pair by key. Return True if removed, False if not found
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def contains_key(self, key: K) -> bool:
        # Check if the key exists in the hash table
        return self.get(key) is not None

    def size(self) -> int:
        # Return the number of key-value pairs in the hash table
        return self._size

    def clear(self):
        # Remove all key-value pairs from the hash table
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def to_string(self) -> str:
        # Return a string representation of the hash table (all buckets)
        result = []
        for i, bucket in enumerate(self._buckets):
            result.append(f"{i}: {bucket}")
        return "\n".join(result)

    def __str__(self):
        # Magic method for string representation, calls to_string()
        return self.to_string()
