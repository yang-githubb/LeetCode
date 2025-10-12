class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0

        for number in range(1,len(nums)):
            if nums[number] != nums[i]:
                i += 1
                nums[i] = nums[number]
        
        return i+1
