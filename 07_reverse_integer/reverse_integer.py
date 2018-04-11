import operator
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = abs(x)
            r = int('-'+str(x)[::-1])
            return r if -2147483648<r<2147483648 else 0
        else:
            r = int(str(x)[::-1])
            return r if -2147483648<r<2147483648 else 0
        