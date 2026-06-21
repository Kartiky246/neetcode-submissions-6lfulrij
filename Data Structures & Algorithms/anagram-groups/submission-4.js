class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagramMap = new Map();
        for(let str of strs){
            const charKey = str.split('').sort().join('');
            if(anagramMap.has(charKey)){
                anagramMap.set(charKey, [...anagramMap.get(charKey), str]);
            }
            else{
                anagramMap.set(charKey, [str]);
            }
        }
        return Array.from(anagramMap.values())
    }
}
