class Solution:
    def hasDuplicate(self, nums):
        numberSet = set()
        for _, num in enumerate(nums):
            if num in numberSet:
                return True
            numberSet.add(num)
        return False