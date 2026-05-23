class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}
        for idx, num in enumerate(nums):
            if (target-num) in number_dict:
                return [number_dict.get(target-num), idx]
            number_dict[num] = idx
        return [-1, -1] 