from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class ITree(ABC, Generic[T]):
    @abstractmethod
    def insert(self, value: T):
        pass

    @abstractmethod
    def remove(self, value: T) -> bool:
        pass

    @abstractmethod
    def find(self, value: T) -> bool:
        pass

    @abstractmethod
    def min(self) -> Optional[T]:
        pass

    @abstractmethod
    def max(self) -> Optional[T]:
        pass

    @abstractmethod
    def inorder(self) -> list:
        pass

    @abstractmethod
    def preorder(self) -> list:
        pass

    @abstractmethod
    def postorder(self) -> list:
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

class TreeNode(Generic[T]):
    def __init__(self, value: T, left: Optional['TreeNode[T]'] = None, right: Optional['TreeNode[T]'] = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(ITree, Generic[T]):
    def __init__(self):
        self.root: Optional[TreeNode[T]] = None
        self._size = 0

    def insert(self, value: T):
        def _insert(node, value):
            if node is None:
                self._size += 1
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            # If value == node.value, do nothing (no duplicates)
            return node
        self.root = _insert(self.root, value)

    def remove(self, value: T) -> bool:
        def _remove(node, value):
            if node is None:
                return node, False
            if value < node.value:
                node.left, deleted = _remove(node.left, value)
            elif value > node.value:
                node.right, deleted = _remove(node.right, value)
            else:
                # Node to be deleted found
                if node.left is None:
                    self._size -= 1
                    return node.right, True
                elif node.right is None:
                    self._size -= 1
                    return node.left, True
                # Node with two children
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.value = temp.value
                node.right, _ = _remove(node.right, temp.value)
                deleted = True
            return node, deleted
        self.root, deleted = _remove(self.root, value)
        return deleted

    def find(self, value: T) -> bool:
        def _find(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _find(node.left, value)
            else:
                return _find(node.right, value)
        return _find(self.root, value)

    def min(self) -> Optional[T]:
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.value

    def max(self) -> Optional[T]:
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.value

    def inorder(self) -> list:
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self) -> list:
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self) -> list:
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        _postorder(self.root)
        return result

    def size(self) -> int:
        return self._size

    def clear(self):
        self.root = None
        self._size = 0

    def to_string(self) -> str:
        return 'Inorder: ' + str(self.inorder())

    def __str__(self):
        return self.to_string()
