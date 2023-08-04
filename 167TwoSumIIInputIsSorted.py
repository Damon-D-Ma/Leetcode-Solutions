class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers) - 1
        sum = 0
        while (ind1 != ind2):
            sum = numbers[ind1] + numbers[ind2]
            if sum == target:
                return [ind1+1, ind2+1]
            elif sum < target:
                ind1 += 1
            else:
                ind2 -= 1
        return [ind1+1, ind2+1]