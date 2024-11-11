# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

from typing import Any, Dict, Optional

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class LRU:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.node_map: Dict[Any, Node] = {}
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            if node.next:
                node.next.prev = node.prev
            else: # this must be the tail as it has no next
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            self.add_to_head(node)
            return node.value
        else:
            return None
    
    def set(self, key, value):
        new_node = Node(key, value)
        if self.head is None:  # no records in table
            self.head = new_node
            self.tail = new_node
        elif len(self.node_map) < self.cache_size: # some records, but not full yet
            self.add_to_head(new_node)
        else: # full, drop last record and add new one
            del self.node_map[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None
            self.add_to_head(new_node)
        self.node_map[key] = new_node

    def add_to_head(self, node: Node):
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
    

lru = LRU(cache_size = 3)
lru.set("a", 1)
lru.set("b", 2)
lru.set("c", 3)
assert(lru.get("a") == 1)
lru.set("d", 4)
assert(lru.get("d") == 4)
assert(lru.get("c") == 3)
assert(lru.get("b") is None)
