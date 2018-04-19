class Solution:
    def isBalanced(self, root):  #recursive
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def depth(node):
            if not node:
                return 0 # leaves has no length
            left=depth(node.left)
            right=depth(node.right)
            if abs(left-right) > 1:
                raise Exception
            return max(left,right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False