class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return 1

        l = 0 #index of the last found unique number
        r = 1 #search index/pointer
        while r < len(nums):
            if nums[r] > nums[l]:
                temp = nums[l+1]
                nums[l+1] = nums[r]
                nums[r] = nums[l+1]
                l += 1
                r += 1
            else:
                r += 1
        
        
        
        return l+1
                