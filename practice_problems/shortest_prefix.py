# This problem was asked by Square.

# Given a list of words, return the shortest unique prefix of each word. For example, given the list:
# dog
# cat
# apple
# apricot
# fish

# Return the list:
# d
# c
# app
# apr
# f

from typing import Dict, List

class TrieNode:
    def __init__(self):
        # one letter -> trienode
        self.value_dict: Dict[str, TrieNode] = {}

    def add(self, string: str):
        if len(string) == 0:
            return
        if string[0] not in self.value_dict:
            self.value_dict[string[0]] = TrieNode()
        self.value_dict[string[0]].add(string[1:])

    def size(self) -> int:
        return len(self.value_dict.keys())

    def is_tail(self):
        if self.size() > 1:
            return False
        elif self.size() == 0:
            return True
        else:
            for key in self.value_dict.keys():
                # only one key, so can just return the result here
                return self.value_dict[key].is_tail()


def shortest_unique_prefix(input_list: List[str]) -> List[str]:
    root = TrieNode()
    for word in input_list:
        root.add(word)

    ret = iterate(root, prefix="")
    
    return ret

def iterate(node: TrieNode, prefix: str) -> List[str]:
    ret = []
    for start_char in node.value_dict.keys():
        cur_node = node.value_dict[start_char]
        if cur_node.is_tail():
            ret.append(prefix + start_char)
        else:
            ret = ret + iterate(cur_node, prefix = prefix + start_char)
    return ret


ret = shortest_unique_prefix([
        "dog",
        "cat",
        "apple",
        "apricot",
        "fish"
    ])

assert(len(ret) == 5)
assert("d" in ret)
assert("c" in ret)
assert("app" in ret)
assert("apr" in ret)
assert("f" in ret)
