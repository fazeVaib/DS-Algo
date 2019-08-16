import sys
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getDepth(root, depth):
    if root:
        dl = getDepth(root.left, depth+1)
        dr = getDepth(root.right, depth+1)
        depth = max(dl, dr)
    else:
        depth -= 1
    return depth

def swap(root, depth, height):
    if root:
        if depth == height:
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            swap(root.left, depth, height+1)
            swap(root.right, depth, height+1)


def inorderTraversal(root, s):
    if root:
        sl = inorderTraversal(root.left, s)
        sc = root.val
        sr = inorderTraversal(root.right, s)
        return sl + sc + sr
        
    else:
        return ''


n = int(input())
Tree = [Node(i) for i in range(1, n+1)]
root = Tree[0]

for i in range(n):
    a, b = input().split(' ')
    a, b = [int(a)-1, int(b)-1]

    Tree[i].left = Tree[a] if a>0 else None
    Tree[i].right = Tree[b] if b>0 else None

depth = getDepth(root, 1)
# print(depth)

T = int(input())
for i in range(T):
    k = int(input())
    H = [k*i for i in range(1,n) if k*i <= depth]
    for height in H:
        swap(root, height, 1)
    
    print(inorderTraversal(root, ''))