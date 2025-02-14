# This problem was asked by LinkedIn.

# Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

# For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.

from typing import List, Tuple

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def partition_by_k(linked_list: Node, k: int) -> Node:
    # group elements by segment
    lesser = []
    greater_or_equal = []
    while linked_list:
        if linked_list.val < k:
            lesser.append(linked_list)
        else:
            greater_or_equal.append(linked_list)
        linked_list = linked_list.next

    (lesser_head, lesser_tail) = list_to_nodes(lesser)
    (greater_head, _) = list_to_nodes(greater_or_equal)

    if not lesser_head:
        return greater_head
    if not greater_head:
        return lesser_head
    # both lesser tail and greater head exist, connect them
    lesser_tail.next = greater_head
    return lesser_head

def list_to_nodes(list: List[Node]) -> Tuple[Node, Node]:
    if len(list) == 0:
        return (None, None)
    head = list[0]
    cur_node = head
    for node in list[1:]:
        cur_node.next = node
        cur_node = node
    cur_node.next = None
    return (head, cur_node)


head = Node(5, Node(1, Node(8, Node(0, Node(3)))))
partitioned = partition_by_k(head, 3)

for i in range(2):
    assert(partitioned.val < 3)
    partitioned = partitioned.next
while partitioned:
    assert(partitioned.val >= 3)
    partitioned = partitioned.next
