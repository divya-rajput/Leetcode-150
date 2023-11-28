class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-209: https://leetcode.com/problems/minimum-size-subarray-sum/
        # Copy the below code logic
        l, total = 0,0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r-l+1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res