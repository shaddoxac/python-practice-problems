# This problem was asked by Microsoft.

# Let's represent an integer in a linked list format by having each node represent a digit in the number.
# The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list format.

# For example, given

# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:

# 4 -> 2 -> 1

from typing import Optional

class Node:
    def __init__(self, val: int, next: Optional["Node"] = None):
        self.val = val
        self.next = next

    def get_value(self):
        if self.next:
            return self.val + self.next.get_value() * 10
        return self.val


nodeA = Node(val=1, next=Node(val=2, next=Node(val=3, next=Node(val=4, next=Node(val=5)))))
assert(nodeA.get_value() == 54321)

nodeB = Node(val=9, next=Node(val=9))
assert(nodeB.get_value() == 99)

nodeC = Node(val=5, next=Node(val=2))
assert(nodeC.get_value() == 25)


def add_nodes(add1: Node, add2: Node) -> Node:
    new_sum = add1.get_value() + add2.get_value()
    if new_sum < 0:
        positive_or_negative_multiplier = -1  # this will be multiplied by all values to make negative when appropriate
        new_sum = new_sum * -1
    else:
        positive_or_negative_multiplier = 1
    cur_node = None
    root = None
    while new_sum > 0:
        cur_val = (new_sum % 10) * positive_or_negative_multiplier
        if cur_node:
            cur_node.next = Node(val=cur_val)
            cur_node = cur_node.next
        else:
            cur_node = Node(val=cur_val)
            root = cur_node
        new_sum = int(new_sum / 10)
    return root


added_nodes = add_nodes(nodeB, nodeC)

assert(added_nodes.val == 4)
assert(added_nodes.next.val == 2)
assert(added_nodes.next.next.val == 1)



# the provided solution is interesting - rather than computing the sums and constructing a new set of nodes,
# they basically zip the two linked lists together and add

def add_nodes2(node0: Optional[Node], node1: Optional[Node], carry: int=0):
    if not node0 and not node1 and not carry:
        return None

    node0_val = node0.val if node0 else 0
    node1_val = node1.val if node1 else 0
    total = node0_val + node1_val + carry

    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total >= 10 else 0

    return Node(val=total % 10, next=add_nodes2(node0_next, node1_next, carry_next))


added_nodes2 = add_nodes(nodeB, nodeC)

assert(added_nodes2.val == 4)
assert(added_nodes2.next.val == 2)
assert(added_nodes2.next.next.val == 1)
