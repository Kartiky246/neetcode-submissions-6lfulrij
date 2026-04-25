class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const res = new Array(2*nums.length).fill(0);
        for(let i =0; i<nums.length; i++){
            res[i] = nums[i];
            const n = nums.length
            res[i+n] = nums[i];
        }
        return res;
    }
}
