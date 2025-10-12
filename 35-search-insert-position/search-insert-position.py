class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in nums:
            if i >= target:
                 return index
            else:
                index += 1
        return index