# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # inorder tree+iterative
    
    def order(self,root):
        result,stack = [],[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return result
            else:
                node=stack.pop()
                result.append(node.val)
                if node.left != None and node.right == None:
                    result.append(None)
                root=node.right

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        order_p=self.order(p)
        order_q=self.order(q)
        if order_p == order_q:
            return True
        else:
            return False
        
#Runtime: 36 ms