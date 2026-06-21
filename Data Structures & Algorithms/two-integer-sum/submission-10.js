class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numberMap = new Map();
        for(let i =0; i< nums.length; i++){
            if(numberMap.has(target-nums[i])){
                return [numberMap.get(target - nums[i]), i]
            }
            numberMap.set(nums[i], i);
        }
        return [-1, -1]
    }
}
