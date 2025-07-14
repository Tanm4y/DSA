#Binary tree 
class TreeNode: 
    def __init__(self , val , left = None , right = None ):
        self.val = val
        self.left = left 
        self.right = right 

    def __str__(self):
        return str(self.val)
    


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


print(A)

#Rrecursive pre order traversal : DFS time : O(n) and space : O(n)

def in_order(node):
    if not node:
        return 
    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node=stk.pop()
        if node.right:stk.append(node.right)
        if node.left:stk.append(node.left)
        print(node)

    pre_order_iterative(A)

#Level order Traversal (BFS) Time : O(n) and Space : O(n)

from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

    level_order(A)
    
    #Check if value exists (DFS) TIme : O(N) and space : O(n)

    def search(node,target):
        if not node:
            return False 
        
        if node.val == target :
            return True
        
        return search(node.left , target ) or search(node.right ,  target)
    
    print(search(A , 11))

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print(A2)

in_order(A2)

# Time: O(log n), Space: O(log n)
def search_bst(node, target):
  if not node:
    return False

  if node.val == target:
    return True

  if target < node.val: return search_bst(node.left, target)
  else: return search_bst(node.right, target)

print(search_bst(A2, -1))