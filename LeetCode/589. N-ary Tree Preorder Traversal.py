# 589. N-ary Tree Preorder Traversal

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        d = deque()
        d.appendleft(root)
        if root:
            t = [root.val]
            while len(d) != 0:
                if len(root.children) > 0:
                    for i in reversed(root.children):
                        d.appendleft(i)

                root = d.popleft()
                t.append(root.val)
            return t[:-1]
        else:
            return None
