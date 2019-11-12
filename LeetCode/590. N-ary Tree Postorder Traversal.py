# 590. N-ary Tree Postorder Traversal

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        d = [root]
        p = []

        while len(d) != 0 and root != None:
            n = d.pop()
            p.insert(0, n.val)
            d += n.children
        return p
