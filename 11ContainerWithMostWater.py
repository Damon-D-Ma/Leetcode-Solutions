class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = 0
        l = 0
        r = len(height) - 1
        while l < r:
            left = height[l]
            right = height[r]
            bucket_height = min(left, right)
            width = r - l
            curr = bucket_height*width
            if curr > highest:
                highest = curr

            if left > right:
                    r -= 1
            else:
                    l += 1

        return highest