class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_1 in range(len(nums)):
            for index_2 in range(index_1 +1 , len(nums)):
                    if nums[index_1] + nums[index_2] == target:
                        return [index_1,index_2]