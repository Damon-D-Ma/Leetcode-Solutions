class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        
        nums.sort()
        return nums



#O(n) solution (my monkey brain likes the one above though because of how short the code is :))) :
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            nums[0] = nums[0]**2
        elif len(nums) == 2:
            nums[0] = nums[0]**2
            nums[1] = nums[1]**2
            if (nums[0] > nums[1]):
                nums[0], nums[1] = nums[1], nums[0]
        else:
            answer = []
            l = 0 # used to navigate negative numbers
            r = 0 # used to navigate positive numbers
            median = len(nums)-1
            for i in range(0, len(nums)):
                if nums[i] >= 0:
                    median = i
                    break
            l = median - 1
            r = median
            
            while 0 <= l and r < len(nums):
                left = nums[l]**2
                right = nums[r]**2
                if left < right:
                    answer.append(left)
                    l -=1
                else:
                    answer.append(right)
                    r+=1
            if l >=0:
                while 0 <= l:
                    answer.append(nums[l]**2)
                    l -= 1
            else:
                while r < len(nums):
                    answer.append(nums[r]**2)
                    r += 1
            
            return answer
        return nums



#another O(n) implementation that I like a lot more than the above one:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            left = nums[l]**2
            right = nums[r]**2
            if (left > right):
                answer.append(left)
                l += 1
            else:
                answer.append(right)
                r -= 1
        answer.reverse()
        return answer