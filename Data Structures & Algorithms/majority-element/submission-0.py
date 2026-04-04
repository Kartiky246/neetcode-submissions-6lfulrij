class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_map = {}
        for _ , num in enumerate(nums):
            number_map[num] = number_map.get(num, 0) + 1
            if number_map.get(num) >= (len(nums)/2):
                return num
        return -1