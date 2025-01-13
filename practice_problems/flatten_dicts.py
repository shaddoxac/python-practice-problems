# This problem was asked by Stripe.

# Write a function to flatten a nested dictionary. Namespace the keys with a period.

# For example, given the following dictionary:

# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:

# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.

from typing import Dict, Optional


def flatten_nested_dict(dict: Dict) -> Dict:
    return flatten_helper(dict, ret={}, prefix=None)


def flatten_helper(dict: Dict, ret: Dict, prefix: Optional[str]) -> Dict:
    for key in dict.keys():
        new_prefix = key if not prefix else f"{prefix}.{key}"
        if isinstance(dict[key], Dict):
            ret = flatten_helper(dict[key], ret=ret, prefix=new_prefix)
        else:
            ret[new_prefix] = dict[key]
    return ret


ret = flatten_nested_dict({"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}})

assert ret["key"] == 3
assert ret["foo.a"] == 5
assert ret["foo.bar.baz"] == 8
