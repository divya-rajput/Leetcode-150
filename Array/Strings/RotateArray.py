class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time- O(n), Space- O(1)
        # Leetcode-189: https://leetcode.com/problems/rotate-array/
        # Copy the below code logic
        k = k % len(nums)
        l,r = 0, len(nums)-1
        while  l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1, r - 1
        l,r = 0, k-1
        while  l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1, r - 1
        l,r = k, len(nums)-1
        while  l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1, r - 1