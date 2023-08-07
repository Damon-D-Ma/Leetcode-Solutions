class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        longest = 0
        while r < len(nums):
            if nums[r] != 1:
                l = r + 1
            else:
                if r - l + 1 > longest:
                    longest = r - l + 1
            r += 1    

        return longest