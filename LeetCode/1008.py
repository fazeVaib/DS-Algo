# Construct Binary Search Tree from Preorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stk = [root]

        for ele in preorder[1:]:
            if ele < stk[-1].val:
                stk[-1].left = TreeNode(ele)
                stk.append(stk[-1].left)
            else:
                while stk and stk[-1].val < ele:
                    t = stk.pop()
                t.right = TreeNode(ele)
                stk.append(t.right)

        return root
