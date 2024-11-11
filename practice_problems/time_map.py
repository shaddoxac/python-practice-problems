# This problem was asked by Stripe.

# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

# It should contain the following methods:

# set(key, value, time): sets key to value for t = time.
# get(key, time): gets the key at t = time.
# The map should work like this.
# If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time.
# In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

from typing import Optional

class Node:
    def __init__(self, value, time):
        self.value = value
        self.time = time
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def add(self, node: "Node"):
        if node.time > self.time:
            if self.next:
                self.next.add(node)
            else:
                self.next = node
                node.prev = self
        elif node.time == self.time:
            self.value = node.value
        else:
            if self.prev:
                self.prev.next = node
                node.prev = self.prev
            node.next = self
            self.prev = node

    def get(self, time) -> Optional["Node"]:
        if self.time > time:
            # no value at this time
            return None
        elif not self.next:
            # most recent record
            return self
        elif self.next.time > time:
            # next record is later, we must be at the right spot
            return self
        else:
            # keep going
            return self.next.get(time) 

class TimeMap:
    def __init__(self):
        # map key -> linked list, find relevant record
        self.map_tree = {}

    def set(self, key, value, time):
        value_node = Node(value, time)
        if key in self.map_tree:
            self.map_tree[key].add(value_node)
        else:
            self.map_tree[key] = value_node

    def get(self, key, time):
        if key not in self.map_tree:
            return None
        ret = self.map_tree[key].get(time)
        if ret:
            return ret.value
        return None

d = TimeMap()


d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
assert(d.get(1, 1) == 1) # get key 1 at time 1 should be 1
assert(d.get(1, 3) == 2) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
assert(d.get(1, -1) == None) # get key 1 at time 0 should be null
assert(d.get(1, 10) == 1) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
assert(d.get(1, 0) == 2) # get key 1 at time 0 should be 2
