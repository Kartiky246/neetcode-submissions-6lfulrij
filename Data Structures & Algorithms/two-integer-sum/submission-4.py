class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_set = {}
        for i in range(len(nums)):
            if target - nums[i] in number_set:
                return [number_set.get(target - nums[i]), i]
            number_set[nums[i]] = i
        return [-1,-1]
