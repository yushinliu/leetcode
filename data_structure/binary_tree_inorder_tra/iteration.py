# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   #iteration method
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [],[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return result
            else:
                node=stack.pop()
                result.append(node.val)
                root=node.right
                
                '''
                list=[(True,[1,2,3,4])]
                a,b=list.pop(0)
                '''