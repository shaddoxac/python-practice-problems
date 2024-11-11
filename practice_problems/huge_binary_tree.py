# This problem was asked by Jane Street.

# Generate a finite, but an arbitrarily large binary tree quickly in O(1).

# That is, generate() should return a tree whose size is unbounded but finite.

from random import random, randint
from typing import Optional

class HugeTreeNode:
    def __init__(self):
        self.val: int = randint(0, 1000)
        self._left: Optional[HugeTreeNode] = None
        self._right: Optional[HugeTreeNode] = None
        self.random_factor = 0.5

        self._has_left = False
        self._has_right = False
    
    @property
    def left(self) -> Optional["HugeTreeNode"]:
        if not self._left:
            if random() < self.random_factor:
                self._left = HugeTreeNode()
        return self._left
    
    @property
    def right(self) -> Optional["HugeTreeNode"]:
        if not self._right:
            if random() < self.random_factor:
                self._right = HugeTreeNode()
        return self._right


def generate() -> HugeTreeNode:
    return HugeTreeNode()

