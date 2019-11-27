# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    l = []
    
    def fixtree(self, root: TreeNode):
        if not root:
            return None
        
        if root.left:
            self.fixtree(root.left)
        
        self.l.append(root.val)
        
        if root.right:
            self.fixtree(root.right)
            
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.l = []
        self.fixtree(root)
        temp = self.l
        root = TreeNode(temp[0])
        curr = root
        
        for ele in temp[1:]:
            curr.right = TreeNode(ele)
            curr = curr.right
            
        return root
       