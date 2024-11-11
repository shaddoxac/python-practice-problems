# This problem was asked by Airbnb.

# We're given a hashmap associating each courseId key with a list of courseIds values,
# which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.

# Return null if there is no such ordering.

# For example, given {
#     'CSC300': ['CSC100', 'CSC200'],
#     'CSC200': ['CSC100'],
#     'CSC100': []
# }, should return ['CSC100', 'CSC200', 'CSCS300'].

from typing import Dict, List, Optional, Set

def courses(courseMap: Dict[str, List[str]]) -> Optional[List[str]]:
    taken_classes: Set[str] = set()
    ret = []
    while courseMap:
        added_course = False
        for (key, v) in courseMap.items():
            if not v or set(v).issubset(taken_classes):
                added_course = True
                taken_classes.add(key)
                ret.append(key)
                courseMap.pop(key)
                break

        if not added_course:
            return None

    return ret

assert(courses({
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}) == ['CSC100', 'CSC200', 'CSC300'])

assert(courses({
    'CSC300': ['CSC100', 'CSC400'],
    'CSC200': ['CSC100'],
    'CSC100': []
}) == None)
