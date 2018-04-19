# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:  # the recrusive method
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        self.helper(root,result)
        return result
    
    def helper(self,root,result):
        if root:
            self.helper(root.left,result)
            result.append(root.val)
            self.helper(root.right,result)