class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if(nums[i]!=val):
                temp = nums[pointer]
                nums[pointer] = nums[i]
                nums[i] = temp
                pointer+=1
        return pointer