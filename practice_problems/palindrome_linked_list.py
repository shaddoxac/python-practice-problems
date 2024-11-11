# This problem was asked by Google.

# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

from typing import Optional

class Node:
    def __init__(self, val: str):
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def add_next(self, next: "Node"):
        self.next = next
        next.prev = self

def is_palindrome_helper(head: Node, tail: Node) -> bool:
    if head == tail:
        return True
    if head.val == tail.val:
        return is_palindrome_helper(head.next, tail.prev)
    return False

def is_palindrome(head: Node) -> bool:
    tail = head
    while tail.next:
        tail = tail.next
    return is_palindrome_helper(head, tail)


head = Node(1)
head.add_next(Node(4))
assert(not is_palindrome(head))

head.next.add_next(Node(3))
head.next.next.add_next(Node(4))
head.next.next.next.add_next(Node(1))

assert(is_palindrome(head))
