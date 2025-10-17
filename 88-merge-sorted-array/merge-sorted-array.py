class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # i -> last index of valid data in nums1
        i = m - 1
        # j -> last index of nums2
        j = n - 1
        # k -> last index of nums1 (final write position)
        k = m + n - 1

        # While both arrays have elements left, place the larger of nums1[i], nums2[j] at nums1[k]
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2, copy them (nums1's remaining elements are already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1