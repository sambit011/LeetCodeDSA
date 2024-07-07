class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2[:]
            return

        if n == 0:
            return

        j = 0
        for i in range(m):
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                nums2.sort()
        nums1[m:] = nums2