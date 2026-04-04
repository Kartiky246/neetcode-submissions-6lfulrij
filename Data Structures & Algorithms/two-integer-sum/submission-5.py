class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx, num in enumerate(nums):
            if target - num in index_map:
                return [index_map.get(target-num), idx]
            index_map[num] = idx
        return [-1, -1]