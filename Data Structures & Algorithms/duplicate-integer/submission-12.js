class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numberSet = new Set();
        for(let v of nums){
            if(numberSet.has(v)) return true;
            numberSet.add(v);
        }
        return false
    }
}
