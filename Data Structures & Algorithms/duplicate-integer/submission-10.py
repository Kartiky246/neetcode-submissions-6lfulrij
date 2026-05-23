class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()
        for i in range(len(nums)):
            if nums[i] in number_set:
                return True
            number_set.add(nums[i])
        return False