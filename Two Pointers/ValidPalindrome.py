class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time- O(n), Space- O(1)
        # Leetcode-125: https://leetcode.com/problems/valid-palindrome/
        # Copy the below code logic
        left = 0
        right = len(s)-1
        while left < right :
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True