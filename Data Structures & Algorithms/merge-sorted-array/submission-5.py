class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1 # last position in nums1 (position to be filled)
        i = m - 1 # last valid element in nums1
        j = n - 1 # last element in nums2

        while i >= 0 and j >= 0: 
            # If nums1's element is larger, place it at the end of nums1
            # Otherwise, place nums2's element at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        # Copy remaining elements of nums2 into nums1
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1

